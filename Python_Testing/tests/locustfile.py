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
