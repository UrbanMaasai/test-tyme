def fizz_buzz(n):
	"""Returns fizz when divisible by 3
		Returns buzz when divisible by 5
		and fizzbuzz if divisible by both 3 and 5"""
	if n % 3 == 0 and n % 5 == 0:
		return 'fizzbuzz'
	elif n % 3 == 0:
		return 'fizz'
	elif n % 5 == 0:
		return 'buzz'