# Categorical Variables and Interactions -- Debugging Practice

Coding 2 homework, companion to **Lecture 14: Categorical Variables and Interactions**.

## The project

`analysis.ipynb` regresses salary on experience, training, AI-tool use and sector, then adds a training-by-sector interaction using `data/career_outcomes.csv`. It follows the workflow from the
lecture:

1. Fit a model with a categorical sector predictor.
2. Add an interaction between training hours and sector.
3. Compare the two models and plot predicted salaries by sector.

## Your task

This project does not yet work the way it should. Clone it, get it running, and read it
critically: make sure every step actually does what it claims to do and that the
conclusions it reaches are justified. Fix whatever you find.

Work like an analyst reviewing a colleague's notebook -- at each step, ask where this could
go wrong and whether you believe the numbers.

You may use an LLM to help, but treat its suggestions as drafts: check them against the
data and against what the lecture says a sound workflow looks like.

## Running it

```bash
uv sync
uv run jupyter lab        # open analysis.ipynb and run it top to bottom
```

To execute the whole notebook from the command line:

```bash
uv run jupyter nbconvert --to notebook --execute analysis.ipynb --stdout
```

## Data

`data/career_outcomes.csv` is a small synthetic teaching dataset; no downloads are needed.
