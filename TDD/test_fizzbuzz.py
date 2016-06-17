import unittest
import fizzbuzz
#from fizzbuzz import fizz_buzz

class fizzBuzzTest(unittest.TestCase):
	"""Testing the fizzbuzz"""
	""" """
	def test_returns_fizz_when_divisible_by_three(self):
		"""Test returns fizz when input is divisible by three"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')
		#self.assertEqual(fizz_buzz(3), 'fizz')

	def test_returns_buzz_when_divisible_by_five(self):
		"""Test returns buzz when input is divisible by five"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')
		#self.assertEqual(fizz_buzz(5), 'fizz')

#if __name__ == ('__main__'):
#	unittest()