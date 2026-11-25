"""One-star review of something essential.

Writes a single deadpan one-star review of gravity to /output/entry.txt.
The review must be one line, at most 160 characters, and hold the deadpan
all the way to the sting in its last few words.
"""

import os


REVIEW = (
    "One star for gravity. Works perfectly until my phone lands "
    "face-down, and customer service never answers."
)

# The grievance has to be the sharpest true one everyone recognises:
# gravity never fails, except that everything you drop lands on its
# worst side. The last clause is the turn: filed like a real complaint
# against a support desk that does not exist.
assert REVIEW == REVIEW.strip(), "no leading/trailing whitespace"
assert len(REVIEW) <= 160, "review over the 160-character limit"


def main() -> None:
    review = " ".join(REVIEW.split())
    if not review or len(review) > 160:
        raise SystemExit("review must be 1-160 characters")
    if "\n" in review:
        raise SystemExit("review must be a single line")
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(review + "\n")


if __name__ == "__main__":
    main()
