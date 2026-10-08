"""
Exercise: File Backed Restock List

Implement the six functions below. See README.md in this folder for
the full problem description.
"""

import json
import os
import tempfile

STATUSES = ["pending", "ordered", "received"]


def load_list(filepath):
    """Load the restock list from filepath, as a list of item dicts.

    Each item looks like:
        {"id": 1, "name": "Sugar", "quantity": 30, "status": "pending"}

    If the file doesn't exist yet, return an empty list.
    """
    raise NotImplementedError("TODO: implement load_list")


def save_list(items, filepath):
    """Save the restock list to filepath as JSON."""
    raise NotImplementedError("TODO: implement save_list")


def add_item(items, name, quantity):
    """Add a new item to the list with status "pending", and return it.

    The new item's id is one higher than the highest id already in the
    list, or 1 if the list is empty.

    Raises ValueError if name is blank, or quantity isn't a positive
    whole number.
    """
    raise NotImplementedError("TODO: implement add_item")


def update_status(items, item_id, new_status):
    """Move an item forward to its next status.

    An item can only move one step at a time, in this order:
        pending -> ordered -> received

    Raises KeyError if no item has that id.
    Raises ValueError if new_status isn't one of the three statuses,
    or isn't the very next step for that item.
    """
    raise NotImplementedError("TODO: implement update_status")


def pending_items(items):
    """Return a list of every item whose status is "pending"."""
    raise NotImplementedError("TODO: implement pending_items")


def remove_received(items):
    """Return a NEW list without the received items. The list passed
    in must be left unchanged."""
    raise NotImplementedError("TODO: implement remove_received")


def self_check():
    items = []

    sugar = add_item(items, "Sugar", 30)
    flour = add_item(items, "Flour", 20)
    assert sugar == {"id": 1, "name": "Sugar", "quantity": 30, "status": "pending"}
    assert flour["id"] == 2

    for bad_name, bad_quantity in (("", 5), ("   ", 5), ("Rice", 0), ("Rice", -3), ("Rice", "ten")):
        try:
            add_item(items, bad_name, bad_quantity)
            assert False, f"expected ValueError for ({bad_name!r}, {bad_quantity!r})"
        except ValueError:
            pass
    assert len(items) == 2, "a rejected item must not be added to the list"

    update_status(items, 1, "ordered")
    assert items[0]["status"] == "ordered"
    update_status(items, 1, "received")
    assert items[0]["status"] == "received"

    try:
        update_status(items, 2, "received")
        assert False, "expected ValueError for skipping a step"
    except ValueError:
        pass
    try:
        update_status(items, 2, "shipped")
        assert False, "expected ValueError for an unknown status"
    except ValueError:
        pass
    try:
        update_status(items, 99, "ordered")
        assert False, "expected KeyError for an id that doesn't exist"
    except KeyError:
        pass

    waiting = pending_items(items)
    assert [item["name"] for item in waiting] == ["Flour"]

    remaining = remove_received(items)
    assert [item["name"] for item in remaining] == ["Flour"]
    assert len(items) == 2, "remove_received must not change the original list"

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "restock.json")
        assert load_list(path) == [], "a missing file should load as an empty list"

        save_list(items, path)
        reloaded = load_list(path)
        assert reloaded == items, "a saved list should load back identical"

        newest = add_item(reloaded, "Bread", 12)
        assert newest["id"] == 3, "ids must keep counting up after a reload"

    print("All checks passed.")


if __name__ == "__main__":
    self_check()
