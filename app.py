from flask import Flask, render_template, request
import pickle
import sklearn
app = Flask(__name__)

with open('transformer.pkl', 'rb') as f:
    transformer = pickle.load(f)
with open('model1.pkl', 'rb') as f1:
    model1 = pickle.load(f1)
with open('model2.pkl', 'rb') as f2:
    model2 = pickle.load(f2)


@app.route('/', methods = ['get', 'post'])
def main_page():
    message = ''
    if request.method == 'POST':
        try:
            IW = request.form.get('IW')
            IF = request.form.get('IF')
            VW = request.form.get('VW')
            FP = request.form.get('FP')

            parameters = [[int(IW), int(IF), float(VW), int(FP)]]
        except ValueError:
            message = 'Введены некорректные данные!'

        else:
            parameters_tr = transformer.transform(parameters)

            message = f'Ширина сварного шва: {model1.predict(parameters_tr)[0]}, \n ' \
                      f' Глубина сварного шва: {model2.predict(parameters_tr)[0]}'


    return render_template("index.html", message=message)


app.run()