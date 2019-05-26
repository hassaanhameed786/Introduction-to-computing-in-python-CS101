## IMPORTS GO HERE

## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(H, file, recluze=""):
	count = 0
	with open(file, "r") as f:
		for line in f:
				count += 1
		count = count + 1
		return count
    
#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(H, recluze, new=""):
    count = 0
    with open(recluze, "r") as N:
        count = 0
        for line in N:
            	for i in line:
                	count += 1
        	return count            
            
#### End OF MARKER


### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###

#### End OF MARKER



if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
