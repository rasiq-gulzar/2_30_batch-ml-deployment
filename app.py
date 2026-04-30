from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('multiple_lr.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sq = float(request.form['sqfts'])
        r = float(request.form['rooms'])
        prediction = model.predict(np.array([[sq,r]]))
        return render_template('index.html', result=prediction[0])
    return render_template('index.html')

if __name__ == '__main__':
    # 4. FIXED: Use app.run, not app.start
    app.run(debug=True)
