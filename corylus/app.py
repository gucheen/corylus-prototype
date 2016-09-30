from flask import Flask, send_from_directory, g
from flask_restful import Resource, Api

from database import db_session
from resources.task import TaskList, TaskItem

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@app.route('/png/<string:file_id>')
def send_png(file_id):
    return send_from_directory('data/png', file_id + '.png', mimetype='image/png')


@app.before_request
def create_session():
    g.session = db_session()


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


api.add_resource(HelloWorld, '/')
api.add_resource(TaskList, '/task')
api.add_resource(TaskItem, '/task/<int:task_id>')

if __name__ == "__main__":
    app.run(debug=True)
