from corylus.database import db_session
from corylus.models.task import Task
from corylus.huey_tasks.config import huey
from huey.consumer import EVENT_FINISHED


def process_result(event, result):
    session = db_session()
    session.query(Task).filter(Task.file_id == result['file_id']).update({'status': 1})
    session.commit()
    session.close()
    return


def task_consumer():
    for event in huey.storage:
        if event['status'] == EVENT_FINISHED:
            result = huey.result(event['id'])
            if result and not result['sync']:
                return process_result(event, result)
            else:
                return
        else:
            return
