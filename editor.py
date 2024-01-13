import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file(window, text_edit):
    filepath=askopenfilename(filetypes=[("Text Files","*.txt")])

    if not filepath:
        return
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content=f.read()
        text_edit.insert(tk.END,content)
    window.title(f"Open File:{filepath}")

def save_file(window,text_edit):
    filepath=asksaveasfilename(filetypes=[("Text Files","*.txt")])

    if not filepath:
        return
    
    with open (filepath, "w") as f:
       content=text_edit.get(1.0,tk.END)
       f.write(content)
    window.title(f"Save File:{filepath}")


def main():
    window=tk.Tk()
    window.title('Text Editor')
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(0,minsize=500)

    text_editor=tk.Text(window,font='Helvetica 18')
    text_editor.grid(row=0,column=1)

    frame=tk.Frame(window,relief=tk.RAISED,bd=2)
    save_button=tk.Button(frame,text='save',command=lambda :save_file(window,text_editor))
    open_button=tk.Button(frame,text='open',command=lambda:open_file(window,text_editor))

    save_button.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    open_button.grid(row=1,column=1,padx=5,sticky='ew')
    frame.grid(row=0,column=0,sticky='ns')

    # here we add control -s and -o to open and save the files
    window.bind("<Control-s>",lambda x: open_file(window,text_editor))
    window.bind("<Control-o>",lambda x: save_file(window,text_editor))

    window.mainloop()

if __name__ == '__main__':
    main()