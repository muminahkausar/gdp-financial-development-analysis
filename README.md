# GDP per capita and domestic credit: an econometrics case study

**Focus:** Financial development, cross-country comparisons and interpreting OLS results.  
**Status:** Results interpretation and visualisation; **not** an independently reproduced regression.

## Research question
Is GDP per capita associated with domestic credit across a sample of 40 countries, and how does accounting for income-group differences change the estimated relationship?

## Background
This portfolio case study adapts my university econometrics coursework. It presents two regression result tables and explains what can and cannot be concluded from them. The original underlying 40-country dataset and estimation output are not included, so this repository **does not claim to reproduce the regressions**.

## Methods and reported results
The coursework considered domestic credit (DC) as the dependent variable and GDP per capita (GDPC) as an explanatory variable.

| Statistic | Model 1: GDPC | Model 2: GDPC + HighGDPC |
|---|---:|---:|
| GDPC coefficient | 0.000967 | 0.000386 |
| GDPC p-value | 0.0047 | 0.411 |
| HighGDPC coefficient | — | 40.96 |
| HighGDPC p-value | — | 0.097 |
| Adjusted R² | 0.171 | 0.211 |

`HighGDPC` is a binary indicator for countries with GDP per capita above the sample median. These values were transcribed from the original report; the accompanying Python script **plots reported statistics** and does not estimate OLS.

## Findings
- In Model 1, GDP per capita had a positive association with domestic credit, statistically significant at the 1% level (p = 0.0047).
- After including an income-group indicator, the GDPC coefficient was smaller and not statistically significant at the 5% level (p = 0.411).
- Adjusted R² increased from 0.171 to 0.211. This is a modest improvement in in-sample fit, not evidence of causality.

## Limitations
- Cross-sectional associations do not establish that GDP per capita *causes* greater credit provision.
- Omitted factors and reverse causality may affect the estimates.
- The original report discusses diagnostic tests, but the underlying test output is not supplied here and has not been independently verified.
- Raw observations, sample definitions and the exact credit measure are not available in this repository. A full replication would require those details and the source data.

## Files
- `analysis/visualise_results.py` — Python script to visualise reported model fit and GDPC p-values.
- `figures/model_comparison.png` — generated figure.
- `requirements.txt` — Python dependency.

## Run locally
```bash
python -m pip install -r requirements.txt
python analysis/visualise_results.py
```

## Next steps
Find the original 40-country dataset, document the source and variables, rerun the regressions in EViews or Python, and upload reproducible code and diagnostic output. This is the next stage rather than a claim about the current project.
