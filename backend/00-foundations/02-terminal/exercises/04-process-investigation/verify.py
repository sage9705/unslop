"""
Run this from the same folder stuck.py wrote heartbeat.txt into:

    python verify.py
"""

import os
import time


def self_check():
    path = "heartbeat.txt"
    if not os.path.exists(path):
        print("heartbeat.txt not found. Did you run stuck.py first?")
        return

    last_modified = os.path.getmtime(path)
    age = time.time() - last_modified

    if age > 3:
        print(f"heartbeat.txt hasn't updated in {age:.1f} seconds. The process looks stopped.")
        print("All checks passed.")
    else:
        print(f"heartbeat.txt was updated {age:.1f} seconds ago. The process might still be running.")


self_check()
