from flask import Flask, render_template, request

# Your existing prediction function and model code
# ...

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_budget = float(request.form['budget'])
        prediction_result = predict_colleges(user_budget, model, scaler)
        return render_template('result.html', result=prediction_result)
    except ValueError:
        return "Invalid input. Please enter a valid budget."

if __name__ == '_main_':
    app.run(debug=True)