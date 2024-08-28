
# Weather Prediction Machine Learning Project

## Overview

This project is a Flask web application that predicts weather conditions based on input features such as precipitation, maximum temperature, minimum temperature, and wind speed. The application allows users to select from four different machine learning models to make predictions.

## Features

- **Model Selection**: Choose between four machine learning models:
  - Logistic Regression (Accuracy: 0.83)
  - Decision Tree (Accuracy: 0.72)
  - Random Forest (Accuracy: 0.82)
  - Support Vector Machine (Accuracy: 0.83)
- **Input Features**:
  - Precipitation
  - Maximum Temperature
  - Minimum Temperature
  - Wind Speed
- **Prediction Output**: The application predicts one of the following weather conditions:
  - Drizzle Weather
  - Foggy Weather
  - Rainy Weather
  - SnowFall
  - Sunny Weather

## Project Structure

\`\`\` plaintext
weather-prediction /
│
├── app.py                  # Main application file
├── templates/
│   └── index.html          # HTML template for the web interface
├── models/
│   ├── model1.sav          # Pre-trained Logistic Regression model
│   ├── model2.sav          # Pre-trained Decision Tree model
│   ├── model3.sav          # Pre-trained Random Forest model
│   └── model4.sav          # Pre-trained Support Vector Machine model
└── README.md               # Project documentation
\`\`\`

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Pickle (for loading pre-trained models)

## Installation

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/yourusername/weather-prediction.git
   cd weather-prediction
   \`\`\`

2. Install the required Python packages:

   \`\`\`bash
   pip install flask
   \`\`\`

3. Place the pre-trained models (\`model1.sav\`, \`model2.sav\`, \`model3.sav\`, \`model4.sav\`) in the \`models/ \` directory.

## Usage

1. Start the Flask application:

   \`\`\` bash
    python app.py
   \`\`\`

2. Open your web browser and go to \` http://127.0.0.1:5000/ \`.

3. Enter the input features (precipitation, max temperature, min temperature, wind speed) and select a model from the dropdown.

4. Click "Predict" to see the weather prediction.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

- The machine learning models were pre-trained and saved using the Scikit-learn library.
- Flask is used to create the web application.
