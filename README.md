# Music Genre Recommender Website

## Overview

This project is a web application that uses a machine learning model to predict the genre of music based on user inputs. The model is built using a Decision Tree Classifier and is integrated into a Flask web application. Users can input their age and gender to receive a music genre recommendation.

## Features

- Predicts music genre based on user inputs (age and gender)
- Simple and intuitive web interface
- Built using Flask for the backend and HTML/CSS/JavaScript for the frontend

## Requirements

- Python 3.7 or later
- Flask
- joblib
- scikit-learn
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/music-genre-recommender-website.git
    ```

2. Navigate to the project directory:

    ```bash
    cd music-genre-recommender-website
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

4. Install the required packages:

    ```bash
    pip install flask joblib scikit-learn pandas
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter your age and gender in the form to get a music genre recommendation.

## Model

The model used in this application is a Decision Tree Classifier trained on a dataset of music genres. The model is saved in a file named `music-recommender.joblib`.

## File Structure
/Music-genre-recommender-website
│
├── app.py
├── music-recommender.joblib  # Your saved model file
└── static
    └── index.html  # Your frontend file

