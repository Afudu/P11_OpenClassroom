"""
This file contains the performance test with locust configuration.

Here we define a class for the users that we will be simulating.
It inherits from HttpUser which gives each user a client attribute, which is an instance of HttpSession,
that can be used to make HTTP requests to the target system that we want to load test.
When a test starts, locust will create an instance of this class for every user that it simulates,
and each of these users will start running within their own green gevent thread.
For a file to be a valid locustfile it must contain at least one class inheriting from User.
"""

from locust import HttpUser, task, between


class AppLocustTest(HttpUser):
    # simulate users wait between 1 and 5 seconds after each task
    wait_time = between(1, 3)

    # will be called for each simulated user when they start.
    # A User will call its on_start method when it starts running,
    # and its on_stop method when it stops running.
    def on_start(self):
        self.client.get("/")

    @task
    def go_to_dashboard(self):
        self.client.get("/dashBoard")

    @task
    def show_summary(self):
        self.client.post("/showSummary", data={'email': 'john@simplylift.co'})

    @task
    def competition_booking_url_is_online(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def booking_a_competition(self):
        self.client.post("/purchasePlaces", data={"places": "1",
                                                  "club": "Simply Lift",
                                                  "competition": "Spring Festival"
                                                  })

    def on_stop(self):
        self.client.get("/logout")
