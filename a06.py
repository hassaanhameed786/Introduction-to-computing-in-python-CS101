## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(recluze):
    recluze = round(recluze)
    recluze = int(recluze)
    
    list = []

    for h in range(1, recluze + 1):

    	if recluze % h == 0:
    		list.append(h)

    	else:
    		None

    for h in list:
    		if is_prime(h):
    			print h

def is_prime(recluze):  
    
    if type(recluze) == float:
        return None
    
    if recluze < 2:
        return False
    
    for h in range(2, recluze):
        if recluze % h==0:
            return False
            break
    else:
        return True


#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###

def get_nth_prime(recluze):   
    
    if type(recluze) == float:
    	return None

    nth_term = 0
    for i in range(1, 100000):
    	if is_prime(i):
    		nth_term = nth_term + 1

    	if nth_term == recluze:
    		return i
    		break
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(230)
    print get_nth_prime(4)
