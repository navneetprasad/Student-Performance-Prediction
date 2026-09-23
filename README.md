🎓 Student Performance Predictor

An interactive machine learning web application that predicts a student's final math grade based on their academic history, demographics, and lifestyle choices.

📝 Overview

This project uses the Student Performance dataset from the UCI Machine Learning Repository to forecast student grades (on a scale of 0 to 20). The application features a predictive model powered by a Random Forest Regressor and a user-friendly frontend built with Streamlit.

It takes 30 unique features into account, including:

Past class failures and weekly study time

Social habits (going out with friends, free time)

Health status and number of absences

Family education and background demographics

🛠️ Tech Stack

Language: Python

Data Processing: Pandas, NumPy

Machine Learning: Scikit-learn (Random Forest)

Web Framework: Streamlit

Model Serialization: Joblib

📂 Project Structure

setup.py - The script used to clean the raw data, train the Random Forest model, and export it.

app.py - The main Streamlit web application script that creates the user interface and handles predictions.

student-mat.csv - The original dataset containing student records.

student_model.pkl - The saved (serialized) machine learning model used by the web app.

requirements.txt - The list of Python libraries needed to run the app.

🚀 How to Run Locally

If you want to run this application on your own machine, follow these steps:

1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Install the required dependencies
Make sure you have Python installed, then run:

pip install -r requirements.txt


(Note: Create a requirements.txt file containing streamlit, pandas, scikit-learn, and joblib)

3. Run the Streamlit app

streamlit run app.py


The application will automatically open in your default web browser at http://localhost:8501.
