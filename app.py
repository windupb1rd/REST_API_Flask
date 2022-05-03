from sqlalchemy import inspect, desc, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, abort
import requests
from sqlalchemy_utils import database_exists, create_database


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post_api_user:postapi@localhost:7432/post_api'
engine = create_engine('postgresql://post_api_user:postapi@localhost:7432/post_api')

if not database_exists(engine.url):
    create_database(engine.url)

db = SQLAlchemy(app)


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, nullable=False)
    question_text = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False)

    def obj_to_json(self):
        dictionary = {
            'question_id': self.question_id,
            'question_text': self.question_text,
            'answer': self.answer,
            'creation_date': self.creation_date,
        }

        return jsonify(dictionary)


if not inspect(engine).has_table('questions'):
    db.create_all()


@app.route('/api/questions', methods=['POST'])
def get_question():

    def get_question_from_api(questions_num: int) -> dict:

        return requests.get(f'https://jservice.io/api/random?count={questions_num}').json()

    def check_if_question_exists_and_get_new_one(question: object) -> object:
        if question in list_of_existing_questions_ids:
            question = get_question_from_api(1)
            return check_if_question_exists_and_get_new_one(question)

        return question

    if request.json and 'questions_num' in request.json:
        previous_entry = Questions.query.order_by(desc('id')).first()

        if previous_entry is None:
            result = {}
        else:
            result = previous_entry.obj_to_json()

        response_from_api = get_question_from_api(request.json['questions_num'])

        # Извлекаем ID вопросов из БД
        questions_ids= Questions.query.with_entities(Questions.question_id).all()
        list_of_existing_questions_ids = [question_id for tup in questions_ids for question_id in tup]

        for question in response_from_api:
            check_if_question_exists_and_get_new_one(question['id'])  # проверка каждого вопроса из выборки на наличие в БД

            db.session.add(Questions(question_id=question['id'],
                                     question_text=question['question'],
                                     answer=question['answer'],
                                     creation_date=question['created_at']))

        db.session.commit()

    else:
        abort(400)

    return result


if __name__ == '__main__':
    app.run(debug=False)
