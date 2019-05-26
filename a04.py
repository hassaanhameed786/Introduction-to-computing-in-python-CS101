## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(Score):
    Score = int(Score)
    if Score >= 90:
        return 'A+'
    if Score >= 86:
        return 'A'
    if Score >= 82:
        return 'A-'
    if Score >= 78:
        return 'B+'
    if Score >= 74:
        return 'B'
    if Score >= 70:
        return 'B-'
    if Score >= 66:
        return 'C+'
    if Score >= 62:
        return 'C'
    if Score >= 58:
        return 'C-'
    if Score >= 54:
        return 'D+'
    if Score >= 50:
        return 'D'
    if Score >= 0:
        return 'F'

#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def grading_scale(G):
    if G == 'A+':
        return 4.00
    if G == 'A':
        return 4.00
    if G == 'A-':
        return 3.67
    if G == 'B+':
        return 3.33
    if G == 'B':
        return 3.00
    if G == 'B-':
        return 2.67
    if G == 'C+':
        return 2.33
    if G == 'D+':
        return 1.33
    if G == 'D':
        return 1.00
    if G == 'F':
        return 0.00
def calculate_sgpa(ITC, Calculus, BasicElectronics):
    SGPA = 0.00
    sum_of_number_of_subjects = 0
    if  ITC != "nothing":
        sum_of_number_of_subjects = sum_of_number_of_subjects + 1
        SGPA = SGPA + grading_scale(ITC)

    if  Calculus != "nothing":
        sum_of_number_of_subjects = sum_of_number_of_subjects + 1
        SGPA = SGPA + grading_scale(Calculus)

    if BasicElectronics != "nothing":
        sum_of_number_of_subjects = sum_of_number_of_subjects + 1
        SGPA = SGPA + grading_scale(BasicElectronics)

    if sum_of_number_of_subjects == 0:
        return 0
    else:
        SGPA = SGPA / sum_of_number_of_subjects
        SGPA = round(SGPA)
        return SGPA
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A-', 'A-', 'nothing')
