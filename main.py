from corylus.app import app
from corylus.huey_tasks.consumer import task_consumer
from multiprocessing import Process

if __name__ == '__main__':
    process = Process(target=task_consumer)
    process.start()
    app.run(debug=True)
    process.join()
