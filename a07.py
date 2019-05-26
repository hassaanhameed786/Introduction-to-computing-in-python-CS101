## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def grading_scale(grade):
    
    if grade == 'A+':
    	return 4.00
    if grade == 'A':
        return 4.00
    if grade == 'A-':
        return 3.67
    if grade == 'B+':
        return 3.33
    if grade == 'B':
        return 3.00
    if grade == 'B-':
        return 2.67
    if grade == 'C+':
        return 2.33
    if grade == 'C':
        return 2.00
    if grade == 'C-':
        return 1.67
    if grade == 'D+':
        return 1.33
    if grade == 'D':
        return  1.00
    if grade == 'F':
        return 0.00
    else:
    	return None


def calculate_sgpa(Grades):   
    subs = 0
    total_marks = 0.0
    
    if Grades == None:
    	return None
    if type(Grades) != list:
        Grades = [Grades]

    for i in Grades:
        if i == None:
            return None
        else:
            subs += 1
            if grading_scale(i) == None: return None
            total_marks += grading_scale(i)

    if subs == 0 or total_marks == 0:
    	return None
            
    sgpa = total_marks / subs
            
    return sgpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(Grades, Credit_hours):
	

    SGPA = type(float) 
    Recluze = 0.0
    Hours = 0

    if type(Grades) != list:
        Grades = [Grades]
    if type(Credit_hours) != list:
        Credit_hours = [Credit_hours]
    

	if len(Grades) != len(Credit_hours):
		return None
	else:
		for i in Grades:
			if i == None:
				return None
			else:
				for i in Credit_hours:
					if i == None:
						return None
					else:
						Recluze += grading_scale(i) * Credit_hours[i]
						Hours += Credit_hours[i]
        SGPA = Recluze / float(Hours)
        return SGPA


#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa([])
    print calculate_sgpa_weighted(['A+'], [4])
