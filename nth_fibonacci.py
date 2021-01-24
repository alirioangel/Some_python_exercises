# Solution 1:
def getNthFib(n, memo = {}):
	if abs(n) <= 1:
		return 0
	if n == 2:
		return 1
	try:
		return memo[n]
	except KeyError:
		result = getNthFib(n - 1, memo) + getNthFib(n - 2, memo)
		memo[n] = result
		return result

# Solution 2:
def getNthFib(n):
    lastTwo = [0,1]
	counter = 3
	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
	return lastTwo[1] if n>1 else lastTwo[0]
