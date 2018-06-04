import os
import sys
import subprocess

def convert_pdf_to_jpg(input_file_name, output_file_name):
    retcode = subprocess.call("convert -density 300 " + input_file_name + " " + output_file_name, shell=True)
    if retcode == 0:
        print('File', input_file_name, 'has been converted!')
    else:
        print('Error:', retcode)

def main():
    input_file = input('Enter the full path to the pdf file: ')
    if os.access(input_file, os.F_OK):
        output_file = input('Enter a name for the jpg file: ')
        convert_pdf_to_jpg(input_file, output_file)
    else:
        print('File ', input_file, 'not found.')

if __name__ == '__main__':
    main()
