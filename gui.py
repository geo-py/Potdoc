import tkinter as tk
from tkinter import filedialog, ttk
import potdoc
from potdoc import convert

class MainWindow(tk.Frame):
    def __init__(self, master):
        #window
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Potdoc a GUI frontend for Pandoc")
        self.master.wm_iconbitmap('media/potdoc.ico')
        #self.master.resizable(False, False)

        width = 400
        height = 300
        #get centre x coord
        x = int((self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2)
        #get centre (1 third) y coord
        y = int((self.master.winfo_screenheight() - self.master.winfo_reqheight())/3)
        self.master.geometry("{}x{}+{}+{}".format(width, height, x, y))

        #sub frames
        inputFrame = tk.Frame(self)
        inputFrame.pack(anchor='w')
        fromFrame = tk.Frame(self)
        fromFrame.pack(anchor='w')
        toFrame = tk.Frame(self)
        toFrame.pack(anchor='w')
        extraFrame = tk.Frame(self)
        extraFrame.pack(anchor='w')
        
        #buttons
        self.okButton = ttk.Button(extraFrame, text='OK', default='active', command=self.click_ok)
        self.inputButton = ttk.Button(inputFrame, text='Browse', default='active', command=self.select_file)
        self.inputButton.focus_set()
       
        #labels
        lblTo = tk.Label(toFrame, text="To")
        #lblFrom = tk.Label(fromFrame, text="From")
        lblInput = tk.Label(inputFrame, text="file path")
        
        lblOutput = tk.Label(extraFrame, text="Ouput filename")

        #text entries
        self.vTxtOutput = tk.StringVar()
        self.vTxtOutput.set('')
        self.txtOutput = ttk.Entry(extraFrame, textvariable=self.vTxtOutput, width="35")

        self.vTxtInput = tk.StringVar()
        self.vTxtInput.set('C:/User/Desktop/Example.md')
        self.txtInput = ttk.Entry(inputFrame, textvariable=self.vTxtInput, width="35")
        
        #comboboxes
        """ INPUTS = [
            ("Markdown",'.md'),     
            ("Open Document Format",'.odt'),    
            ("Word",'.docx'),   
            ("HTML",'.html'),  
            ]

        OUTPUTS = [
            ("PDF", '.pdf'), 
            ("LaTeX", '.tex'), 
            ("HTML", '.html'), 
            ("Open Document Format", '.odt'), 
            ("Word", '.docx'),
            ] """
        OUTPUTS = ['pdf', 'tex', 'html', 'odt', 'docx']        
        self.vCmbTo = tk.StringVar()
        self.vCmbTo.set('pdf')
        self.cmbTo = ttk.Combobox(toFrame, textvariable=self.vCmbTo, values=OUTPUTS, state="readonly", width="32")
        #INPUTS = ['.md', '.tex', '.odt', '.docx', '.html']
        #self.vCmbFrom = tk.StringVar()
        #self.cmbFrom = ttk.Combobox(fromFrame, textvariable=self.vCmbFrom ,values=INPUTS, state="readonly")

        #packing
        lblTo.pack(anchor='w')
        self.cmbTo.pack(anchor='w')

        #lblFrom.pack()
        #self.cmbFrom.pack()

        lblInput.pack(anchor='w')
        self.inputButton.pack(side="right", anchor='w')
        self.txtInput.pack(side="left", anchor="w")
        
        lblOutput.pack(anchor='w')
        self.txtOutput.pack(anchor='w')
        self.okButton.pack(side="bottom", anchor='w', pady=20)

    def select_file(self):
        self.selected_file = tk.filedialog.askopenfilename(parent=self, initialdir = "Desktop/", title = "Select file", filetypes = (("markdown files","*.md *.markdown"), ("plain text files","*.txt"), ("all files","*.*")))
        self.vTxtInput.set(self.selected_file)
        print(self.selected_file)
        return self.selected_file

    def select_style(self): #currently unused
        self.selected_style = tk.filedialog.askopenfilename(parent=self, initialdir = "Desktop/", title = "Select file", filetypes = (("styles/themes","*.css"),("all files","*.*")))
        return self.selected_style

    def click_ok(self):
        #get parameters
        filepath = self.vTxtInput.get()
        formatTo = self.vCmbTo.get()
        
        #output filename
        outFileName=self.txtOutput.get()
        print(outFileName)

        #styles
        #style='styles/default.css'

        #extra arguments
        """  
        extraArguaments=[
           self.txtExtraArgs,
           '--css {}'.format(style)
        ] 
        """
        
        potdoc.convert(self, filepath, formatTo, outFileName)
#==========================================================================#
if __name__=="__main__":
    root = tk.Tk() 
    Potdoc = MainWindow(root)
    Potdoc.mainloop()

