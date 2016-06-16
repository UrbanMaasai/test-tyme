import unittest
import Note_it
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

	def successfully_created_list_as_required(self):
		"""test if the note_list is properly created
		"""
		#testcase = NotesApplication("")
		self.assertListEqual(testcase.notes, [],
							 msg="notes attribute is incorrect")

	def able_to_modify_existing_list(self):
		"""test if edit changes the right variable to the right value"""

		testcase = NotesApplication("G.I. JOE")
		testcase.create("Another Note")
		testcase.edit(1, "Another Note Edited")

		self.assertEqual(testcase.notes[0], "New Note 0",
						 msg="edit value incorrect")


#if __name__ == ('__main__'):
#	unittest()