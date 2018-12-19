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

    if outFileName=='':
        outFileName='{}{}.{}'.format(cutFileName(filepath), formatTo)


    #if extraArguments==['']:
    #    style = 'styles/defualt.css'
    #    extraArguments=('--css {}'.format(style))
    
    #self.pypandocInput = '{filepath},{formatTo}, outputfile={outFileName},extraArgs={}'.format(filepath, formatTo, outFileName, extraArguments)

    pypandoc.convert_file(filepath, formatTo, outputfile=outFileName)

def cutFileName(filepath) :
    posExtension = filepath.find('.')
    posLastDirectory = filepath.rfind('/')
    print(posExtension)
    print(posLastDirectory)

    backtrack = len(filepath) - posExtension
    print(backtrack)

    filename = filepath[posExtension:backtrack]
    print(filename)
    return filename 
