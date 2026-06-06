class OverflowHandler:

    @staticmethod
    def handle_overflow(task):
        print(f"[OVERFLOW] Task rejected: {task}")
        return False