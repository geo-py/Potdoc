import tkinter as tk
from tkinter import filedialog
import logic
from logic import go

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
        okButton = tk.Button(extraFrame, text='OK', default='active', command=click_ok)
        inputButton = tk.Button(inputFrame, text='Select File', default='active', command=select_file)
       
        #labels
        lblTo = tk.Label(toFrame, text="To")
        lblFrom = tk.Label(fromFrame, text="From")
        lblInput = tk.Label(inputFrame, text="Inputs")
        lblExtra = tk.Label(extraFrame, text="Extra Arguments")
        lblOutput = tk.Label(extraFrame, text="Ouput filename")

        #checkbox
        stylecheckboxvar = tk.IntVar()
        stylecheckbox = tk.Checkbutton(extraFrame, text="custom theme", variable=stylecheckboxvar)

        #text entries
        txtExtraArgs = tk.Entry(extraFrame, width=20)
        txtOutput = tk.Entry(extraFrame)

        #packing
        lblTo.pack(side="top")
        lblFrom.pack(side="top")

        lblInput.pack(side="top", padx=20, pady=20)
        inputButton.pack(side='top')

        stylecheckbox.pack(side="top", padx=20, pady=20)

        lblExtra.pack(side="top")
        txtExtraArgs.pack(side="top", padx=20, pady=20)

        lblOutput.pack(side="top")
        txtOutput.pack(side="top", padx=20, pady=20)

        okButton.pack(side='bottom')
        
        #radiobuttons
        def populateRadioButtons(rb, parent, list):
            v = tk.StringVar()
            v.set(list[0]) # initialize
            for i in range (0, len(list)): #generating listbox contents 
                rb = tk.Radiobutton(parent, text=list[i-len(list)], variable=v, value=list[i-len(list)], state="active")
                rb.pack(side="top", anchor='w')

        outputs = ['.pdf', '.tex', '.html', '.odt', '.docx']
        populateRadioButtons('rbTo', toFrame, outputs)      

        inputs = ['.md', '.odt', '.docx', '.html']
        populateRadioButtons('rbFrom', fromFrame, inputs)

        """ #listboxes
        def populateListBox(lb, list):
            for i in range (0, len(list)): #generating listbox contents 
                lb.insert(i, list[i])
                #lb.pack(side='left')       
                
        lbTo = tk.Listbox(toFrame, selectmode="SINGLE")
        outputs = ['.pdf', '.tex', '.html', '.odt', '.docx']
        populateListBox(lbTo, outputs)      
        lbTo.pack(side="bottom")

        lbFrom = tk.Listbox(fromFrame, selectmode="SINGLE")
        inputs = ['.md', '.odt', '.docx', '.html']
        populateListBox(lbFrom, inputs)
        lbFrom.pack(side="bottom") """

        


#==========================================================================#
if __name__=="__main__":
    root = tk.Tk() 
    Potdoc = MainWindow(root)
    Potdoc.mainloop()

def click_ok():
    #get parameters
    filename = Potdoc.filename
    formatTo= rbTo.curselection
    formatFrom = rbFrom.curselection

    #output filename
    if txtTo.get=="":
        pos = filename.find('.')
        backtrack = len(filename) - pos
        outFileName = filename[:backtrack]
    else:
        outFileName = txtTo.get
    #style
    if (stylecheckboxvar == 1):
        style = getDirectory()
        pos = style.find('.')
        backtrack = len(filename) - pos
        style = filename[:backtrack]
    #extraargs
    if txtExtraArgs == "":
        extraArguaments=['--css {}'.format(style)]
    else:
        extraArguaments=['--css {}'.format(style), txtExtraArgs.get()]
        print('it works')

def go(filename, formatTo="pdf", formatFrom="md", outFileName="", style="styles/default.css", extraArguaments=""):        
    try:
        import pypandoc
    except ImportError:
        import pydocverter as pypandoc

    fileoutput = pypandoc.convert_file(filename, formatTo, outputfile=outFileName, extra_args=extraArguaments)
    # fileoutput = pypandoc.convert_file(filename, '.'.format(formatFrom), outputfile='{}.{}'.format(outFileName, formatTo), extra_args=['--css {}'.format(style), extraArguaments])

    
def select_file():
    Potdoc.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = (("markdown files","*.md *.markdown"), ("plain text files","*.txt"), ("styles/themes","*.css"),("all files","*.*")))
    return Potdoc.filename

