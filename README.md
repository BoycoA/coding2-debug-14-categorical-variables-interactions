# The Gender Wage Gap — Debugging Practice

**Homework 3 — Coding 2**, companion to **Lecture 14: Categorical Variables and Interactions**.

**Deadline: Wednesday, 25 November 2026.** Commit and push your completed work to your own
fork by this date. No new branch or pull request is required.

## The project

How do hourly wages differ between women and men, and does the relationship between
education and wages differ between them? Use a historical sample of 534 workers from
the 1985 US Current Population Survey, supplied in `data/cps1985.csv`.

`analysis.ipynb` follows three steps:

1. Inspect the data and visualise wage differences.
2. Fit a female-indicator model, then account for education and potential experience.
3. Add a female-by-education interaction and interpret the supplied education-slope calculations.

## Your task

This project does not yet work the way it should. Clone it, get it running, and read it
critically: make sure every step actually does what it claims to do and that the
conclusions it reaches are justified. Fix whatever you find.

Work like an analyst reviewing a colleague's notebook — at each step, ask where this could
go wrong and whether you believe the numbers.

You may use an LLM to help, but treat its suggestions as drafts: check them against the
data and against what the lecture says a sound workflow looks like.

## What you must submit

Submit **`analysis.ipynb` with working code, saved outputs, and completed Answer 1–3
cells**, plus any project configuration files you changed. No separate report is required.

| Question | What your answer must contain |
| --- | --- |
| 1. Get the notebook running | The error, its cause, your repair, and how you verified it. |
| 2. Check and interpret the wage gap | An indicator check, any repair, and the adjusted female coefficient's interpretation. |
| 3. Interpret the education slopes | The slopes calculated by the supplied code, their interpretations, and which group has the steeper relationship. |

Resolve execution problems first. Record the requested initial coefficient in Answer 2
before revising the analysis. Then complete the answers, restart the kernel, run all
cells, and save the outputs. Keep the supplied data unchanged and comparisons in log-wage units.

## Workflow: setup, debugging, and submission

There are two separate repositories. Use the **course folder** to update and launch
CEU AI. Use the **homework folder** to set up, run, commit, and push this assignment.

### 1. Update your course repository

Exit CEU AI with `/quit` if it is running. In a terminal in your main
`Coding-2-Python-for-Data-Analysis` folder, run:

```bash
git pull --ff-only
```

This gets the latest `ceu-ai.py` and `harness.md`, including support for homework
repositories. If Git reports a conflict with local changes, keep your work and ask for
help rather than discarding it.

### 2. Fork this homework and clone your fork

Click **Fork** on [this repository's GitHub page](https://github.com/ulrichwohak/coding2-debug-14-categorical-variables-interactions).
On your fork's page, copy the clone URL from **Code**. The URL must contain **your GitHub
username**, not `ulrichwohak`.

Clone your fork **inside your local course folder**. You can keep the repository's name
or put it in an ordinary subfolder such as `Homework 3/`; spaces and deeper nesting are
fine. Do not use hidden, private, environment, or raw-data folders. Clone the repository
as a separate folder; do not copy its files into the course root or add it as a submodule.

### 3. Set up the homework environment

In a terminal inside the cloned **homework repository**—the folder containing this
README and `analysis.ipynb`—run:

```bash
uv sync
```

Open `analysis.ipynb` in VS Code and select the **homework's `.venv` environment** as the
notebook kernel. Read the README, inspect the data and code, and try running the notebook
yourself **before asking the AI for help**.

### 4. Use CEU AI if helpful

Open another terminal in the **main course folder**, which contains `ceu-ai.py`, and run:

```bash
uv run python ceu-ai.py
```

Use your existing CEU setup; enter the class credentials supplied separately if prompted.
Tell the assistant the notebook's path relative to the course folder. For example, if
you kept the repository's original folder name:

```text
Help me understand the error in coding2-debug-14-categorical-variables-interactions/analysis.ipynb.
Inspect that homework's README, notebook, and local dataset. Explain the error before
suggesting changes.
```

Replace the path with your actual location if you used another folder name. The app
keeps nested homework repositories separate from the parent course repository in Git;
you still commit and push from the homework folder.

Check every proposed repair yourself. The assistant does not execute the notebook.
To discuss actual results, run the notebook, **save it with its outputs**, and ask the
assistant to interpret the saved text output. Do not put credentials in a prompt or notebook.

### 5. Check and submit your work

Complete Questions 1–3 in the notebook's answer cells and its submission checklist.
Restart the kernel, run all cells from top to bottom, and save the notebook with its outputs.

From the **homework repository's folder**, check that `origin` points to your own fork:

```bash
git remote -v
git status
```

Then commit and push your work:

```bash
git add analysis.ipynb
git commit -m "Complete homework 3"
git push origin main
```

If you intentionally changed other assignment files, stage those files too before
committing. Do not include credentials, `.venv`, or files from the parent course folder.

Open **your fork on GitHub** and check that the latest commit and your completed notebook
are visible. Your submission is the work pushed to your fork by **Wednesday, 25 November
2026**. Stay on the existing `main` branch: you do **not** need a new branch or a pull
request, and you should not push homework answers to the main course repository.

## Data and attribution

The dataset is included: students do **not** need to download data or rerun the course
fetch script. `education` measures years directly; no centering or recoding is required.
`female` is constructed in the notebook from the source's recorded `gender` categories.

The CPS was located through [Todd Jones's dataset catalogue](https://github.com/toddrjones/datasets).
This assignment uses the documented `CPS1985` teaching sample from **AER**, via **Rdatasets**.
Wages are historical US dollars per hour. The models describe this sample; the file has no
survey weights. See [data/README.md](data/README.md) for the fixed source, units, and attribution.
