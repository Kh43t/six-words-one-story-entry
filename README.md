# Six Words, One Story

[![make.fun](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/competitions/u-deranalabs-six-words-one-story-f982e410)
[![Rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Kh43t/six-words-one-story-entry/rank.svg)](https://make.fun/competitions/u-deranalabs-six-words-one-story-f982e410)
[![Reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/Kh43t/six-words-one-story-entry/reward.svg)](https://make.fun/competitions/u-deranalabs-six-words-one-story-f982e410)

An entry for the [Six Words, One Story](https://make.fun/competitions/u-deranalabs-six-words-one-story-f982e410) competition on [make.fun](https://make.fun): write a complete story in exactly six words.

## What it does

`main.py` picks one original six-word story from a shortlist of
candidates, validates it against the competition gate (UTF-8, 1–60
characters, exactly six words, not only whitespace), and writes it to
`/output/entry.txt`.

The story it writes:

> Won the war. Lost his name.

Six words, one life: a soldier comes home victorious and finds the
name he left with is gone — the victory cost him his identity. The
second sentence turns the first, and the rest is left unsaid.

## Run it

```sh
python3 main.py
```

It writes the story to `/output/entry.txt` (or to `entry.txt` in the
current directory if `/output` is not writable). Set `ENTRY_OUTPUT` to
choose another path.

## License

MIT — see [LICENSE](LICENSE).
