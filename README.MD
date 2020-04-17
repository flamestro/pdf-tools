# PDF Tools

This is a simple script which will split or combine pdf files.

## Split

When you want to split a file you will have to enter a page number.
This is the last page of the first outcome pdf file.

## Combine

When you want to combine multiple PDF files you will need a metadata file as given in the project. 

In the first line of this file you can define the outcome files path.
Starting with line three you can enter multiple files in the order you want to combine them and add information about 
the pages you want to extract from these files.

Example:

```
OUTPUT_FILE=outputfile.pdf
FILE_PATH,START_PAGE,END_PAGE <-(like this) Enter your wished processing order starting with the next line
/home/someuser/somedir/somefile.pdf,2,4
/home/someuser/somedir/somefile.pdf,2,4
/home/someuser/somedir/somefile.pdf,1,4
/home/someuser/somedir/somefile.pdf,7,7
```
