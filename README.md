# Task_04_Descriptive_Stats
# Author - Bhaarat Kotak

## Objective
This repository is a submission for Research Task 04, which involves performing descriptive statistical analysis on real-world datasets using three different methods:
- Pure Python (no external libraries)
- Pandas
- Polars

The dataset used consists of Facebook Ads, Facebook Posts, and Twitter Posts related to the 2024 U.S. Presidential Elections.

## Datasets
**Note:** The datasets are not included in this repository to adhere to data privacy and size constraints. They must be downloaded separately from [this Google Drive link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing).

Datasets:
- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

## Scripts

### 1. `RA_pure_python_BK.py`
- Implements base Python logic using `csv`, `math`, and `collections`.
- Computes: Count, Mean, Min, Max, Std Dev, Unique Counts, Most Frequent Value.
- Supports grouping by one or more keys (e.g., Page Id, Ad Id).

### 2. `RA_pandas_BK.ipynb`
- Leverages `pandas` to compute the same statistics as in the Pure Python script.
- Additional summaries like `.describe()`, `.value_counts()`, and `.nunique()`.
- Grouped analysis by columns like `facebook_id`, `page_id`, and `post_id`.

### 3. `RA_polar_BK.ipynb`
- Uses the `polars` library for performance-oriented analysis.
- Computes count, mean, median, std dev, min, and max for numeric columns.
- Supports group-by analysis for one and multiple columns.
- Includes handling of missing values and calculation of column-wise mode.

## Instructions to Run

Make sure you have the required packages installed:

```bash
pip install pandas polars

---

### Key Takeaways

```markdown
##  Key Takeaways

- **Pandas**:
  - Offers a highly intuitive and mature API.
  - Great community support and excellent documentation.
  - Slower performance for large datasets compared to Polars.

- **Polars**:
  - Extremely fast due to Rust backend and lazy execution.
  - Syntax is more verbose than Pandas initially, but powerful once mastered.
  - Best suited for large-scale analytical workloads.

- **Pure Python**:
  - Offers transparency and control.
  - Not suitable for large-scale data due to lack of built-in optimizations.
  - Good for educational purposes or environments where dependencies are restricted.

- **Overall**:
  - For exploratory data analysis: Pandas is most beginner-friendly.
  - For performance and scalability: Polars is the ideal choice.
  - For absolute dependency-free environments or low-level control: Pure Python works, but requires more effort.
