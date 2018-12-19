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

        width = 600
        height = 500
        #get centre x coord
        x = int((self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2)
        #get centre (1 third) y coord
        y = int((self.master.winfo_screenheight() - self.master.winfo_reqheight())/3)
        self.master.geometry("{}x{}+{}+{}".format(width, height, x, y))

        #sub frames
        toFrame = tk.Frame(self)
        toFrame.pack(side='right', padx=20, pady=20)
        fromFrame = tk.Frame(self)
        fromFrame.pack(side='left', padx=20, pady=20)
        extraFrame = tk.Frame(self)
        extraFrame.pack(side='bottom', padx=20, pady=20)
        inputFrame = tk.Frame(self)
        inputFrame.pack(side='top', padx=20, pady=20)

        #buttons
        self.okButton = tk.Button(extraFrame, text='OK', default='active', command=self.click_ok)
        self.inputButton = tk.Button(inputFrame, text='Select File', default='active', command=self.select_file)
        self.inputButton.focus_set()
       
        #labels
        lblTo = tk.Label(toFrame, text="To")
        lblFrom = tk.Label(fromFrame, text="From")
        lblInput = tk.Label(inputFrame, text="Inputs")
        
        lblOutput = tk.Label(extraFrame, text="Ouput filename")

        #text entries
        self.txtOutput = tk.Entry(extraFrame)

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
        OUTPUTS = ['.pdf', '.tex', '.html', '.odt', '.docx']
        INPUTS = ['.md', '.tex', '.odt', '.docx', '.html']
        self.vCmbTo = tk.StringVar()
        self.cmbTo = ttk.Combobox(toFrame, textvariable=self.vCmbTo, values=OUTPUTS, state="readonly")
        #self.vCmbFrom = tk.StringVar()
        #self.cmbFrom = ttk.Combobox(fromFrame, textvariable=self.vCmbFrom ,values=INPUTS, state="readonly")

        #packing
        lblTo.pack(side="top")
        self.cmbTo.pack(side="top", padx=20, pady=20)

        #lblFrom.pack(side="top")
        #self.cmbFrom.pack(side="top", padx=20, pady=20)

        lblInput.pack(side="top", padx=20, pady=20)
        self.inputButton.pack(side='top')

        lblOutput.pack(side="top")
        self.txtOutput.pack(side="top", padx=20, pady=20)

        self.okButton.pack(side='bottom')

        

        #==============UNUSED=====================
        #self.styleButton = tk.Button(extraFrame, text='Custom Theme', default='active', command=self.select_style)
        #self.styleButton.pack(side='top')

        #lblExtra = tk.Label(extraFrame, text="Extra Arguments")
        #lblExtra.pack(side="top")
        #self.txtExtraArgs.pack(side="top", padx=20, pady=20)
        #self.txtExtraArgs = tk.Entry(extraFrame, width=20)

        """
        v1 = tk.StringVar()
        v1.set(".md") # initialize
        for text, inputs in INPUTS:
            self.rbFrom = tk.Radiobutton(fromFrame, text=text, variable=v1, value=inputs)
            self.rbFrom.pack(side='top', anchor='w')
       
        v2 = tk.StringVar()
        v2.set(".pdf") # initialize
        for text, outputs in OUTPUTS:
            self.rbTo = tk.Radiobutton(toFrame, text=text, variable=v2, value=outputs)
            self.rbTo.pack(side='top', anchor='w') 
        """

    def select_file(self):
        self.selected_file = tk.filedialog.askopenfilename(parent=self, initialdir = "/",title = "Select file", filetypes = (("markdown files","*.md *.markdown"), ("plain text files","*.txt"), ("all files","*.*")))
        return self.selected_file

    def select_style(self): #currently unused
        self.selected_style = tk.filedialog.askopenfilename(parent=self, initialdir = "/",title = "Select file", filetypes = (("styles/themes","*.css"),("all files","*.*")))
        return self.selected_style

    def click_ok(self):
        #get parameters
        filename = self.selected_file
        formatTo= self.vCmbTo.get()
        #formatFrom = self.vCmbFrom.get()

        #output filename
        outFileName=self.txtOutput.get()

        style='styles/default.css'

        """  
        extraArguaments=[
           self.txtExtraArgs,
           '--css {}'.format(style)
        ] 
        """
        
        potdoc.convert(self, filename, formatTo, outFileName)
#==========================================================================#
if __name__=="__main__":
    root = tk.Tk() 
    Potdoc = MainWindow(root)
    Potdoc.mainloop()

