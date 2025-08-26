# Movie Recommendation System

## Overview

This project is a **Movie Recommendation System** built using machine learning techniques. It suggests movies to users based on similarity measures calculated from the dataset features.

## Dataset

The dataset used in this project is **TMDB 5000 Movies Dataset**, which can be downloaded from Kaggle:
👉 [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Make sure to download the dataset and place the CSV files in the project directory before running the code.

## Features

* Content-based filtering using movie metadata
* Similarity calculation using vectorization and cosine similarity
* Movie search and recommendation functionality

## Requirements

Install the required dependencies before running the project:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/Md-Shahid-S/Movie-Recommendation.git
```

2. Navigate into the project folder:

```bash
cd Movie-Recommendation
```

3. Download the dataset from Kaggle and place it inside the project directory.
4. Run the notebook or Python script to generate recommendations.

## Project Structure

```
Movie-Recommendation/
│── data/                # Place dataset files here (movies.csv, credits.csv)
│── notebook.ipynb       # Jupyter Notebook for model building
│── src/app.py           # Python script for recommendations
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## Example Output

```
Input Movie: Avatar
Recommended Movies:
1. Guardians of the Galaxy
2. Star Wars: The Force Awakens
3. Star Trek
4. The Fifth Element
5. Interstellar
```

---

🚀 This is a learning project created to practice recommendation systems using machine learning.
