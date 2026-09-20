"""
Run this from the same folder read_env.py wrote greeting.txt into:

    python verify.py
"""


def self_check():
    try:
        with open("greeting.txt") as f:
            content = f.read()
    except FileNotFoundError:
        print("greeting.txt not found. Did you run read_env.py?")
        return

    if "Unknown Shop" in content:
        print("greeting.txt still shows the default. SHOP_NAME may not have been set before running read_env.py.")
    else:
        print(f"Found: {content.strip()}")
        print("All checks passed.")


self_check()
