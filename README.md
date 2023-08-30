# Movie Recommendation System using Machine Learning

Welcome to the Movie Recommendation System project! This project aims to provide users with personalized movie recommendations based on their selected movies using machine learning techniques. The system utilizes the TMDB 5000 Movie Dataset from Kaggle for training and employs various features like movie tags, overview, production companies, crew, and cast to make accurate recommendations. The recommendations are presented through a user-friendly web interface created using the Streamlit Python library. Additionally, the TMDB API is integrated to fetch movie posters corresponding to the recommended movies.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Model](#machine-learning-model)
- [Deployment](#deployment)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Movie Recommendation System is designed to help users discover new movies based on their preferences. By analyzing the user's selected movies, the system suggests the top 5 movies that are most likely to align with their taste.

## Dataset

We use the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) from Kaggle, which contains information about movies including their titles, overviews, production companies, crew, and cast.

## Feature Engineering

To create meaningful features for the machine learning model, we employ a combination of movie tags, overviews, production companies, crew, and cast. These features are transformed into numerical representations using the CountVectorizer from the scikit-learn library.

## Machine Learning Model

We calculate the cosine similarity between the feature vectors of movies to quantify their similarity. This similarity metric allows us to recommend movies that are closely related to the user's selected movies.

## Deployment

The recommendation system is deployed using the Streamlit Python library, providing an interactive web interface for users to input their movie preferences and receive recommendations. The user interface is intuitive and easy to navigate.

[Click here to view web page ](https://movierecomender.streamlit.app/)

## Getting Started

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/your-username/movie-recommendation.git
   ```

2. Navigate to the project directory.
   ```
   cd movie-recommendation
   ```

3. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app.
   ```
   streamlit run app.py
   ```

2. Access the web interface by opening the provided URL in your web browser.

3. Select your favorite movies from the list.

4. Click on the "Get Recommendations" button to receive your top 5 movie recommendations.

## Dependencies

The following dependencies are used in this project:

- scikit-learn
- pandas
- numpy
- streamlit
- requests

You can install them using the provided `requirements.txt` file.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request in this repository.

---

We hope you enjoy using our Movie Recommendation System! If you have any questions or feedback, please don't hesitate to contact us. Happy movie watching! 🍿🎬
