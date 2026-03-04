# Beijing-Consumption-Analysis-2015-2024
Empirical analysis of the evolution of consumption structure among Beijing urban and rural residents using Python.
2015-2024 Empirical Analysis of Beijing Urban and Rural Residents' Consumption Structure Evolution

This project employs Python to conduct in-depth analysis of Beijing's statistical data over the past decade,
multidimensionally illustrating the historical progression of consumption upgrades among residents of this megacity—shifting from subsistence-oriented to enjoyment-oriented spending.

Key Insights

1. Engel's Coefficient: Crossing the “Extremely Affluent” Threshold
Data Findings: Beijing's urban Engel's coefficient dropped to “19.87%” in 2024, breaking below the 20% threshold for the first time.
Empirical Supplement: Analysis of per capita physical consumption data reveals urban residents' grain consumption decreased from “88.5kg” in 2015 to “81.9kg” in 2024.
Conclusion: The decline in food expenditure share, accompanied by reduced staple intake and optimized dietary structure, signifies residents' entry into an extremely affluent stage of living.

2. Service Consumption: Urban-Rural Convergence and Rural Momentum
Key Inflection Point: In 2017, rural service consumption surpassed urban for the first time.
Driving Factors: Benefiting from widespread rural communication infrastructure and expanded medical insurance coverage. By 2024, rural service consumption reached 29.41%, on par with urban levels.

 3. Consumption Resilience: Structural Adjustment Amid Major Shocks
2020 Observations: External factors caused a sharp decline in discretionary spending (entertainment, apparel), while healthcare and housing expenditures demonstrated remarkable resilience.

---

Technical Implementation (Tech Stack)
Language: Python 3.10+
Libraries: Pandas (data cleaning), Matplotlib (professional visualization), Numpy (matrix operations)
Cleaning Strategy: Utilized regular expressions and slicing techniques to resolve special characters (e.g., missing numeric digits) and transposition alignment issues in the original Excel files.

Directory Description
 `/data`: Contains raw urban, rural, and physical consumption volume datasets.
 `/scripts`: Core computational logic and plotting code.
 `/images`: Includes Engel trend charts, radar charts, stacked charts, and service share diagrams.

Challenges and Retrospective
Dimension Mismatch: Resolved Matplotlib's (9,) vs. (11,) dimension error during radar chart generation using a circular closing algorithm.
Data Alignment: Ensured strict alignment of urban/rural indicators across years through multi-table joins, maintaining analytical rigor.
Exception Handling & Robustness: Implemented try-except blocks for auxiliary data (e.g., physical consumption CSV). This ensures the core visualization pipeline remains uninterrupted even if secondary data sources are missing or encoded incorrectly, demonstrating production-level code robustness.
