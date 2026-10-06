# Exercise: Work With JSON

*`00-foundations/03-files-and-data/exercises/04-work-with-json/`, part of [Unslop](https://github.com/sage9705/unslop)*

## The Problem

The shop's settings and catalog now live in JSON files, `shop_config.json` and `catalog.json`. A supplier has announced a price rise, and a second supplier has sent a list of updated and brand new products. The owner needs to apply both without damaging the catalog they already have, in case the new numbers turn out to be wrong.

That last requirement matters. Both of your changes have to produce a new catalog and leave the original alone.

## What You Need to Build

In `starter.py`, implement four functions:

1. **`load_json(filepath)`**, reads a JSON file and returns the Python data inside it.
2. **`save_json(data, filepath)`**, writes data to a file as JSON, indented with 2 spaces.
3. **`apply_price_increase(catalog, percent)`**, returns a new catalog with every price raised by `percent`, rounded to 2 decimal places.
4. **`merge_catalogs(base, updates)`**, returns a new catalog with everything from `base`, plus everything from `updates`, where an updated product replaces the old version.

## Concepts You'll Need

- [`08-json.md`](../../concepts/08-json.md)
- [`09-serialization-and-deserialization.md`](../../concepts/09-serialization-and-deserialization.md)
- [`11-mutation-and-references.md`](../../../01-programming/concepts/11-mutation-and-references.md), from `01-programming`, for leaving the original untouched

## Self Check

```bash
python starter.py
```

`self_check()` confirms your results, and confirms the original catalog survived both operations unchanged. It saves into a temporary folder, so nothing gets left behind. You should see `All checks passed.`
