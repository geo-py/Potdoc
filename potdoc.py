import os

def convert(self, filepath, formatTo, outFileName):
    try:
        import pypandoc
    except ImportError:
        import pydocverter as pypandoc

    acceptedFormats=[
        'pdf',
        'html',
        'tex',
        'md',
        'docx',
        'odt',
    ]

    if (formatTo=='') or (formatTo not in acceptedFormats):
        formatTo='pdf'

    formatFrom = os.path.splitext(filepath)[1]

    if outFileName=='':
        outFileName=os.path.splitext(filepath)[0] #gets filename (no extension)
        outFileName+= ('.'+formatTo)
        
    #if extraArguments==['']:
    #    style = 'styles/defualt.css'
    #    extraArguments=('--css {}'.format(style))
    
    #self.pypandocInput = '{filepath},{formatTo}, outputfile={outFileName},extraArgs={}'.format(filepath, formatTo, outFileName, extraArguments)
    print(filepath)
    print(outFileName)
    print(formatTo)

    pypandoc.convert_file(filepath, formatTo, outputfile=outFileName)

def cutFileext(filepath) :
    posExtension = filepath.find('.')
    posLastDirectory = filepath.rfind('/')
    filenameLength = len(filepath) - posExtension
    filename = filepath[posLastDirectory:filenameLength]
    return filename 
