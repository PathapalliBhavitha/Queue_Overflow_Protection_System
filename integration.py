from rate_limiter import RateLimiter
from queue_manager import QueueManager


class ProtectionSystem:

    def __init__(self):
        self.rate_limiter = RateLimiter(
            max_requests=5,
            time_window=10
        )

        self.queue_manager = QueueManager(
            max_size=3
        )

    def receive_request(self, user_id, task):

        if not self.rate_limiter.allow_request(user_id):
            print(
                f"[RATE LIMITED] User {user_id}"
            )
            return False

        return self.queue_manager.add_task(task)