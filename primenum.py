import time

# check if n is divisible by 2
# check if n / 2 has a remainder
# check if n is divisible by 3
# check if n / 3 has a remainder
def find_prime(n):
    '''
    It returns True if n is prime.
    It returns False if n is not prime.
    Parameters:
        n: number to check if it is prime
    '''
    remainders = 0

    for x in range(2, n):
        if n % x == 1:
            # not divisible
            remainders = remainders + 1
        else:
            # divisible
            remainders = remainders

    if remainders > 0:
        return True
    else:
        return False


assert find_prime(23) == True, "It is prime"
assert find_prime(1) == False, "It is not prime"
assert find_prime(27277) == True, "It is prime"

#_________________________________________________________________
# this way is more efficient

def find_prime2(n):
    '''
    It returns True if n is prime.
    It returns False if n is not prime.
    Parameters:
        n: number to check if it is prime
    '''
    if n == 1:
        return False

    for x in range(2, n):
        if n % x == 0:
            # divisible
            print(x)
            return False

    # it did not find any divisible number
    return True

assert find_prime2(4) == False
assert find_prime2(1) == True

start_time = time.time()
find_prime(817_504_252)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
find_prime2(817_504_252)
print("--- %s seconds ---" % (time.time() - start_time))

143/9
