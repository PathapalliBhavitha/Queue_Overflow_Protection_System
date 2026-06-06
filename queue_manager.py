from queue import Queue
from overflow_handler import OverflowHandler


class QueueManager:

    def __init__(self, max_size=5):
        self.queue = Queue(maxsize=max_size)

    def add_task(self, task):

        if self.queue.full():
            OverflowHandler.handle_overflow(task)
            return False

        self.queue.put(task)
        print(f"Task Added: {task}")
        return True

    def process_task(self):

        if self.queue.empty():
            print("Queue Empty")
            return

        task = self.queue.get()
        print(f"Processing: {task}")

    def current_size(self):
        return self.queue.qsize()