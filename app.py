from flask import Flask, request, jsonify, abort
import requests, datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
engine = create_engine('postgresql://post_api_user:postapi@localhost:5432/post_api')
if not database_exists(engine.url):
    create_database(engine.url)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post_api_user:postapi@localhost:5432/post_api'



class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    question_id = db.Column(db.String(1000), nullable=False)
    question_text = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return self.question_id


@app.route('/api/questions', methods=['POST'])
def get_question():
    if request.json and 'questions_num' in request.json:
        questions_num = request.json['questions_num']
        response_from_api = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()

        # response_data = {}
        for question in response_from_api:
            db.session.add(Questions(question_id=question['id'],
                                     question_text=question['question'],
                                     answer=question['answer'],
                                     creation_date=question['created_at']))

        db.session.commit()
        result = Questions.query.order_by(desc('id')).filter_by(id=3)
        print(result)
        # result = {}

    else:
        abort(400)

    return {}


if __name__ == '__main__':
    app.run(debug=True)
