#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Picks one original six-word story from a shortlist of candidates,
validates it against the competition gate (UTF-8, 1-60 chars, exactly
six words, not only whitespace), and writes it to /output/entry.txt.
"""

import os
import sys


# Candidate stories, each written for this entry. Every candidate is
# exactly six words; the selector below only trusts a candidate after
# re-checking that fact, so a typo can never slip an invalid line out.
CANDIDATES = [
    "The letter said yes. Too late.",
    "She forgave him. The mirror didn't.",
    "Grandma's recipe: salt, love, and goodbye.",
    "Won the war. Lost his name.",
    "The will was read. Nobody came.",
]

# Words that mark the turn of the story: the second sentence flips
# the meaning of the first. A candidate carrying one scores higher.
TURN_WORDS = {
    "late", "didn't", "never", "goodbye", "nobody", "lost", "too",
}

GATE_MAX_CHARS = 60


def word_count(text):
    """Count words the way a reader would: split on whitespace."""
    return len(text.split())


def is_valid_story(text):
    """The gate, restated: UTF-8, 1-60 chars, not only whitespace,
    and exactly six words."""
    if not text or not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if len(text) > GATE_MAX_CHARS:
        return False
    return word_count(text) == 6


def twist_score(text):
    """Rank candidates: two sentences (setup, then turn) beat one,
    and a turn word in the closing sentence beats none."""
    score = 0
    sentences = [s for s in text.split(".") if s.strip()]
    if len(sentences) >= 2:
        score += 2
    closing = sentences[-1].lower() if sentences else ""
    for word in TURN_WORDS:
        if word in closing:
            score += 3
            break
    return score


def pick_story(candidates):
    """Return the strongest valid candidate, or None if none pass."""
    seen = set()
    unique = []
    for candidate in candidates:
        key = candidate.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate)
    valid = [c for c in unique if is_valid_story(c)]
    if not valid:
        return None
    # Highest twist score wins; on a tie the shorter line wins, so
    # every byte has to justify itself.
    valid.sort(key=lambda c: (twist_score(c), -len(c)), reverse=True)
    return valid[0]


def write_entry(story, output_path):
    """Write the story as UTF-8 text to the harness output path."""
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(story)
    return output_path


def main():
    story = pick_story(CANDIDATES)
    if story is None:
        print("error: no candidate passes the six-word gate", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        write_entry(story, output_path)
    except OSError:
        # The grading sandbox always provides /output; fall back to a
        # local file only so a manual run still leaves a trace.
        write_entry(story, "entry.txt")
        output_path = "entry.txt"
    print(f"wrote {word_count(story)}-word story to {output_path}: {story}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
