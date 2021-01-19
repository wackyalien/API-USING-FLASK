from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String,nullable=False)
    Likes = db.Column(db.Integer,nullable=False)
    Views = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Video(Name = {Name},Likes = {Likes}, Views = {Views})"

# db.create_all()

resource_fields = {
    'id': fields.Integer,
    'Name': fields.String,
    'Likes': fields.String,
    'Views': fields.String
}


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("Name",type=str,help="Name of the video",required = True)
video_put_args.add_argument("Likes",type=int,help="Likes on the video",required = True)
video_put_args.add_argument("Views",type=int,help="Views of the video",required = True)


class video(Resource):

    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message="could not found...")
        return result

    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result:
            abort(409,message="video id taken")
        video = VideoModel(id = video_id, Name=args['Name'], Likes=args['Likes'], Views=args['Views'])
        db.session.add(video)
        db.session.commit()
        return video,201

    # def delete(self,video_id):
    #     abort_if_videoid_doesnt_exist(video_id)
    #     del videos[video_id]
    #     return '',204

api.add_resource(video,'/video/<int:video_id>')


if __name__ =="__main__":
    app.run(debug=True)