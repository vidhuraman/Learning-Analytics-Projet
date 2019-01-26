def sex_con(user_input_raw):
    con = 1
    if user_input_raw == 'M':
        con = 0
    else:con=1
    return con

def age_con(user_input_raw):
    con = 1
    if user_input_raw == 15:
        con = 0
    elif user_input_raw == 16:
        con = 1
    elif user_input_raw == 17:
        con = 2
    elif user_input_raw == 18:
        con = 3
    elif user_input_raw == 19:
        con = 4
    elif user_input_raw == 20:
        con = 5
    elif user_input_raw == 21:
        con = 6
    return con

def travelTime_con(user_input_raw):
    con = 1
    if user_input_raw == 1:
        con = 1
    elif user_input_raw == 2:
        con = 2
    elif user_input_raw == 3:
        con = 3
    elif user_input_raw == 4:
        con = 4
    elif user_input_raw == 5:
        con = 5
    return con

def studyTime_con(user_input_raw):
    con = 1
    if user_input_raw == 1:
        con = 1
    elif user_input_raw == 2:
        con = 2
    elif user_input_raw == 3:
        con = 3
    elif user_input_raw == 4:
        con = 4
    elif user_input_raw == 5:
        con = 5
    return con