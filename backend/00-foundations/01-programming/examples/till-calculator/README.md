# Till Calculator

*`00-foundations/01-programming/examples/till-calculator/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Calculates the total a customer owes for an order: subtotal, a percentage discount, tax on top, and the change due from whatever cash they hand over. It also prints a readable receipt.

## Concepts It Demonstrates

- [`01-values-and-variables.md`](../../concepts/01-values-and-variables.md) and [`02-types.md`](../../concepts/02-types.md), prices, quantities, and totals as named values
- [`03-expressions-and-operators.md`](../../concepts/03-expressions-and-operators.md), the subtotal, discount, and tax calculations
- [`04-conditionals.md`](../../concepts/04-conditionals.md), checking whether the cash given was enough
- [`05-loops.md`](../../concepts/05-loops.md), adding up every line item in the order
- [`06-functions.md`](../../concepts/06-functions.md), the whole calculation is broken into small, reusable functions

## How to Run

```bash
python main.py
```

## Sample Output

```
==================================
CORNER SHOP RECEIPT
==================================
Rice bag          2 x  25.50 =   51.00
Cooking oil       1 x  18.00 =   18.00
Sugar             3 x  12.75 =   38.25
----------------------------------
TOTAL                        114.62
CASH GIVEN                   100.00
CHANGE                       -14.62
==================================
Not enough cash given for this order.
```

The sample order intentionally isn't fully covered by the cash given, so you can see the negative change case without changing anything.

## Try Changing

- Set `discount_percent=0` and predict how the total changes before rerunning.
- Raise `cash_given` to `120.00` and predict what the change should be.
- Add a fourth item to the `order` list and confirm the subtotal picks it up correctly.
- Set `tax_rate=0` and check the math still lines up by hand.
