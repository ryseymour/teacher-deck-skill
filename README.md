# Teacher Deck Builder: An AI-Assisted System

This project is a portable AI Agent Skill designed to bridge the gap between generic AI
content and classroom-ready materials.

Most teachers face a "rework trap": they use AI to generate a lesson, but the output is
generic and fails to align with their school's existing templates, fonts, or lesson
structure. They end up spending more time formatting the AI output than they would have
spent building the lesson from scratch.

This system solves that problem. It takes a lesson plan from any source and rebuilds it
directly inside your school's specific PowerPoint template.

## The Workflow: Brief → Build → Check

This system operates on a human-in-the-loop framework. The goal is not to replace the
teacher, but to automate the constraint-fitting that needlessly consumes prep time.

- **Brief.** You provide the AI with your specific context: a sample deck in your school
  template, the lesson plan, and your preferred routines for checking understanding.
- **Build.** The agent reads your template's actual layouts and maps the lesson content
  onto them. It sources openly-licensed (CC0) images, writes teacher notes (including
  timing and differentiation) into the slides, and generates image-generation prompts for
  you to review if the right media is missing.
- **Check.** You own the final call. The output is a formatted deck that lands exactly in
  the shape your school requires, leaving no reformatting for you to do.

## How to use it

### Option 1: The Agent Approach (Claude)

This is an Agent Skill file (`SKILL.md`) plus a set of Python scripts.

1. Download this repository, or copy the contents of `SKILL.md`.
2. Upload or paste the contents into your preferred AI agent (Claude is recommended).
3. Give the instruction: *"Turn this lesson into slides in my school's template,"* and
   provide your files when prompted.

### Option 2: The Script Approach

For more control, run the Python scripts directly.

```bash
# 1. Install dependencies
pip install -r scripts/requirements.txt

# 2. Inspect your template's available layouts
python3 scripts/inspect_template.py your_template.pptx

# 3. Find openly-licensed images
python3 scripts/find_images.py "water cycle diagram" --download images/

# 4. Build the deck
python3 scripts/build_deck.py --template your_template.pptx --lesson lesson.json --out deck.pptx
```

A worked Grade 3 science example is in `examples/lesson.example.json`.

## System Features

### Template-Aware Formatting

The `build_deck.py` script opens your existing `.pptx` file as the base. It inherits your
fonts, theme, and colors, then clears the example slides while keeping the design. The
generated output requires zero manual formatting.

### Media Attribution

The image search defaults to CC0, Public Domain, and CC-BY licenses. Attribution is
recorded in the slide notes for every image, and a small credit line is added to the slide
automatically for CC-BY assets. You can restrict searches to no-attribution-required
images by passing `--license cc0,pdm`.

### Differentiation Support

Differentiation techniques and timing are mapped from the lesson source directly into the
slide notes, supporting the teacher without cluttering the student-facing view.

## Feedback

This is version one, and it is meant to be adjusted. Try it on your next lesson and tell me
where it breaks. Issues and pull requests are welcome, and if GitHub isn't your thing,
**[share quick feedback here](https://docs.google.com/forms/d/e/1FAIpQLSc0LG3JEm_2PCY18Zf730smPIEi8_jNwCVoUVjaQdL2RpE5Lg/viewform)**.

## License

[MIT](LICENSE). Built by [Ryan Seymour](https://github.com/ryseymour), Seymour Learning Insights.
