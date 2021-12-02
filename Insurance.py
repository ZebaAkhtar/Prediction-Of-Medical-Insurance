from flask import Flask, request, url_for, redirect, render_template
import pickle

import numpy as np

app = Flask(__name__)

model = pickle.load(open('project.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    features = [float(x) for x in request.form.values()]

    print(features)
    print("hello")
    final = np.array(features).reshape((1,6))
    print(final)
    print("hooooo")
    pred = model.predict(final)[0]
    print(pred)
    print("byeeee")

    
    if pred < 0:
        return render_template('index.html', pred='Error calculating Amount!')
    else:
        return render_template('index.html', pred=' {0:.3f}'.format(pred))

if __name__ == "__main__":
    app.run(debug=True)
