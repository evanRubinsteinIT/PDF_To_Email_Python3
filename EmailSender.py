import PDF_Text_Extractor
import smtplib
from email.message import EmailMessage

def sendEmail(userInput):
    #Set up connection with Gmail SMTP Server with SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #Logs into email
        smtp.login('your email address goes here','your password goes here')
        #Format Email Message
        message = EmailMessage()
        message['Subject'] = 'Your subject line goes here '
        message['From'] = 'the from address goes here'
        message['To'] = PDF_Text_Extractor.emailList
        message.set_content("The text for your email goes here")
        #Set the attatchment up
        #Opens file that the user gave as the input, sets the name as 'f'
        with open(userInput, 'rb') as f:
            fileToAttatch = f.read()
            fileName = f.name
        message.add_attachment(fileToAttatch, maintype='document', subtype='pdf', filename = fileName)

        #Sends the message
        smtp.send_message(message)


