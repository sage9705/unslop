# Stock Reorder Alert

*`00-foundations/01-programming/examples/stock-reorder-alert/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Scans a shop's inventory and flags anything that's out of stock or running low, so nobody finds out a product is gone by watching a customer walk out empty handed.

## Concepts It Demonstrates

- [`04-conditionals.md`](../../concepts/04-conditionals.md), the out of stock versus low stock versus fine logic
- [`05-loops.md`](../../concepts/05-loops.md), checking every product in the inventory, one at a time
- [`08-dictionaries-and-sets.md`](../../concepts/08-dictionaries-and-sets.md), the inventory is a dictionary rather than a list, deliberately, see [`problem-solving/05-complexity-basics.md`](../../problem-solving/05-complexity-basics.md) for why that choice matters as a catalog grows

## How to Run

```bash
python main.py
```

## Sample Output

```
REORDER:       Sugar (3 left)
OUT OF STOCK:  Cooking oil
REORDER:       Bread (4 left)

3 product(s) need attention: Sugar, Cooking oil, Bread
```

## Try Changing

- Lower `threshold` to `2` and predict which products still get flagged.
- Add a new product to `inventory` with a quantity of `0` and confirm it's caught.
- Raise every quantity in `inventory` well above the threshold and confirm the "Everything is well stocked" message appears instead.
