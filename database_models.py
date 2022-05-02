# from flask_sqlalchemy import SQLAlchemy
#
# from app import app
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post_api_user:postapi@localhost:5432/post_api'
# db = SQLAlchemy(app)
#
#
# class Questions(db.Model):
#     __tablename__ = 'questions'
#     id = db.Column(db.Integer , primary_key=True , autoincrement=True)
#     question_id = db.Column(db.String(1000), nullable=False)
#     question_text = db.Column(db.String(1000), nullable=False)
#     answer = db.Column(db.String(1000), nullable=False)
#
#     def __repr__(self):
#         return self.question_id
#

