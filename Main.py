from PDF_Text_Extractor import extractEmail
from EmailSender import sendEmail
#Ask user for what PDF they want to use
pdfUserChoice = input("Please input the file you would like to use: ")
#Call functions from other files and use input from above question
extractEmail(pdfUserChoice)
sendEmail(pdfUserChoice)
