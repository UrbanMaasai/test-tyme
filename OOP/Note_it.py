class NotesApplication(object):
	"""Class definition for a note application"""

	def __init__(self,author):#,note_list):
		"""Constructor to instantiate a list of various 
			notes by Author- in this case 'JOE'"""
		#self.author=str(author) 
		self.author=author
		self.note_list=["My First Note"]
		
	def create_note(self,note_content):
		"""To allow creation of notes list
			Takes note_content as a parameter and incrementaly 
			updates notes list
		   """
		self.note_list.append(note_content)
		return(self.note_list)
		#print(self.notes)

	def list_note(self):
		for locate, note in enumerate(self.note_list):
			print("Note ID: {}".format(locate))
			print(note) 
			print("------------------- ")
		print("By Author : {}".format(self.author))
		print(" ")

	def get_note(self, note_id):
		"""This function returns the content of a note
			as a string using a note_id(which refers to the
			 index of the note in the notes """
		for note_id in self.note_list:
			print(note_id)
			return self.note_list[note_id]
	
	def search_note(self, search_text):
		"""A function that takes a search string/text 
			and returns all the notes with that text"""
		# print search result header first
		print ("Displaying results for search '{}'\n".format(search_text))
		for locate, note in enumerate(self.note_list):
			if search_text in note:
				args = (locate, note, self.author)
				print ("Note ID: {}\n{}\n\nBy Author {}\n\n".format(*args))

	def edit_note(self, note_id, new_content):
		"""This function replaces the content in the
			note with new_content using note_id as search parameter"""
		try:
			self.note_list[note_id] = new_content
			return True
		except IndexError:
			return False

#new_note=NotesApplication("G.I.JOE")
#my_note = NotesApplication("G.I.JOE","My Second Note")
note_list = NotesApplication("G.I. JOE")
#note_list.author="G.I. JOE"
#note_content = NotesApplication("My Third Post")
note_list.create_note("My Second Post")
#search_note.search_text("My")
#note_list.search_note("My")

#NotesApplication(note_list).append="My First Note"
#my_note = NotesApplication(list_note)("My first Note")
#print("Notes Aunthored by: {} ".format(new_note) )
#NotesApplication(list_note)
#print(a)
note_list.list_note()
#note_list.get_note(1)
