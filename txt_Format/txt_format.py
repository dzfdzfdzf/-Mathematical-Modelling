
import os
import openpyxl
import codecs
from openpyxl.utils import get_column_letter

def txt_format(filename,outfile):
    f = open(filename)
    for line in f.readlines():
        with open(outfile, 'a') as m:
            m.write(' '.join(line.split()))
        with open(outfile, 'a') as m:
            m.write('\n')
if __name__=='__main__':
    inputdir_path='C:\\Users\\asus\\Desktop\\raw'
    outputdir_path = "C:\\Users\\asus\\Desktop\\raw_format"
    fileList = os.listdir(inputdir_path)
    print(fileList)
    for name in fileList:
        filename = os.path.join(inputdir_path, name)
        outfile = os.path.join(outputdir_path, name)
        txt_format(filename, outfile)
