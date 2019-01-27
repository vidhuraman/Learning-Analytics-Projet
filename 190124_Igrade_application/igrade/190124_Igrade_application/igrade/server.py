import numpy as np
from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect
from Model_classification import predictFunction, validation_data
from Convertor import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

studentInfo = ["sex","age","travelTime","studyTime","failures","schoolsup","famsup","paid","activities",
               "higher","internet","famrel","freetime","goout","health","absences"]

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
    failures = ['No of Failures',1, 2, 3, 4, 5]
    schoolsup = ['Is SchoolsUp','yes','no']
    famsup = ['Is FamsUp','yes','no']
    paid = ['Is Paid','yes','no']
    activities = ['Is Active','yes','no']
    higher = ['Is Higher','yes','no']
    internet = ['Internet','yes','no']
    famrel = ['Level of famrel',1, 2, 3, 4, 5]
    freetime = ['Quantity of freetime',1, 2, 3, 4, 5]
    goout = ['Go out',1, 2, 3, 4, 5]
    health = ['Health Level',1, 2, 3, 4, 5]
    absences = ['Absences',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,24,26,30,32]

    # failures = ['how many failures', 0, 1, 2]
    # pre_result = predictFunction(validation_data)

    if request.method == 'POST':
        if request.form['sex'] == 'sex' or request.form['age'] == 'select your age'\
                or request.form['travelTime'] == 'level your travel time'\
                or request.form['studyTime'] == 'level your study time' \
                or request.form['failures'] == 'No of Failures'\
                or request.form['schoolsup'] == 'Is SchoolsUp'\
                or request.form['famsup'] == 'Is FamsUp'\
                or request.form['paid'] == 'Is Paid'\
                or request.form['activities'] == 'Is Active'\
                or request.form['higher'] == 'Is Higher'\
                or request.form['internet'] == 'Internet'\
                or request.form['famrel'] == 'Level of famrel'\
                or request.form['freetime'] == 'Quantity of freetime'\
                or request.form['goout'] == 'Go out'\
                or request.form['health'] == 'Health Level'\
                or request.form['absences'] == 'Absences':
                error = 'select all field.'
        else:
            studentInfo[0] = convertor(request.form['sex'])
            studentInfo[1] = convertor(request.form['age'])
            studentInfo[2] = convertor(request.form['travelTime'])
            studentInfo[3] = convertor(request.form['studyTime'])
            studentInfo[4] = convertor(request.form['failures'])
            studentInfo[5] = convertor(request.form['schoolsup'])
            studentInfo[6] = convertor(request.form['famsup'])
            studentInfo[7] = convertor(request.form['paid'])
            studentInfo[8] = convertor(request.form['activities'])
            studentInfo[9] = convertor(request.form['higher'])
            studentInfo[10] = convertor(request.form['internet'])
            studentInfo[11] = convertor(request.form['famrel'])
            studentInfo[12] = convertor(request.form['freetime'])
            studentInfo[13] = convertor(request.form['goout'])
            studentInfo[14] = convertor(request.form['health'])
            studentInfo[15] = convertor(request.form['absences'])
            return redirect(url_for('prediction'))
    return render_template('question_form.html', error=error,sex=sex, age=age,travelTime=travelTime, studyTime=studyTime,
    failures=failures,schoolsup=schoolsup,famsup=famsup,paid=paid,activities=activities,higher=higher,
    internet=internet,famrel=famrel,freetime=freetime,goout=goout,health=health,absences=absences)

@app.route('/prediction')
def prediction():
    student = np.array(studentInfo)
    studentTwoDArray = np.reshape(student, (-1, 16))
    pred_result = predictFunction(studentTwoDArray)
    return render_template('prediction.html', student=student,pred_result=pred_result)

if __name__ == "__main__":
    app.run()