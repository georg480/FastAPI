from locust import User, HttpUser, TaskSet, task, constant


class UserTasks(TaskSet):
    @task()
    def access_site(self):
        with self.client.get("/,", name="access site", catch_response=True) as response:
            print(response.status_code)
            if "Suce Labs Swag Labs app" in response.text and response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to access base url")

class BasicUser(HttpUser):
    host = "https://www.saucedemo.com"
    wait_time = constant(
    tasks = [UserTasks]

def on_start(self):
    self.client.post("/login", json={"username":"standard_user", "password":"secret_sauce"})
#login
#https://www.saucedemo.com/login