import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QTextEdit,QMenuBar,QMenu,QFileDialog,QInputDialog
from PyQt6.QtGui import QAction,QIcon,QTextCursor,QColor
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100,100,400,300)

        #Initial file path
        self.current_file = None

        # Edit spans entire window
        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        #region Menu Bar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

            #region File Menu
        fileMenu = QMenu("File",self)
        menubar.addMenu(fileMenu)

                #region Actions
            # New
        new_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/new_file.png"),"New",self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

            # Open
        open_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/open_file.png"),"Open",self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

            # Save
        save_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/save_file.png"),"Save",self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

            # Save As
        save_as_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/save_as.png"),"Save As",self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_file_as)
                #endregion
            #endregion
        
            #region Edit Menu
        editMenu = QMenu("Edit",self)
        menubar.addMenu(editMenu)
                #region Actions
            # Undo
        undo_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/undo.png"),"Undo",self)
        editMenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

            # Redo
        redo_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/redo.png"),"Redo",self)
        editMenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        editMenu.addSeparator()
            # Cut
        cut_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/cut.png"),"Cut",self)
        editMenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

            # Copy
        copy_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/copy.png"),"Copy",self)
        editMenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)
        
            # Paste
        paste_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/paste.png"),"Paste",self)
        editMenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        editMenu.addSeparator()

            # Find and Highlight
        find_action = QAction(QIcon("PyQt/Notepad App/Toolbar Icon/find.png"),"Find",self)
        editMenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)

                #endregion
            #endregion
        #endregion

    #region Menu Methods
    def new_file(self):
        print("Creating new file")
        self.edit_field.clear()
        self.current_file = None
        
    def open_file(self):
        print("Opening file")
        file_path,_ = QFileDialog.getOpenFileName(self,"Open File","","All Files(*);; Text File(*.txt);; Python File(*.py)")
        with open(file_path,"r") as file:
            text = file.read()
            self.edit_field.setText(text)

    def save_file(self):
        print("Saving file")
        if self.current_file:
            with open(self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else: 
            self.save_file_as()

    def save_file_as(self):
        print("Saving file as")
        file_path,_ = QFileDialog.getSaveFileName(self,"Save File","","All Files(*);; Text File(*.txt);; Python File(*.py)")
        if file_path:
            with open(file_path,"w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file = file_path

    def find_text(self):
        print("Finding Text")
        search_text,ok = QInputDialog.getText(self,"Find Text","Search for:")
        if ok:
            all_words = []
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = QColor(Qt.GlobalColor.red)

            while(self.edit_field.find(search_text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)

                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)

    #endregion

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())