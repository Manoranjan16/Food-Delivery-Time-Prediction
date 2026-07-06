# 🍔 Food Delivery Time Prediction

## 📌 Project Overview

This project predicts the estimated food delivery time using Machine Learning based on delivery-related factors such as distance, weather, traffic, preparation time, vehicle type, and courier experience.

The project is built using Scikit-learn Pipeline and deployed with Streamlit.

---

## 🚀 Features

- Predicts food delivery time in minutes
- Uses a Scikit-learn Pipeline
- Automatic preprocessing with ColumnTransformer
- OneHotEncoder for categorical features
- Interactive Streamlit web application

---

## 📊 Dataset

Features used:

- Distance_km
- Weather
- Traffic_Level
- Time_of_Day
- Vehicle_Type
- Preparation_Time_min
- Courier_Experience_yrs

Target:

- Delivery_Time_min

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Workflow

1. Data Cleaning
2. Missing Value Handling
3. Feature Selection
4. Train-Test Split
5. ColumnTransformer
6. OneHotEncoder
7. Pipeline
8. Model Training
9. Model Evaluation
10. Cross Validation
11. Model Deployment using Streamlit

---

## 📈 Model Performance

| Metric | Score |
|---------|--------|
| R² Score | 0.8263 |
| MAE | 5.90 |
| RMSE | 8.82 |
| Cross Validation R² | 0.7685 |

---

## 📂 Project Structure

```
Food Delivery Time Prediction/
│
├── app.py
├── notebook.ipynb
├── pipeline.pkl
├── requirements.txt
├── README.md
├── Food_Delivery.csv
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone <your-github-repository-link>
```

Move into the project folder

```bash
cd Food-Delivery-Time-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

(Add screenshots of your Streamlit application here.)

---

## 👨‍💻 Author

**Manoranjan Behera**
