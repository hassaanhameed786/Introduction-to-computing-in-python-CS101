## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(recluze):
	if type(recluze) == float:
		recluze = int(recluze)
	if recluze < 2:
		return False
	else:
		for h in range(2, recluze):
			if recluze % h == 0:
				return False
			else:
				return True

#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(recluze):

	for h in range(1, recluze):

		a = recluze % h
		if a == 0:
			print (h)
		else:
			None
		h = h + 1

		if h == recluze:
			print(recluze)
			break

		else:
			None

#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def prime_for_largest(recluze):

	if recluze == 0 or recluze == 2 or recluze == 3 or recluze == 5 or recluze == 7:
		return recluze 

	if recluze % recluze == 0 and recluze % 2 != 0 and recluze % 3 != 0 and recluze % 5 != 0:
    	    return recluze
	else:
		return False

def get_largest_prime(recluze):

	if recluze < 2:
	    return None

	if type(recluze) == float:
	    recluze = int(recluze)

	recluze = []

	if prime_for_largest(recluze):
	    prime.append(recluze)

	for h in range(1, recluze):
	    
	    if prime_for_largest(h):
	 	    prime.append(h)
	return max(recluze)

#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
