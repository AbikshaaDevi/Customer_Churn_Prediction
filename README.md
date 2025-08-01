
# Customer Churn Prediction 🚨

A Flask-based web application that predicts whether a telecom customer is likely to churn or continue using the service. It uses machine learning models trained on the Telco Customer Churn dataset.

---

## 📌 Project Overview

Customer churn is one of the major challenges in the telecom industry. This application helps predict whether a customer is at risk of leaving, allowing the business to take action in advance.

Users can input basic customer information (like contract type, internet service, payment method, etc.) and get a prediction:  
✅ *The customer is willing to continue*  
❌ *The customer is about to leave*

---

## 🔍 Features

- User-friendly web interface (HTML + CSS)
- Prediction using combined results from:
  - ✅ Random Forest Classifier
  - ✅ Logistic Regression
- Models trained on cleaned and preprocessed Telco churn data
- Scaled inputs using `StandardScaler`
- Custom result messages based on prediction

---

## 🧠 Models Used

- **Random Forest Classifier**
- **Logistic Regression**
- Final prediction is made by combining both results and returning a single message

---

## 🛠️ Technologies

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML/CSS (Jinja2 Templates)
- Git, GitHub

---

## 📁 Project Structure

```
Customer_Churn_Prediction/
│
├── app.py                     # Flask backend
├── templates/
│   └── index.html             # Frontend form
├── rf_model.pkl               # Random Forest model
├── lr_model.pkl               # Logistic Regression model
├── scaler.pkl                 # Feature scaler
├── label_maps.pkl             # Encoded mappings
├── Telco-Customer-Churn.csv   # Original dataset
├── requirements.txt           # Python dependencies
├── render.yaml                # Render deployment file
└── README.md                  # Project documentation
```

---

## 🚀 How to Run This Project Locally

1. **Clone the repository**

```bash
git clone https://github.com/AbikshaaDevi/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate      # for Windows
source venv/bin/activate   # for Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Visit the app in your browser**

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The app is ready for deployment using [Render](https://render.com). A `render.yaml` file is included to set it up easily.

---

## 🙋‍♀️ Author

**Abikshaa Devi Ashokkumar**  
[GitHub Profile](https://github.com/AbikshaaDevi)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📣 Contributions

Feel free to fork this repository and improve the project. Pull requests are welcome!
