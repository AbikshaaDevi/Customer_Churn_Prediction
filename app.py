from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained models and encoders
rf_model = pickle.load(open("rf_model.pkl", "rb"))
lr_model = pickle.load(open("lr_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_maps = pickle.load(open("label_maps.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        form = request.form
        input_dict = {
            'tenure': float(form['tenure']),
            'MonthlyCharges': float(form['MonthlyCharges']),
            'Contract': label_maps['Contract'][form['Contract']],
            'InternetService': label_maps['InternetService'][form['InternetService']],
            'PaymentMethod': label_maps['PaymentMethod'][form['PaymentMethod']],
            'SeniorCitizen': int(form['SeniorCitizen'])
        }

        # Convert to DataFrame and scale
        df = pd.DataFrame([input_dict])
        scaled_input = scaler.transform(df)

        # Predict with both models
        rf_pred = rf_model.predict(scaled_input)[0]
        lr_pred = lr_model.predict(scaled_input)[0]

        # Combine predictions into a single final message
        if rf_pred == 1 or lr_pred == 1:
            final_result = "🔴 The customer is willing to leave."
        else:
            final_result = "🟢 The customer is willing to continue."

        return render_template('index.html', prediction=final_result)

    except Exception as e:
        return render_template('index.html', prediction=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
