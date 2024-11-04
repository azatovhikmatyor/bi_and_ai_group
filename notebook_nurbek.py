from tabulate import tabulate


def show_all_notes(notes):
    headers = ["ID", "Content"]
    table = []
    for i, note in enumerate(notes, start=1):
        table.append([i, note["content"]])
    print(tabulate(table, headers=headers))

def show_note_details(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            print(f"ID: {note['id']}")
            print(f"Content: {note['content']}")
            break
    else:
        print(f"Note with ID {note_id} not found.")

def create_note(notes):
    content = input("Enter note content: ")
    notes.append({"id": len(notes) + 1, "content": content})
    print("Note created successfully.")

def update_note(notes, note_id):
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            content = input("Enter new content for the note: ")
            note["content"] = content
            print(f"Note with ID {note_id} updated successfully.")
            break
    else:
        print(f"Note with ID {note_id} not found.")

def delete_note(notes, note_id):
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            print(f"Note with ID {note_id} deleted successfully.")
            break
    else:
        print(f"Note with ID {note_id} not found.")

def main():
    notes = []
    while True:
        print("\nNotebook Menu:")
        print("1: Show All Notes")
        print("2: Show Note Details")
        print("3: Create Note")
        print("4: Update Note")
        print("5: Delete Note")
        print("Q: Quit")
        print("M: Show Menu Again")

        choice = input("Enter your choice: ").upper()

        if choice == "1":
            show_all_notes(notes)
        elif choice == "2":
            note_id = int(input("Enter note ID: "))
            show_note_details(notes, note_id)
        elif choice == "3":
            create_note(notes)
        elif choice == "4":
            note_id = int(input("Enter note ID to update: "))
            update_note(notes, note_id)
        elif choice == "5":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(notes, note_id)
        elif choice == "Q":
            break
        elif choice == "M":
            continue
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()