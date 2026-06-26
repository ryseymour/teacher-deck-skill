# Teacher Deck Builder — an AI Skill

Take a lesson plan you found online and rebuild it as a slide deck **in your school's
template** — same layouts, same opening routine — instead of losing half an hour
reformatting it by hand.

This is a free, portable [Agent Skill](https://www.anthropic.com/news/skills): a text
file (`SKILL.md`) plus a few small Python scripts. It is written for Claude, but because
it is just instructions you can paste the contents into whatever AI tool you use and it
should behave similarly.

It pairs with the Substack post *"Introducing AI Skills: A Practical Workflow for
Teachers."*

## What it does

Following a **Brief → Build → Check** workflow:

- **Brief.** Asks for three things: an example deck in your school's template, the lesson
  plan (with subject, grade, and your differentiation focus), and any opening routine or
  check-for-understanding you run every class.
- **Build.** Reads your template's real layouts, maps the lesson onto them, sources
  **openly-licensed (CC0) images** — and when it can't find one, drafts a generation
  prompt for you to approve rather than inventing something. Writes **teacher notes**
  (timing and differentiation) into each slide's notes pane.
- **Check.** Hands the deck back for you to read against your standards. You own the final
  call, and you can reprompt to adjust anything.

## Use it with Claude

1. Download this repo (or just `SKILL.md`).
2. Point Claude at `SKILL.md` (upload it, or paste its contents).
3. Say: *"Turn this lesson into slides in my school's template,"* and share your template
   and lesson when asked.

## Use the scripts directly

```bash
pip install -r scripts/requirements.txt

# 1. See your template's layouts and placeholders
python3 scripts/inspect_template.py your_template.pptx

# 2. Find openly-licensed images
python3 scripts/find_images.py "water cycle diagram" --download images/

# 3. Build the deck from a lesson JSON (see references/lesson_schema.md)
python3 scripts/build_deck.py --template your_template.pptx --lesson lesson.json --out deck.pptx
```

A worked Grade 3 science example is in `examples/lesson.example.json`.

## How it matches your template

`build_deck.py` opens your example `.pptx` as the base, so it inherits the theme, fonts,
colors, and slide layouts. It clears the example's slides (keeping the design) and adds
new ones on the layouts you name. That is the whole point: the output lands *inside* the
shape your school already uses, so there's nothing left to reformat.

## A note on images

The image search defaults to CC0, Public Domain Mark, and CC-BY. CC0 and public-domain
images need no attribution; CC-BY images do, so attribution is recorded in the slide notes
for every image, and a small credit line is added **on the slide itself** for CC-BY images
automatically. To restrict to no-attribution-required images only, pass `--license cc0,pdm`.
On-slide credit is controlled by `build_deck.py --credit-on-slide {auto,always,off}`
(default `auto` = CC-BY only).

## This is version one

It's meant to be adjusted. Try it on your next lesson and tell me where it breaks. The
places it falls short in your classroom are exactly what will make the next version
better. Issues and pull requests welcome, and if GitHub isn't your thing, **[share quick
feedback here](https://docs.google.com/forms/d/e/1FAIpQLSc0LG3JEm_2PCY18Zf730smPIEi8_jNwCVoUVjaQdL2RpE5Lg/viewform)**.

## License

[MIT](LICENSE). Built by [Ryan Seymour](https://github.com/ryseymour), Seymour Learning
Insights.
