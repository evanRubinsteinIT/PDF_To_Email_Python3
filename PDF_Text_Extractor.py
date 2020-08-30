#Import needed packadges
import re
import PyPDF2

#Start Function
def extractEmail(userInput):
    #Create object out of file that the user opens, instruct it to read binaries
    fileObj = open(userInput, 'rb')
    #Creates interpreter, using PyPDF2 to be able to pull text from file
    pdfInterpret = PyPDF2.PdfFileReader(fileObj)
    #Pulls the page that the interpreter will read. I only needed it to read the first page, so I set it to 0.
    pageObj = pdfInterpret.getPage(0)
    #This pulls the raw text from the file, and stores it in a variable
    rawTextFromFile = pageObj.extractText()
    #I ended up having to put all of the text from the file in one line because if the email address is split onto two lines,
    #the interpreter on the next line won't be able to properly recognize it
    rawReadableTextFromFile = str.join("",rawTextFromFile.splitlines())
    #I needed the list of emails that gets extracted to be global so that I could use it in the email sender file
    global emailList
    #This finds all of the email addresses in the file and puts them in a list
    emailList = re.findall(r"[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+", rawReadableTextFromFile)
    #emailList.remove("emailyoudontwant@email.com"). You can include this line if there is an address that appears in your document that
    #you don't want in your list

    #I like to print the list of emails after just to make sure that it picked everything up correctly.
    print(emailList)



