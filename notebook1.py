from typing import List

class Note:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __str__(self):
        pass

    ...


class Notebook:
    def __init__(self, notes: List[Note] = None):
        # if notes is not None:
        #     self.notes = notes
        # else:
        #     self.notes = []
        self.notes = notes if notes else []

    def add_note(self, note: Note):
        # Implementation
        pass

    def update_note(self, note_id: int, new_note: Note):
        pass

    def remove_note(self, note_id: int):
        pass

    def list_notes(self):
        pass


class ConsoleApp:
    def __init__(self):
        self.notebook = Notebook()

    def add_note(self):
        # Implementation
        pass

    def update_note(self):
        pass

    def remove_note(self):
        id = int(input("Id = "))
        pass

    def list_notes(self):
        pass
