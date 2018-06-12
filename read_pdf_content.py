#importing the necessary modules
import PyPDF2
import time

#reading the contents of the file
user_input=input("Enter the name of file along with the path")
file=open(user_input,'rb')

#mention the starting page from where you want to read from the book
start_page=int(input("Enter the starting page"))
pdfReader = PyPDF2.PdfFileReader(file)
num_pages=pdfReader.numPages
#print(num_pages)
#mention the ending page till where you want to read from the book
print("Type end if you want to display till the end page")
end_page=input("Enter the last page till where you want to display PDF")

if end_page=="end" or end_page=="End" or end_page=="END":
    end_page=num_pages
#reads each page one by one and if user press n the moves to next page
while start_page<int(end_page):
    page=pdfReader.getPage(start_page)
    print(page.extractText())
    start_page=start_page+1
    if input("press n for next page")=="n":
        pass
print("------------------File Ended------------------")
