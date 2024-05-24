from endpoints import Endpoints


class Lessons:
    def __init__(self, client):
        self.client = client

    def get_next_lesson(self):
        endpoint = Endpoints.next_lesson
        response = self.client.make_request(endpoint=endpoint)
        return response.json()

    def hours_until_next_lesson(self):
        next_lesson = self.get_next_lesson()
        return next_lesson['hours_until_next_lesson']