Task_04_Descriptive_Stats

This repository contains three approaches to perform descriptive statistics and grouping operations on datasets related to the 2024 US Presidential Elections. The task was to explore the data using:
	1.	Pure Python (no third-party libraries)
	2.	Pandas
	3.	Polars

⸻

📂 Dataset

Download the dataset used for this project from the following link:
	•	Facebook Ads, Facebook Posts, and Twitter Posts Dataset

Note: Do not commit the dataset to the repository. Place the .csv files in the project root before running the scripts.

⸻

🧑‍💻 Author

Bhaarat Kotak
M.S. in Information Systems
Syracuse University

⸻

🚀 Instructions to Run

1. Clone the Repository

git clone https://github.com/yourusername/Task_04_Descriptive_Stats.git
cd Task_04_Descriptive_Stats

2. Place the Dataset

Place the downloaded .csv files (e.g., 2024_fb_ads_president_scored_anon.csv, 2024_fb_posts_president_scored_anon.csv, 2024_tw_posts_president_scored_anon.csv) in the root directory of this repo.

3. Run the Pure Python Script

python RA_pure_python_BK.py 2024_fb_ads_president_scored_anon.csv "Page Id" "Ad Id"

	•	You can replace the dataset name and grouping columns as needed.

4. Run the Pandas and Polars Notebooks

Open the following files in Jupyter:
	•	RA_pandas_BK.ipynb
	•	RA_polar_BK.ipynb

Run all cells. You may need to update the file path inside the notebook if your dataset is placed elsewhere.

⸻

📊 Key Takeaways
	•	Polars:
	•	Extremely fast and memory-efficient for large datasets.
	•	Group-by and descriptive stats were concise and performant.
	•	A bit less intuitive syntax for new users.
	•	Pandas:
	•	Most user-friendly and rich in functionality.
	•	Flexible and highly compatible with visualization tools.
	•	Slower on large-scale computations compared to Polars.
	•	Pure Python:
	•	Best for learning internals of statistics calculations.
	•	No external dependencies.
	•	Verbose and slower, especially with large datasets.

All three approaches were used to compute:
	•	Count, Mean, Min, Max, Std Dev (for numeric columns)
	•	Unique values and most frequent values (for categorical columns)
	•	Grouped analysis by one and multiple columns

⸻

🧪 Bonus
	•	Grouped stats on Facebook Ads by Page Id and Ad Id
	•	Mode and n-unique values per column
	•	Insights on performance and API usability

⸻

📌 Requirements
	•	Python 3.8+
	•	Jupyter
	•	pandas
	•	polars

Install dependencies with:

pip install pandas polars jupyter


⸻

📨 Contact

For queries or collaborations, please reach out to Bhaarat Kotak.

⸻
