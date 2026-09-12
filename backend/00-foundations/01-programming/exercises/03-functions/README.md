# Exercise: Discount Engine

*`00-foundations/01-programming/exercises/03-functions/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The [`till-calculator`](../../examples/till-calculator/) example applies one flat discount. A real shop usually has more than one reason to discount an order, a loyal customer, or a bulk purchase, and they don't stack on top of each other. The shop only gives the customer whichever single discount benefits them the most.

## What You Need to Build

In `starter.py`, implement three functions:

1. **`calculate_loyalty_discount_rate(years_as_member)`**, returns a discount rate based on how long someone has been a member:

   - `0` years to under `2` years: `0`
   - `2` years to under `5` years: `0.05`
   - `5` years or more: `0.10`
2. **`calculate_bulk_discount_rate(quantity)`**, returns a discount rate based on how many units of a single item are being bought:

   - fewer than `10`: `0`
   - `10` to under `20`: `0.03`
   - `20` or more: `0.07`
3. **`calculate_final_price(price, quantity, years_as_member)`**, calculates the subtotal, works out both discount rates, applies **whichever one is larger** (never both at once), and returns the final price.

## Concepts You'll Need

- [`06-functions.md`](../../concepts/06-functions.md)
- [`04-conditionals.md`](../../concepts/04-conditionals.md), for the tiers inside each function

## Self Check

```bash
python starter.py
```

It checks each discount tier individually, then checks that `calculate_final_price` correctly picks the larger of the two discounts in several different scenarios. You should see `All checks passed.` with no errors.
