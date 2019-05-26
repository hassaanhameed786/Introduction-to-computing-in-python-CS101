## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results): 

    if results == None:
        return None
    if results == []:
    	return []
    results_data = []
    for i in results:
        sum_of_assignment_marks = 0
        student_ID = i[0]
        name_of_student = i[1]
        for j in i[2:]:
            if j == None:
                j = 0
            sum_of_assignment_marks = sum_of_assignment_marks + j
        results_data.append((student_ID, name_of_student, sum_of_assignment_marks))

    return results_data


#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    results_data = find_cumulative_marks(results)
    a = []
    c = ()
    for i in results_data:
        a.append(i[2])
    b = max(a)
    for j in results_data:
        if b == (j[2]):
            c = (j[0:2])
    return c
#### End OF MARKER





if __name__ == '__main__':
    results = [
         ('p101111', 'Ali Khayam', 1),
            ('p101112', 'Mudasser Farooq', 1),
            ('p101113', 'Tamleek Ali', 1),
            ('p101114', 'Jawad Mansoor', 0)
    ]

   #print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
#