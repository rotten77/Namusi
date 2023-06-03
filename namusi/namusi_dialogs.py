
import tkinter
import tkinter.filedialog
from tkinter.messagebox import askyesno, showerror

class NamusiDialogs():
    @staticmethod
    def yesno(title, message):
        tk = tkinter.Tk()
        tk.withdraw()  # hide window
        prompt = askyesno(title, message)
        tk.destroy()
        return prompt
    
    @staticmethod
    def error(title, message):
        tk = tkinter.Tk()
        tk.withdraw()  # hide window
        showerror(title, message)
        tk.destroy()

    @staticmethod
    def select_file(filetypes):
        tk = tkinter.Tk()
        tk.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=tk, filetypes=filetypes)
        tk.destroy()
        return file_name