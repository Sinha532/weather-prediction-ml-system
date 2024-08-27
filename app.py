from flask import Flask, render_template, request
import pickle

# Load models
model1 = pickle.load(open('./models/model1.sav', "rb"))
model2 = pickle.load(open('./models/model2.sav', "rb"))
model3 = pickle.load(open('./models/model3.sav', "rb"))
model4 = pickle.load(open('./models/model4.sav', "rb"))

models = {
    'Logistic Regression(0.83)': model1,
    'Decison Tree(0.72)': model2,
    'Random Forest(0.82)': model3,
    'Support Vector Machine(0.83)': model4
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_weather():
    prec = float(request.form.get('precipitation'))
    temp_max = float(request.form.get('temp_max'))
    temp_min = float(request.form.get('temp_min'))
    wind = float(request.form.get('wind'))
    selected_model_name = request.form.get('model')
    selected_model = models[selected_model_name]

    # Prepare the input features as a list of lists (2D array-like structure)
    input_features = [[prec, temp_max, temp_min, wind]]

    # Get the prediction from the selected model
    prediction = selected_model.predict(input_features)[0]
    if prediction==0:
        prediction="Drizzle Weather"
    elif prediction==1:
        prediction="Foggy Weather"
    elif prediction==2:
        prediction="Rainy Weather"
    elif prediction==3:
        prediction="SnowFall"
    elif prediction==4:
        prediction="Sunny Weather"

    return render_template('index.html', 
                           prediction=prediction, 
                           selected_model=selected_model_name)

if __name__ == "__main__":
    app.run(debug=True)
