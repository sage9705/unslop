# Customer Feedback Analyzer

*`00-foundations/01-programming/examples/customer-feedback-analyzer/`, part of [Unslop](https://github.com/sage9705/unslop)*

## What It Does

Takes a batch of raw customer comments, the kind with inconsistent spacing and casing you'd actually get from a feedback form, and turns them into two useful things for a shop owner: a word frequency count, and a shortlist of comments that likely need a follow up.

## Concepts It Demonstrates

- [`09-strings.md`](../../concepts/09-strings.md), cleaning and parsing messy raw text
- [`07-collections.md`](../../concepts/07-collections.md), the comments themselves are a list, processed one at a time
- [`08-dictionaries-and-sets.md`](../../concepts/08-dictionaries-and-sets.md), the word frequency count is a dictionary keyed by word
- [`06-functions.md`](../../concepts/06-functions.md), each step, cleaning, counting, flagging, is its own small function

## How to Run

```bash
python main.py
```

## Sample Output

```
Total comments: 6
Comments flagged for follow up: 3
  - The cashier was really rude to me today.
  - My delivery was late again, third time this month.
  - The milk I bought was expired, please check your fridge.

Most common words:
  was: 4
  the: 3
  and: 3
  this: 2
  cashier: 1
```

## Try Changing

- Add `"overpriced"` to `NEGATIVE_KEYWORDS` and add a comment that mentions it, then confirm it gets flagged.
- Add three or four more comments to `feedback` and predict how the top words list shifts.
- Change `top_words(word_counts)` to `top_words(word_counts, count=3)` and confirm only three words print.
