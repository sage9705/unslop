"""
Customer Feedback Analyzer

Reads a batch of raw customer comments and turns them into something a
shop owner can act on: a word frequency count and a list of comments
that likely need a follow up. This is the reference example for
concepts 07 (collections) and 09 (strings), built on the functions
from concept 06.

Run it with:
    python main.py
    
    Look up language features you do not understand 
"""

NEGATIVE_KEYWORDS = ["late", "rude", "expired", "overcharged", "broken"]


def clean_comment(comment):
    return comment.strip().lower() # lowercase and strip a raw comment so it's easier to work with.


def count_words(comments):
    word_counts = {} # build a word frequency dictionary across all comments.

    for comment in comments:
        cleaned = clean_comment(comment)
        words = cleaned.replace(",", "").replace(".", "").split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def flag_negative_comments(comments, keywords):
    flagged = []

    for comment in comments:
        cleaned = clean_comment(comment)
        for keyword in keywords:
            if keyword in cleaned:
                flagged.append(comment.strip())
                break

    return flagged # return the original comments that contain at least one negative keyword, so a shop owner can follow up on them directly.


def top_words(word_counts, count=5):
    return sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)[:count] # return the most frequent words as a list of (word, count) pairs


if __name__ == "__main__":
    feedback = [
        "  The cashier was really rude to me today.  ",
        "Great prices and the rice was fresh.",
        "My delivery was late again, third time this month.",
        "Love this shop, always clean and well stocked.",
        "The milk I bought was expired, please check your fridge.",
        "Friendly staff and fast service.",
    ]

    word_counts = count_words(feedback)
    flagged = flag_negative_comments(feedback, NEGATIVE_KEYWORDS)

    print(f"Total comments: {len(feedback)}")
    print(f"Comments flagged for follow up: {len(flagged)}")
    for comment in flagged:
        print(f"  - {comment}")

    print()
    print("Most common words:")
    for word, count in top_words(word_counts):
        print(f"  {word}: {count}")

