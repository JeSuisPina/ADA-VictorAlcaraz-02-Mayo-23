import random
import sys
sys.setrecursionlimit(100000)
import timeit

def DAC_Max(a, index, l):
	max = -1
	if(l - 1 == 0):
		return arr[index]
	if (index >= l - 2):
		if (a[index] > a[index + 1]):
			return a[index]
		else:
			return a[index + 1]

	# Logic to find the Maximum element
	# in the given array.
	max = DAC_Max(a, index + 1, l)

	if (a[index] > max):
		return a[index]
	else:
		return max

# Function to find the minimum no.
# in a given array.


def DAC_Min(a, index, l):
	min = 0
	if(l - 1 == 0):
		return arr[index]
	if (index >= l - 2):
		if (a[index] < a[index + 1]):
			return a[index]
		else:
			return a[index + 1]

	# Logic to find the Minimum element
	# in the given array.
	min = DAC_Min(a, index + 1, l)

	if (a[index] < min):
		return a[index]
	else:
		return min


# Driver Code
if __name__ == '__main__':

	# Defining the variables
	min, max = 0, -1

	# Initializing the array
	a = [0] * 10000
	for i in range(10000):
		a[i] = 	random.randint(1, 1000)

	# Recursion - DAC_Max function called
	max = DAC_Max(a, 0, 10000)

	# Recursion - DAC_Max function called
	min = DAC_Min(a, 0, 10000)

	t1 = timeit.Timer(lambda: DAC_Max(a, 0, 10000))
	t2 = timeit.Timer(lambda: DAC_Min(a, 0, 10000))
	time_taken1 = t1.timeit(number=1000)
	time_taken2 = t2.timeit(number=1000)

	print("The minimum number in a given array is : ", min)
	print("The maximum number in a given array is : ", max)
	print("Tiempo de ejecución:", (time_taken1 + time_taken2)/1000)
