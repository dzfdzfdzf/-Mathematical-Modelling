# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
    inputdir_path='C:\\Users\\asus\\Desktop\\选拔题-时空船舶AIS轨迹分析\\附件：时空船舶AIS轨迹数据'
    outputdir_path = "C:\\Users\\asus\\Desktop\\data10"
    fileList = os.listdir(inputdir_path)
    print(fileList)
    for name in fileList:
        filename = os.path.join(inputdir_path, name)
        outfile = os.path.join(outputdir_path, name)
        txt_format(filename, outfile)
