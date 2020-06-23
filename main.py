from PyPDF4 import PdfFileReader, PdfFileWriter
from os import scandir


# Scan all the files searching for PDFs
def ScanFiles(path):
    files = []

    for file in scandir(path):
        # Check if the file is a PDF, if true, add it to the list
        if file.name[-4:] == ".pdf":
            files.append({
                "path": path,
                "name": file.name
            })

    return files


print("Conversor PDF from the scanner to a correct PDF")

# Ask to the function to search on curent directory
files = ScanFiles(".")

i = 0

# Print all the names of the files to select later which to use
for file in files:
    i += 1

    print("(" + str(i) + ")" + " - " + file["name"])

# Change the selected number to match with the list indexes
num = int(input()) - 1

# Open the file selected and save the page numbers
fileOpenName = files[num]["path"] + "/" + files[num]["name"]
fileOpen = PdfFileReader(fileOpenName)
numPages = fileOpen.getNumPages()

# Create the new file
NewFile = PdfFileWriter()

# Add the pages in the order: fist, last, second, second last...
x = i = 1
while i < numPages + 1:
    # If the page number is pair add from the start, if not, from the end
    if i/2 == int(i/2):
        NewFile.addPage(fileOpen.getPage(numPages-int(i/2)))

    else:
        NewFile.addPage(fileOpen.getPage(int(i/2)))

    i += 1

# Create the file name
filename = files[num]["path"] + "/" + files[num]["name"][:-4] + " final.pdf"

# Save the file
with open(filename, "wb") as f:
    NewFile.write(f)
