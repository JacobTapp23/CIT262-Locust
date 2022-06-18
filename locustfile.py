from locust import HttpUser, between, task

class WebsiteUser(HttpUser):

    @task 
    def index(self):
        self.client.get("/")
    
    @task
    def index(self):
        self.client.post("/login", json={"userName": "jacobtapp12@byui.edu", "password": "Kikagabe12$$"})

