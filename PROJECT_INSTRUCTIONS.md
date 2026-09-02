# Chinese Flashcard Project — Instructions

## Context

Clarence is studying Mandarin Chinese at the HSK 4 level. After each class, he uploads a PDF of his lesson slides. The goal is to extract new vocabulary and build a growing flashcard app he can use to review weekly.

---

## When a PDF is uploaded

Extract vocabulary words from **all of the following sources** in the slides:

1. **词汇 (cí huì) sections** — explicit vocabulary slides. Format is usually: hanzi | pinyin | part of speech + English meaning.
2. **Blue-colored words with pinyin written above them** — these appear inline in reading passages (课文) and exercises. The pinyin will be rendered just above the Chinese characters.
3. **Red-highlighted words** — usually the 语言点 (grammar/language point) being taught that lesson. Include these as vocabulary cards too.
4. **Any word with pinyin annotation**, regardless of slide type.

Do NOT include:
- Ordinary black-text Chinese that has no pinyin annotation and is not in a 词汇 section
- Proper nouns (character names like 王静, 孙月, place names like 北京)
- Numbers and basic measure words already at HSK 1-2 level (一, 二, 年, 个, etc.)

---

## For each extracted word, collect

| Field | Source |
|---|---|
| **hanzi** | The Chinese characters |
| **pinyin** | The pinyin shown above/beside the word |
| **meaning** | English definition (part of speech + meaning) |
| **usage** | 1–2 example sentences from the slides (if available). Each usage entry must include: the Chinese sentence (`zh`), the full pinyin romanisation (`pinyin`), and an English translation (`en`). |
| **lesson** | The PDF filename (e.g. `Slides_20260408`) |

---

## Output

### 1. Update the vocabulary data file

Append new words to `/flashcards/vocabulary.json`. Do not duplicate words that already exist (match on hanzi). If a word already exists but the new PDF provides a better usage example, you may update the usage field.

### 2. Regenerate the flashcard app

After updating `vocabulary.json`, regenerate `flashcards/index.html` — a single self-contained HTML flashcard app that:
- Embeds all vocabulary data directly (no separate JSON file needed)
- Shows one card at a time: **front = hanzi**, **back = pinyin + meaning + usage example**
- Has simple flip, next, previous navigation
- Shows current card number and total (e.g. "12 / 47")
- Has a "shuffle" button
- Is clean and mobile-friendly

---

## Flashcard design principles

- Keep it simple — no complex interactivity needed
- Prioritize readability: hanzi should be large (at least 64px)
- Pinyin should appear directly above or just after the hanzi on the back
- Usage examples help with memory — always show them if available
- The app will grow over time as more lessons are added

---

## Workflow summary

1. User uploads a PDF → extract vocabulary using the rules above
2. Show the user a summary of extracted words (table: hanzi | pinyin | meaning) and ask for confirmation or corrections
3. Once confirmed, update `vocabulary.json` and regenerate `index.html`
4. Share a link to the updated flashcard app
