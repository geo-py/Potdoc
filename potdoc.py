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

    if (formatTo==''):
        formatTo='pdf'

    #formatFrom = os.path.splitext(filepath)[1]

    if outFileName=='':
        outFileName=os.path.splitext(filepath)[0] #gets filename (no extension)
        outFileName+= ('.'+formatTo)
    elif outFileName.find('.')!=0:
        outFileName=os.path.splitext(filepath)[0] #gets filename (no extension)
        outFileName+= ('.'+formatTo)
    else:
        outFileName = outFileName

    #if extraArguments==['']:
    #    style = 'styles/defualt.css'
    #    extraArguments=('--css {}'.format(style))
    
    pypandoc.convert_file(filepath, formatTo, outputfile=outFileName)

def cutFileext(filepath) :
    posExtension = filepath.find('.')
    posLastDirectory = filepath.rfind('/')
    filenameLength = len(filepath) - posExtension
    filename = filepath[posLastDirectory:filenameLength]
    return filename 
