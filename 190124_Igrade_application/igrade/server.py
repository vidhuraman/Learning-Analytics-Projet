from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect
from Model_classification import predictFunction, validation_data
from Convertor import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

studentInfo = ["sex","age","travelTime","studyTime"]

# Route for handling the login page logic
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/questionForm', methods=['GET', 'POST'])
def dataForm():
    error = None
    sex = ['sex', 'M', 'F']
    age = ['select your age',15, 16, 17, 18, 19, 20, 21]
    travelTime = ['level your travel time', 1, 2, 3, 4, 5]
    studyTime = ['level your study time', 1, 2, 3, 4, 5]
    # failures = ['how many failures', 0, 1, 2]
    # pre_result = predictFunction(validation_data)

    if request.method == 'POST':
        if request.form['sex'] == 'sex' or request.form['age'] == 'select your age'\
                or request.form['travelTime'] == 'level your travel time'\
                or request.form['studyTime'] == 'level your study time':
            error = 'select all field.'
        else:
            studentInfo[0] = sex_con(request.form['sex'])
            studentInfo[1] = age_con(request.form['age'])
            studentInfo[2] = travelTime_con(request.form['travelTime'])
            studentInfo[3] = studyTime_con(request.form['studyTime'])
            return redirect(url_for('prediction'))
    return render_template('question_form.html', error=error,sex=sex, age=age,travelTime=travelTime, studyTime=studyTime)

@app.route('/prediction')
def prediction():
    student = studentInfo
    pred_result = predictFunction(validation_data)
    return render_template('prediction.html', student=student,pred_result=pred_result)

if __name__ == "__main__":
    app.run()