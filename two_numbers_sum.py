def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
		firstNumber = array[i]
		for j in range(i + 1,len(array)):
			secondNumber = array[j]
			if firstNumber + secondNumber == targetSum:
				return [firstNumber,secondNumber]
	return []
