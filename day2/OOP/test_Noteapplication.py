import unittest
import Noteapplication
#from fizzbuzz import fizz_buzz

class NoteapplicationTest(unittest.TestCase):
	"""Testing the Noteapplication class"""
	""" """
	def create_new_note(self):
		"""Test if function can successfully append new note to note_list"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')
		#self.assertEqual(fizz_buzz(3), 'fizz')

	def search_te(self):
		"""Test returns buzz when input is divisible by five"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')
		#self.assertEqual(fizz_buzz(5), 'fizz')

#if __name__ == ('__main__'):
#	unittest()