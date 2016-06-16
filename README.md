# test-tyme Repo Stores a note taking app with below requirements:
For this assignment you will be creating OOP code required for implementing a note taking application. Follow the steps listed to complete the assignment.
1.	Create a class called NotesApplication. Remember to inherit from the object class.
2.	Create a constructor that does the following:
o	Takes in a parameter author as the author of the note and saves this as an instance variable.
o	Create a notes list to store all the notes as an instance property.
3.	Create the following functionality for the NotesApplication class
o	create(self, note_content) - This function takes the note content as the parameter and adds it to the notes list of the object.
o	list(self) - This function lists out each of the notes in the notes list in the following format:
o	Note ID: [note_id]
o	[NOTE_CONTENT]
o	
o	By Author [author]
The note_id parameter represents the respective index of each of the items in the list, the NOTE_CONTENTrepresents the note content and the author represents the note author.
o	get(self, note_id) - This function takes a note_id which refers to the index of the note in the notes list and returns the content of that note as a string.
o	search(self, search_text) - This function takes a search string search_text and returns all the notes with that text within it in the following format:
o	Showing results for search ‘[<search_text>]’
o	
o	Note ID: [note_id]
o	[NOTE_CONTENT]
o	
o	By Author [author]
o	edit(self, note_id, new_content) - This function replaces the content in the note at note_id with new_content.
Ensure to put in the necessary validation every step of the way.

