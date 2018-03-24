'''
 * Name: Elias Andualem
 * Id: ATR/9391/08
 * Architectural Pattern : Repository Architecture
 * Description: The application shows implementation of repository architecture by using the 'Text Document'
   as central repository that is accessible to all system methods and system methods do not interact directly,
   oll of them can modify the central repository(text).
'''


from tkinter import *
from tkinter import messagebox, filedialog
import os

class Editor():
    def __init__(self, root):
        self.root = root
        self.TITLE = "Text Editor implimented using Repository Architectural style"
        self.file_path = None
        self.set_title()

        frame = Frame(root)
        self.yscrollbar = Scrollbar(frame, orient="vertical")
        self.editor = Text(frame, yscrollcommand=self.yscrollbar.set)
        self.editor.pack(side="left", fill="both", expand=1)
        self.editor.config(wrap="word",
                           undo=True,
                           width=80)
        self.editor.focus()
        self.yscrollbar.pack(side="right", fill="y")
        self.yscrollbar.config(command=self.editor.yview)
        frame.pack(fill="both", expand=1)

        root.protocol("WM_DELETE_WINDOW", self.file_quit)

        self.menubar = Menu(root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", underline=1, command=self.file_new, accelerator="Ctrl+N")
        filemenu.add_command(label="Open...", underline=1, command=self.file_open, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", underline=1, command=self.file_save, accelerator="Ctrl+S")
        filemenu.add_command(label="Save As...", underline=5, command=self.file_save_as, accelerator="Ctrl+Alt+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=2, command=self.file_quit, accelerator="Alt+F4")
        self.menubar.add_cascade(label="File", underline=0, menu=filemenu)

        root.config(menu=self.menubar)

    def save_if_modified(self):
        if self.editor.edit_modified():
            response = messagebox.askyesnocancel("Save?",
                                                 "This document has been modified. Do you want to save changes?")
            if response:
                result = self.file_save()
                if result == "saved":
                    return True
                else:
                    return None
            else:
                return response
        else:
            return True

    def file_new(self):
        result = self.save_if_modified()
        if result != None:
            self.editor.delete(1.0, "end")
            self.editor.edit_modified(False)
            self.editor.edit_reset()
            self.file_path = None
            self.set_title()

    def file_open(self, filepath=None):
        result = self.save_if_modified()
        if result != None:
            if filepath == None:
                filepath = filedialog.askopenfilename()
            if filepath != None and filepath != '':
                with open(filepath, encoding="utf-8") as f:
                    fileContents = f.read()

                self.editor.delete(1.0, "end")
                self.editor.insert(1.0, fileContents)
                self.editor.edit_modified(False)
                self.file_path = filepath

    def file_save(self):
        if self.file_path == None:
            result = self.file_save_as()
        else:
            result = self.file_save_as(filepath=self.file_path)
        return result

    def file_save_as(self, filepath=None):
        if filepath == None:
            filepath = filedialog.asksaveasfilename(filetypes=(
            ('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
        try:
            with open(filepath, 'wb') as f:
                text = self.editor.get(1.0, "end-1c")
                f.write(bytes(text, 'UTF-8'))
                self.editor.edit_modified(False)
                self.file_path = filepath
                self.set_title()
                return "saved"
        except FileNotFoundError:
            print('FileNotFoundError')
            return "cancelled"

    def file_quit(self):
        result = self.save_if_modified()
        if result != None:
            self.root.destroy()

    def set_title(self):
        if self.file_path != None:
            title = os.path.basename(self.file_path)
        else:
            title = "Untitled"
        self.root.title(title + " - " + self.TITLE)

    def undo(self):
        self.editor.edit_undo()

    def redo(self):
        self.editor.edit_redo()



if __name__ == "__main__":
    root = Tk()
    root.wm_state('zoomed')
    editor = Editor(root)
    root.mainloop()
