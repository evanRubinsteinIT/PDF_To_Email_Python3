import re
import PyPDF2
import smtplib
from email.message import EmailMessage

# Ask user for what PDF they want to use
pdfUserChoice = input("Please input the file you would like to use: ")


# Call functions from other files and use input from above question
# Import needed packadges
# Start Function
def extractEmail(userInput):
    # Create object out of file that the user opens, instruct it to read binaries
    fileObj = open(userInput, 'rb')
    # Creates interpreter, using PyPDF2 to be able to pull text from file
    pdfInterpret = PyPDF2.PdfFileReader(fileObj)
    # Pulls the page that the interpreter will read. I only needed it to read the first page, so I set it to 0.
    pageObj = pdfInterpret.getPage(0)
    # This pulls the raw text from the file, and stores it in a variable
    rawTextFromFile = pageObj.extractText()
    # I ended up having to put all of the text from the file in one line because if the email address is split onto two lines,
    # the interpreter on the next line won't be able to properly recognize it
    rawReadableTextFromFile = str.join("", rawTextFromFile.splitlines())
    # I needed the list of emails that gets extracted to be global so that I could use it in the email sender file
    global emailList
    # This finds all of the email addresses in the file and puts them in a list
    emailList = re.findall(r"[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+", rawReadableTextFromFile)
    # emailList.remove("emailyoudontwant@email.com"). You can include this line if there is an address that appears in your document that
    # you don't want in your list
    # I like to print the list of emails after just to make sure that it picked everything up correctly.
    print(emailList)


def sendEmail(userInput):
    # Set up connection with Gmail SMTP Server with SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # Logs into email
        smtp.login('your email address goes here', 'your password goes here')
        # Format Email Message
        message = EmailMessage()
        message['Subject'] = 'Your subject line goes here '
        message['From'] = 'the from address goes here'
        message['To'] = emailList
        message.set_content("The text for your email goes here")
        # Set the attatchment up
        # Opens file that the user gave as the input, sets the name as 'f'
        with open(userInput, 'rb') as f:
            fileToAttatch = f.read()
            fileName = f.name
        message.add_attachment(fileToAttatch, maintype='document', subtype='pdf', filename=fileName)

        # Sends the message
        smtp.send_message(message)


extractEmail(pdfUserChoice)
sendEmail(pdfUserChoice)
