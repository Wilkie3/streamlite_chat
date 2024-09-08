from locust import HttpUser, TaskSet, task, between
# Define the behavior of a user accessing the app
class UserBehavior(TaskSet):

    @task(1)
    def send_valid_request(self):
        """
        Simulate sending a valid POST request to the Flowise API.
        """
        payload = {"question": "What is the weather like in New York?"}
        self.client.post("/api/v1/prediction/037dd3d4-8492-45c4-9c5f-6ff84b8e95ee", json=payload)

    @task(1)
    def send_invalid_request(self):
        """
        Simulate sending an invalid POST request to the Flowise API.
        """
        payload = {"invalid_key": "This is an invalid request"}
        self.client.post("/api/v1/prediction/037dd3d4-8492-45c4-9c5f-6ff84b8e95ee", json=payload)

# Define the Load Testing User
class FlowiseUser(HttpUser):
    tasks = [UserBehavior]  # Define the tasks to perform
    wait_time = between(1, 5)  # Random wait time between tasks
    host = "http://localhost:9602"  # Your Streamlit app's base URL
