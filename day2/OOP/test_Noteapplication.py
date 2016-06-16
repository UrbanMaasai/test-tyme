import unittest
import Note-it
#from Note-it import Noteapplication

class NoteapplicationTest(unittest.TestCase):
	"""Testing the Noteapplication class"""
	""" """
	def if_able_to_create_new_note_and_add_to_note_list(self):
		"""Test if function can successfully append new note to note_list"""
		self.assertEqual(Note-it.create_note(3), 'My Fourth')
		#self.assertEqual(Search_note(3), 'My Third')

	def search_note_list_(self):
		"""Test returns buzz when input is divisible by five"""
		self.assertEqual(Note-it.Search_note(3), 'My Second')
		#self.assertEqual(Search_note(5), 'My Third')



#if __name__ == ('__main__'):
#	unittest()