from flask import Flask, render_template, request

# Your existing prediction function and model code
# ...

app = Flask(_name_)

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

if _name_ == '_main_':
    app.run(debug=True)