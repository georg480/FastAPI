from locust import HttpUser, between, task


class Quickstart(HttpUser):
    wait_time = between(3, 10)
    host = "http://127.0.0.1:88"

    @task
    def test_root(self):
        """test root erstellen

        Return
        -------
        object
        """
        self.client.get("/")

    @task
    def test_hello(self):
        """test hello erstellen

        Return
        -------
        object
        """
        self.client.get("/hallo")
