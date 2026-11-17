# 1985 CPS wage sample

`cps1985.csv` contains 534 workers from a teaching sample of the **May 1985 US
Current Population Survey**. The **AER** package documents the sample as drawn
for Berndt (1991), *The Practice of Econometrics*, and credits StatLib as its source.
The [AER documentation](https://cran.r-project.org/web/packages/AER/refman/AER.html#CPS1985)
describes the data and variables. The survey was located through
[Todd Jones's dataset catalogue](https://github.com/toddrjones/datasets#household-surveys).

## File and variables

The supplied file is an unchanged copy of the
[Rdatasets CSV](https://github.com/vincentarelbundock/Rdatasets/blob/cc03c29690889dbe83089f5206e2422db8c3f71f/csv/AER/CPS1985.csv).
It retains all 534 observations and all source columns. There are 289 records
labelled `male` and 245 labelled `female`, no missing values, and no exact duplicate
records after excluding the source row label. No observations were trimmed or imputed.

| Column used | Meaning |
| --- | --- |
| `wage` | Hourly wage in US dollars in 1985; not already logged. |
| `education` | Years of education, used directly as a numeric predictor. |
| `experience` | Years of potential work experience, derived from age and schooling; not observed years in employment. |
| `gender` | Source categories `male` and `female`. |
| `rownames` | Original R row label, retained for tracing observations; not a predictor. |

The notebook creates `female` as 1 for `female` and 0 for `male`, and creates
`log_wage` using the natural logarithm. All 534 observations enter every model.
The other columns are retained for provenance but are not predictors in this assignment.

The source describes potential experience as age minus education minus six.
In this file it equals that quantity bounded below at zero. Values are kept as supplied.
The regressions are unweighted descriptions of this historical sample; the file contains
no survey weights. The recorded male/female field does not describe other gender identities.

## Reproducibility and attribution

- Source revision: `cc03c29690889dbe83089f5206e2422db8c3f71f` in `vincentarelbundock/Rdatasets`.
- SHA-256: `1b4bf681b94ecb82e534a0f97773c704205e13ccf13d273e439e44eaa9f5435c`.
- Source chain: US Census Bureau CPS → Berndt (1991)/StatLib → AER → Rdatasets.
- The source observations have not been relicensed under this repository's MIT licence.
  See [NOTICE.md](../NOTICE.md) for upstream attribution and licensing references.

Students use the included CSV; no download is required. Maintainers can verify or
restore this exact file with `uv run python scripts/fetch_data.py` from the homework root.
The script checks the hash and refuses to overwrite a changed local dataset.
