# Lesson JSON schema

This is the structured shape `build_deck.py` reads. Fill it in from the teacher's lesson
plan and the template you inspected. Use the **real layout names** from
`inspect_template.py`, not generic guesses.

## Top level

| Field            | Required | Notes                                                        |
|------------------|----------|--------------------------------------------------------------|
| `deck_title`     | no       | Used for your reference; the title slide's `title` drives the deck title. |
| `subject`        | no       | e.g. "Science"                                               |
| `grade`          | no       | e.g. "Grade 3"                                               |
| `differentiation`| no       | The differentiation focus the teacher named.                 |
| `slides`         | **yes**  | Ordered list of slide objects (below).                       |

## Each slide object

| Field                     | Required | Notes                                                                 |
|---------------------------|----------|-----------------------------------------------------------------------|
| `layout`                  | no       | Layout name (from `inspect_template.py`) or integer index. Defaults to layout 1. |
| `title`                   | no       | Slide title text.                                                     |
| `bullets`                 | no       | List of strings; one bullet per item.                                 |
| `image`                   | no       | Local path to an image file (download with `find_images.py`).         |
| `image_credit`            | no       | Attribution string; written into the slide notes.                     |
| `notes`                   | no       | Teacher notes: suggested timing + differentiation moves.              |
| `check_for_understanding` | no       | A CFU question; appended to the slide notes.                          |

## Conventions

- Put the school's **opening routine / check-for-understanding slide first** if they gave
  you one.
- Keep bullets short. The deck should look like the school's, not a wall of text.
- Always write `notes` for content slides: a teacher reads these while presenting.
- Record `image_credit` for every image, even CC0, so attribution travels with the deck.
