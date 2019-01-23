from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

studentInfo = ["sex",1]

# Route for handling the login page logic
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/questionForm', methods=['GET', 'POST'])
def dataForm():
    error = None
    sex = ['sex', 'M', 'F']
    age = ['select your age', 16, 17, 18, 19, 20, 21, 22]

    if request.method == 'POST':
        if request.form['sex'] == 'sex' or request.form['age'] == 'select your age':
            error = 'select all field.'
        else:
            studentInfo[0] = request.form['sex']
            studentInfo[1] = request.form['age']
            return redirect(url_for('prediction'))
    return render_template('question_form.html', error=error,sex=sex, age=age)

@app.route('/prediction')
def prediction():
    student = studentInfo
    return render_template('prediction.html', student=student)

if __name__ == "__main__":
    app.run()