class NotesApplication(object):
    '''note taking application class definition'''

    def __init__(self, author):
        '''constructor for the Notes Application.
        Takes a string, the author, and initialises a list to
        store all the different notes'''
        self.author = author
        self.notes = []

    def create(self, note_content):
        '''This function takes the note content as the
         parameter and adds it to the notes list of the object.
         '''
        self.notes.append(note_content)

    def list(self):
        '''This function lists out each of the notes
        in the notes list'''
        for index, note in enumerate(self.notes):
            args = (index, note, self.author)
            print ("Note ID: {0}\n{1}\n\nBy Author {2}\n\n".format(args))

    def get(self, note_id):
        '''This function takes a note_id which
        refers to the index of the note in the notes
        list and returns the content of that note as a string
        '''
        return self.notes[note_id]

    def search(self, search_text):
        '''This function takes a search string search
        text and prints all the notes with that text
        '''
        for index, note in enumerate(self.notes):
            if search_text in note:
                args = (search_text, index, note, self.author)
                print ("Showing results for search '{0}'\n\nNote ID: {1}\n{2}\n\nBy Author {3}\n\n".format(args))

    def edit(self, note_id, new_content):
        '''This function replaces the content in the
        note at note_id with new_content
        '''
        self.notes[note_id] = new_content