# PyQt Notepad app

## Description
This is a simple Notepad application built using `PyQt6`. The application allows you to create, open, edit, and save text files. It also includes basic editing functions such as undo, redo, cut, copy, paste, and a search feature to find and highlight text.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/JordanVF/pyQtNotepad.git
2. Navigate to the project directory: 
```bash
cd pyQtNotepad
```
3. Install the required dependencies:
```bash
pip install PyQt6
```
 
## Usage
1. Run the application
2. Features:
   - New: Create a new file by selecting File > New.
   - Open: Open an existing file using File > Open.
   - Save: Save your current file using File > Save. Use Save As to save with a new name.
   - Undo/Redo: Undo or redo changes using Edit > Undo and Edit > Redo.
   - Cut/Copy/Paste: Use Edit > Cut, Edit > Copy, and Edit > Paste for editing operations.
   - Find: Find and highlight text by selecting Edit > Find.
3. Click the Submit button. After submitting, the entered information will be printed to the console, and the form will reset.

## How it works
- QTextEdit: The core text area is powered by QTextEdit, where users can write and edit text.
- QMenuBar and QActions: The menu bar is created with QMenuBar, containing actions for file and edit operations using QAction.
- File Handling: File operations such as creating, opening, saving, and saving as new files are handled using QFileDialog for path selection and Python file I/O methods.
- Undo/Redo: Basic editing operations such as undo, redo, cut, copy, and paste are connected to the built-in functionality of QTextEdit.
- Text Search: The find function searches for text in the document and highlights all matches using QTextEdit.ExtraSelection.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

