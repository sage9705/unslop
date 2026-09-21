"""
Run this from the same folder stubborn.py wrote heartbeat.txt into:

    python verify.py
"""

import os
import time


def self_check():
    path = "heartbeat.txt"
    if not os.path.exists(path):
        print("heartbeat.txt not found. Did you run stubborn.py first?")
        return

    last_modified = os.path.getmtime(path)
    age = time.time() - last_modified

    if age > 3:
        print(f"heartbeat.txt hasn't updated in {age:.1f} seconds. It's actually stopped.")
        print("All checks passed.")
    else:
        print(f"heartbeat.txt was updated {age:.1f} seconds ago. Still running.")


self_check()
