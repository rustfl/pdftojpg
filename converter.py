import os

INPUT_FILE = 'files/pdf_file.pdf'
OUTPUT_FILE = 'files/jpg_file.jpg'

def convert_pdf_to_jpg(input_file_name, output_file_name):
    ''' Функция для конвертации файла 
    из формата pdf в файл формата jpg '''
    os.system("convert " + input_file_name + " " + output_file_name)


if __name__ == '__main__':
    convert_pdf_to_jpg(INPUT_FILE, OUTPUT_FILE)