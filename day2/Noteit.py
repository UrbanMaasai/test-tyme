class NotesApplication(object):
	"""Class definition for a note application"""

	def __init__(self,Author,note_list):
		"""Constructor to initialize a list of various 
			notes by Author- in this case 'JOE'"""
		self.Author=str(Author) 
		#self.author="JOE"
		self.note_list=[]
		
	def create_note(self,note_content):
		"""To allow creation of notes list
			Takes note_content as a parameter and incrementaly 
			updates notes list
		   """
		self.notes.append(note_content)
		#print(self.notes)
		
	def my_list(self):
		for index, note in enumerate(self.notes):
			print("Note ID: {}".format(index))
			print(note) 
			print(" ")
		print("By Author : {}".format(self.author))
		print(" ")

	def list_note(self):
		"""A function to list each of the notes
			in the notes list by Author """
		for index, note in enumerate(self.notes):
			args = (index, note, self.author)
			print ("Note ID: {0}\n{1}\n\nBy Author {2}\n\n".format(*args))

	def get_note(self, note_id):
		"""This function returns the content of a note
			as a string using a note_id(which refers to the
			 index of the note in the notes """
		try:
			thisid = int(note_id)
			return self.notes[thisid]
		except:
			return None

	def search_note(self, search_text):

		"""A function that takes a search string/text 
			and returns all the notes with that text"""
		# print search result header first
		print ("Displaying results for search '{}'\n\n".format(search_text))

		for index, note in enumerate(self.notes):
			if search_text in note:
				args = (index, note, self.author)
				print ("Note ID: {}\n{}\n\nBy Author {}\n\n".format(*args))

	def edit_note(self, note_id, new_content):
		"""This function replaces the content in the
			note with new_content using note_id as search parameter"""
		try:
			self.notes[note_id] = new_content
			return True
		except IndexError:
			return False

my_note = NotesApplication("G.I.JOE","My Second Note")
#my_note = NotesApplication(list_note)("My first Note")
print("Notes Aunthored by: "+ my_note.Author)
print(my_note.note_list)
#print(a)
