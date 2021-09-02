from locust import HttpUser, SequentialTaskSet, task, between
import re

USERNAME="admin"
PASSWORD="hogefuga"

class UserBehavior(SequentialTaskSet):
    def on_start(self):
        self.login()
    
    def on_stop(self):
        self.logout()

    # 1番目に実行
    @task
    def login(self):
        response = self.client.get("/login")

        # ログインページにcsrf-paramとcsrf-tokenがあるはずなので、loginページから取得する
        csrf_param = re.search("<meta name=\"csrf-param\" content=\"([^\"]+)\" />", response.text).group(1)
        csrf_token = re.search("<meta name=\"csrf-token\" content=\"([^\"]+)\" />", response.text).group(1)

        self.client.post("/login", {"username": USERNAME, "password": PASSWORD, csrf_param: csrf_token})
    
    def logout(self):
        response = self.client.get("/")

        csrf_param = re.search("<meta name=\"csrf-param\" content=\"([^\"]+)\" />", response.text).group(1)
        csrf_token = re.search("<meta name=\"csrf-token\" content=\"([^\"]+)\" />", response.text).group(1)

        self.client.post("/logout", {csrf_param: csrf_token})
    
    @task
    def top(self):
        self.client.get("/")

    @task
    def mypage(self):
        with self.client.get("/my/page", catch_response = True) as response:
            if response.status_code != 200:
                response.failure("/my/page failed")
    
    @task
    def projects(self):
        self.client.get("/projects")

class RedmineUser(HttpUser):
    host = "http://localhost:3000"
    tasks = [UserBehavior]
    wait_time = between(20, 600)
