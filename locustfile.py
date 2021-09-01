from locust import HttpUser, TaskSet
from locust.user.wait_time import between


def getNewItem(self):
    self.client.get("/new_items.json")


def getNewCategoryItems(self):
    self.client.get("/new_items/1.json")


def getTransaction(self):
    self.client.get("/users/transactions.json")


def getUserItems(self):
    self.client.get("/users/1.json")


def getItem(self):
    self.client.get("/items/1.json")


def postItemEdit(self):
    dummy_data = {
        "csrf_token": "hogefugapiyo",
        "item_id": 1,
        "item_price": 101,
    }
    self.client.post("/items/edit", headers={"Content-Type": "application/json"}, json=dummy_data)

def postBuy(self):
    dummy_data = {
        "csrf_token": "hogefugapiyo",
        "item_id": 1,
        "token": "hogefugapiyo",
    }
    self.client.post("/buy", headers={"Content-Type": "application/json"}, json=dummy_data)

class UserTasks(TaskSet):
    tasks = [
        getNewItem,
        getNewCategoryItems,
        getTransaction,
        getUserItems,
        getItem,
        postItemEdit,
        postBuy,
    ]

    def on_start(self):
        pass

    def on_stop(self):
        pass

    # @task
    # def page404(self):
    #    self.client.get("/404")


class ChiUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(2, 5)
    tasks = [UserTasks]
