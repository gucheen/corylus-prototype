from flask import g
from flask_restful import Resource, reqparse, marshal_with, fields
from flask_restful.inputs import boolean

from corylus.models.task import Task
from corylus.huey_tasks.tasks import render_to_png
import uuid
import arrow

task_fields = {
    'name': fields.String,
    'target_url': fields.String,
    'file_id': fields.String,
    'id': fields.Integer,
    'status': fields.Integer,
    'created_at': fields.Integer
}


class TaskList(Resource):
    @marshal_with(task_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('offset', type=int, default=0)
        parser.add_argument('limit', type=int, default=10)
        args = parser.parse_args()
        tasks = g.session.query(Task).offset(args.offset).limit(args.limit).all()
        return tasks

    @marshal_with(task_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('target_url', required=True)
        parser.add_argument('sync')
        args = parser.parse_args()
        file_id = str(uuid.uuid4())
        sync = boolean(args.sync)
        result = None
        if sync:
            res = render_to_png(args.target_url, file_id, sync)
            result = res(blocking=sync)
        else:
            render_to_png(args.target_url, file_id, sync)
        time = arrow.utcnow()
        print(result)
        task = Task(
            name=args.name,
            target_url=args.target_url,
            created_at=time.timestamp,
            file_id=file_id,
            status=1 if (result and result['success']) else 0
        )
        g.session.add(task)
        g.session.commit()
        return task


class TaskItem(Resource):
    @marshal_with(task_fields)
    def get(self, task_id):
        task = g.session.query(Task).get(task_id)
        return task
