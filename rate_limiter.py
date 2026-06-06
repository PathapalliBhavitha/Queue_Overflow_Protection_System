import time


class RateLimiter:
    def __init__(self, max_requests=10, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    def allow_request(self, user_id):
        current_time = time.time()

        if user_id not in self.requests:
            self.requests[user_id] = []

        self.requests[user_id] = [
            t for t in self.requests[user_id]
            if current_time - t < self.time_window
        ]

        if len(self.requests[user_id]) >= self.max_requests:
            return False

        self.requests[user_id].append(current_time)
        return True