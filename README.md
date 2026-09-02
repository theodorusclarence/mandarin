# Mandarin

HSK 4 vocabulary flashcards, built up week by week from class slides.

**[Open the flashcards →](https://theodorusclarence.github.io/mandarin/flashcards/)**
**[Open the SRS review →](https://theodorusclarence.github.io/mandarin/srs/)**

## What's here

| Path | What it is |
|---|---|
| `flashcards/index.html` | Self-contained flashcard app. Vocab is embedded, so it works offline. |
| `flashcards/vocabulary.json` | Source of truth for all vocabulary. |
| `srs/index.html` | Spaced-repetition review app with Again/Hard/Good/Easy grading. |
| `PROJECT_INSTRUCTIONS.md` | How new lessons get extracted and added. |

## Flashcards

Filter by lesson using the pills at the top. Front of the card is the hanzi; reveal shows pinyin, meaning, and an example sentence taken from the slide the word appeared on. Example pinyin is hidden until you hover or tap it, so you can test yourself on the sentence first.

**Keyboard:** `Space` reveal / next · `O` toggle · `←` unreveal, then previous · `→` next · `S` shuffle

## Adding a lesson

Class slides are exported as `Slides_YYYYMMDD.pdf`. Words come from three places on the slides:

1. 词汇 vocabulary tables
2. Blue-annotated words (`#0070c0`) inline in reading passages and exercises
3. Red-highlighted 语言点 grammar points

The blue annotations matter most — those are the words the teacher marked as new. They can't be read from the PDF's plain text layer, which discards colour; `extract_slides.py` reads character colours and positions instead and groups them back into words.

Proper nouns, and HSK 1–2 words that appear without annotation, are skipped.
