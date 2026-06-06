from integration import ProtectionSystem
import time

system = ProtectionSystem()

print("===== NORMAL TRAFFIC =====")

system.receive_request("user1", "Task 1")
system.receive_request("user1", "Task 2")
system.receive_request("user1", "Task 3")

print("\n===== QUEUE OVERFLOW TEST =====")

system.receive_request("user2", "Task 4")
system.receive_request("user2", "Task 5")

print("\n===== RATE LIMIT TEST =====")

for i in range(10):
    system.receive_request(
        "spammer",
        f"Spam Task {i}"
    )

print("\n===== PROCESS TASKS =====")

while system.queue_manager.current_size() > 0:
    system.queue_manager.process_task()
    time.sleep(1)