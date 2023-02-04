from locust import HttpUser, task, between

class Quickstart(HttpUser):
    wait_time = between(3, 10)
    host = "http://127.0.0.1:88"
    @task
    def test_root(self):
        self.client.get("/")

    @task
    def test_hello(self):
        self.client.get("/hallo")