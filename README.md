# MedicineRecommendationSystem
A web-based Medicine Recommendation System that predicts diseases and provides recommendations for medications, diets, workouts, and precautions based on user inputs. This app is built using Flask and deployed on Render.

## Table of Contents
- [Features](##features)
- [Datasets](##datasets)
- [Installation](##installation)
- [Usage](##usage)
- [Deployment](##deployment)

## Features
- **Predict Disease**: Allows users to input symptoms, then predicts possible diseases.
- **Medication Recommendations**: Suggests relevant medications based on the predicted disease.
- **Diet Recommendations**: Provides diet plans associated with the predicted condition.
- **Workout Recommendations**: Offers workout suggestions based on health conditions.
- **Precautions**: Lists necessary precautions related to the predicted disease.
The app features separate buttons for each of these functions, allowing users to click and get the specific information they need.

## Datasets
-The datasets (in CSV format) are hosted as part of the app, with Flask and Render serving the files directly through URL links.
  - Github link - https://github.com/Lakshman895/Medicine-Recommendation-System/tree/main/data
  - App link - https://datasetsurl.onrender.com/
## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Lakshman895/Medicine-Recommendation-System
   ```
2. Navigate to the project directory:
    ```bash
       cd Medicine-Recommendation-System
   ```
3. Install the required packages:
    ```bash
       pip install -r requirements.txt
   ```

## Usage
To run the application locally, execute the following command:
 ```bash
       python app.py
   ```
Once the application is running, open your web browser and navigate to http://127.0.0.1:5000 to access.

## Deployement
The application is deployed on Render. You can access it at: https://medicinerecommendationsystem.onrender.com/
