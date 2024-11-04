from typing import List

class Note:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"


class Notebook:
    def __init__(self):
        self.notes: List[Note] = []

    def show_all_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        for index, note in enumerate(self.notes):
            print(f"{index + 1}: {note.title}")

    def show_note_details(self, index):
        if index < 0 or index >= len(self.notes):
            print("Invalid note index.")
            return
        print(self.notes[index])

    def create_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note = Note(title, content)
        self.notes.append(note)
        print("Note created.")

    def create_note(self, note: Note):
        # title = input("Enter note title: ")
        # content = input("Enter note content: ")
        # note = Note(title, content)
        self.notes.append(note)
        print("Note created.")

    def update_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Invalid note index.")
            return
        title = input("Enter new title (leave blank to keep current): ")
        content = input("Enter new content (leave blank to keep current): ")
        if title:
            self.notes[index].title = title
        if content:
            self.notes[index].content = content
        print("Note updated.")

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Invalid note index.")
            return
        del self.notes[index]
        print("Note deleted.")

class ConsoleAPP:
    def __init__(self) -> None:
        self.notebook = Notebook()

    def run(self):
        pass

    def add_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note = Note(title, content)
        self.notebook.create_note(note)

class GUIApp:
    def __init__(self) -> None:
        self.notebook = Notebook()

    def add_note(self):
        title = self.__get_textbox_input()
        content = self.__get_textbox_input()
        note = Note(title, content)
        self.notebook.create_note(note)

    def __get_textbox_input(self):
        # GUI yordamida textboxdan o'qib olyapti
        pass
    

def display_menu():
    print("\nMenu:")
    print("1: Show all notes")
    print("2: Show note details")
    print("3: Create note")
    print("4: Update note")
    print("5: Delete note")
    print("m: Menu again")
    print("q: Quit the application")


def main():
    notebook = Notebook()
    
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            notebook.show_all_notes()
        elif choice == '2':
            index = int(input("Enter note index to view details: ")) - 1
            notebook.show_note_details(index)
        elif choice == '3':
            notebook.create_note()
        elif choice == '4':
            index = int(input("Enter note index to update: ")) - 1
            notebook.update_note(index)
        elif choice == '5':
            index = int(input("Enter note index to delete: ")) - 1
            notebook.delete_note(index)
        elif choice.lower() == 'm':
            continue
        elif choice.lower() == 'q':
            print("You exit the programm.BYE!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()