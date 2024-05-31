# weather/tasks.py
from celery import shared_task

@shared_task
def fetch_and_store_data():
    print("working")



from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from .tasks import fetch_and_store_data
    sender.add_periodic_task(10.0, fetch_and_store_data.s(), name='Fetch and store data every 10 seconds')