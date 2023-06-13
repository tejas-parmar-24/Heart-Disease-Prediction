import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('temp.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    # Put all form entries values in a list 
    features = [i for i in request.form.values()]
    features[0]=int(features[0])
    features[3]=int(features[3])
    features[4]=int(features[4])
    features[5]=int(features[5])
    features[7]=int(features[7])
    features[9]=float(features[9])
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('temp.html', 
                               result = 'The patient is likely to have heart disease!')
    else:
        return render_template('temp.html', 
                               result = 'The patient is not likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()