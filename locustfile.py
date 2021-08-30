from locust import HttpUser, TaskSet, task
from locust.user.wait_time import between

def index(self):
    self.client.get("/")

def post(self):
    self.client.post("/")

class UserTasks(TaskSet):
    tasks = [index, post]

    def on_start(self):
        pass

    def on_stop(self):
        pass

    # @task
    # def page404(self):
    #    self.client.get("/404")


class ChiUser(HttpUser):
    host = "http://127.0.0.1:8080"
    wait_time = between(2, 5)
    tasks = [UserTasks]
