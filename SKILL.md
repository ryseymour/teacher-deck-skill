---
name: teacher-deck-builder
description: >-
  Turn a lesson plan you found somewhere else into a slide deck that matches your
  school's PowerPoint template, with openly-licensed images and teacher notes written
  into the slide notes. Use this when a teacher wants to convert an external lesson
  plan into presentation slides in their school's own format and structure.
license: MIT
---

# Teacher Deck Builder

Take a lesson plan a teacher found online and rebuild it as a slide deck **in their
school's template** — same layouts, same opening routine — so they don't lose half an
hour reformatting it by hand. The workflow is **Brief → Build → Check**: gather the
teacher's context, build inside it, then hand it back for the teacher to own the final
judgment.

Do **not** invent a lesson. The teacher already has one. Your job is to fit it to the
shape their school requires.

## When to use this

A teacher says something like "turn this lesson into slides for my class," "make this
match our deck template," or "build me a presentation from this lesson plan." If they
have not given you a template or a lesson yet, start at Step 1 (Brief).

## Step 1 — Brief (gather context, ask, do not assume)

Ask for these three things. Ask for whatever is missing; never guess at a school's
format.

1. **The Template.** An example `.pptx` that uses the school's slide template (any past
   deck works). This is where the theme, fonts, colors, and layouts come from.
2. **The Lesson.** The lesson plan (file, link, or pasted text), plus the **subject**,
   **grade level**, and the **differentiation** they have in mind.
3. **The Structure.** Any check-for-understanding questions or opening routines they run
   at the start of every class (for example, a "Do Now" or a knowledge-check slide).

If the teacher only has some of this, build with what you have and tell them plainly what
you assumed.

## Step 2 — Build

1. **Read the template's layouts.** Run:
   ```
   python3 scripts/inspect_template.py "<template.pptx>"
   ```
   It prints the layout names and the placeholders on each, plus the theme fonts. Use
   the real layout names from this output when you fill in the lesson JSON — that is what
   makes the deck match the school's format instead of a generic one.

2. **Map the lesson into the structured JSON.** Write a `lesson.json` following
   `references/lesson_schema.md` (see `examples/lesson.example.json` for a worked Grade 3
   science example). For each slide set: the layout to use (by the real name from step 1),
   the title, the bullet content, an optional image, and the **teacher notes** —
   suggested timing for the section and the differentiation moves for the students who
   need them. Put the school's opening routine / check-for-understanding slide first if
   they gave you one.

3. **Source images, license-first.** For any slide that needs a visual, search openly-
   licensed sources before generating anything:
   ```
   python3 scripts/find_images.py "search terms" --download images/
   ```
   This returns CC0 / public-domain results from Openverse with attribution. Put the
   downloaded path in the slide's `image` field and the returned attribution in
   `image_credit`.
   - **If nothing suitable comes back, do not silently invent an image.** Tell the
     teacher, then draft a generation prompt and show it to them to adjust before you
     generate. Images usually take a couple of rounds to match what the lesson is
     actually doing; treat it as collaborative.

4. **Generate the deck.** Run:
   ```
   python3 scripts/build_deck.py --template "<template.pptx>" --lesson lesson.json --out "<output.pptx>"
   ```
   By default this keeps the template's theme and layouts and replaces only the slide
   content. Teacher notes go into each slide's notes pane; image attribution is appended
   there too.

## Step 3 — Check (the teacher owns this)

Hand the deck back and say what you did and what you assumed. Ask the teacher to read it
against their standards and their sense of the class. Offer to adjust: a different layout,
tighter bullets, a regenerated image, a different opening routine. **The teacher makes the
final call.** This step is the point of the whole thing — the tool fits the format so the
teacher can spend their attention on the parts no model should touch.

## Notes and guardrails

- **Match, don't reinvent.** Reuse the template's layouts and routine. If the model output
  lands "just outside" the school's shape, the teacher is back to reformatting and the
  time savings disappear.
- **Be honest about images.** Prefer CC0 / public domain. Record attribution even when a
  license does not require it. Never present an unclear license as cleared.
- **Reprompt freely.** This Skill is meant to be adjusted. If something is missing,
  change the lesson JSON or the instructions and rebuild.
- **Portable.** This is just a text file plus scripts. It is written for Claude, but the
  instructions read the same in any agent that can run Python.
