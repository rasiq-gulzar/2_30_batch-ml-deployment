#first create the virutual environment  command is = python -m venv name_of_virtutal_environment
#activate the virtual environment= see the root folder of venv to activate the scripts....
#make app.py
#install the required packages
from flask import Flask, render_template, request
import numpy as np
import pickle
#this is the entry point of the application it will gonna run from here and we are simplay passing constructor of the 
#Flask class to the app variable
app= Flask(__name__)  

#now it is time to make the route of the app or we can say the endpoing of the app
@app.route('/',methods=['GET', 'POST'])
#we will make a function that will check whether the app is working or not
def home():
    if request.method == 'POST':
        hs= int(request.form.get('house_size'))
        with open('house_price_model.pkl', 'rb') as f:
            model=pickle.load(f)
        result=model.predict(np.array([[hs]]))
        return render_template('index.html',prediction=result[0])
    else:
        return render_template('index.html', result=None)
        
#now we will check whether the app constructor is working or not
if __name__ == '__main__':
    app.run(debug=True)