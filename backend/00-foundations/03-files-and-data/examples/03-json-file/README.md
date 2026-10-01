# Catalog JSON Converter

*`00-foundations/03-files-and-data/examples/03-json-file/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Converts the shop's old comma-separated `catalog.txt` into `catalog.json`, then loads it straight back, proving the round trip is exact, byte for byte the same data it started with.

## Concepts It Demonstrates

- [`07-structured-data.md`](../../concepts/07-structured-data.md), the same catalog, two different representations
- [`08-json.md`](../../concepts/08-json.md), objects and arrays matching Python dicts and lists
- [`09-serialization-and-deserialization.md`](../../concepts/09-serialization-and-deserialization.md), `json.dump` and `json.load`

## How to Run

```bash
python main.py
```

## Sample Output

```
Loaded from catalog.txt:
{'Rice bag': {'price': 25.5, 'quantity': 40}, 'Sugar': {'price': 12.75, 'quantity': 30}, 'Cooking oil': {'price': 18.0, 'quantity': 15}}

Saved as catalog.json

Loaded back from catalog.json:
{'Rice bag': {'price': 25.5, 'quantity': 40}, 'Sugar': {'price': 12.75, 'quantity': 30}, 'Cooking oil': {'price': 18.0, 'quantity': 15}}

Round trip matches exactly: True
```

`catalog.json` itself ends up looking like this:

```json
{
  "Rice bag": {
    "price": 25.5,
    "quantity": 40
  },
  "Sugar": {
    "price": 12.75,
    "quantity": 30
  },
  "Cooking oil": {
    "price": 18.0,
    "quantity": 15
  }
}
```

## Try Changing

- Open `catalog.json` directly in a text editor after running this once, compare how readable it is next to `catalog.txt`.
- Add a product name containing a comma, like `"Rice, 5kg bag"`, to `catalog.txt` and watch the old comma-split parsing break, then confirm the same name causes no trouble at all once it's stored as JSON.
