import pandas as pd
import os


def excel_to_txt(infile, outfile):
    df = pd.read_excel(infile, header=None, index_col=None)
    df.to_csv(outfile, header=None, sep=' ', index=False)


if __name__ == '__main__':
    inputdir_path = 'C:\\Users\\asus\\Desktop\\data2'
    outputdir_path = 'C:\\Users\\asus\\Desktop\\data_format2'
    fileList = os.listdir(inputdir_path)
    for name in fileList:
        inputfileTxt = os.path.join(inputdir_path, name)
        outfileExcel = os.path.join(outputdir_path, name).replace('.xlsx', 'txt')
        excel_to_txt(inputfileTxt, outfileExcel)
