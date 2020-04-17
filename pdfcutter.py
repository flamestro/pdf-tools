#!/usr/bin/python3

"""pdfcutter.py: This is an script to combine and split pdf files"""

__author__ = "Ahmet Kilic https://github.com/flamestro"

from PyPDF2 import PdfFileWriter, PdfFileReader


# inspired by source: https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
def split_pdf_to_two(filename, page_number, directory=""):
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:
        assert page_number < pdf_reader.numPages
        pdf_writer1 = PdfFileWriter()
        pdf_writer2 = PdfFileWriter()

        for page in range(page_number):
            pdf_writer1.addPage(pdf_reader.getPage(page))

        for page in range(page_number, pdf_reader.getNumPages()+1):
            pdf_writer2.addPage(pdf_reader.getPage(page))

        with open("{}part1.pdf".format(directory), 'wb') as file1:
            pdf_writer1.write(file1)

        with open("{}part2.pdf".format(directory), 'wb') as file2:
            pdf_writer2.write(file2)

    except AssertionError as e:
        print("Error: The PDF you are cutting has less pages than you want to cut!")


def combine_pdf_files(metadata=open("metadata", "r").read().splitlines()):
    output_path = metadata[0].split("=")[1]
    relevant_lines = metadata[2:]
    pdf_writer = PdfFileWriter()
    print(metadata)
    for line in relevant_lines:
        print("processing line: {}".format(line))
        pdf_reader = PdfFileReader(open(line.split(",")[0], "rb"))
        try:
            start_page = int(line.split(",")[1]) - 1
            end_page = int(line.split(",")[2])
            assert int(line.split(",")[2]) < pdf_reader.numPages
            if start_page != end_page:
                for page in range(start_page, end_page):
                    print("line {} adding page {}".format(line, page+1))
                    pdf_writer.addPage(pdf_reader.getPage(page))
            else:
                print("line {} adding page {}".format(line, start_page+1))
                pdf_writer.addPage(pdf_reader.getPage(start_page))
        except AssertionError as e:
            print("Error: The PDF you are cutting has less pages than you want to cut!")
    with open(output_path, 'wb') as file1:
        pdf_writer.write(file1)


if __name__ == "__main__":
    choice = input("enter split to split a file in two files or enter combine to combine multiple pdf files to one: ")
    if choice == "split":
        file_path = input("Enter the absolute path to your file: ")
        page_number = input("Enter the page from which you want to split the file: ")
        directory = input("Enter the directory in which you want to save the file : ")
        if not directory.endswith("/") and directory != "":
            directory += "/"
        split_pdf_to_two(file_path, int(page_number), directory)
    elif choice == "combine":
        metafile = input("Enter the absolute path to your metadata file: ")
        combine_pdf_files(metadata=open(metafile, "r").read().splitlines())
    else:
        print("Shame on you... you have made the wrong choice...")
