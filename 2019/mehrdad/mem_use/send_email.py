import csv
import diskusage
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def get_contacts(filename='contacts.csv'):
    """ read filename and return names and emails """
    contacts = []
    with open('contacts.csv') as f:
        reader = csv.reader(f)
        for contact in reader:
            contacts.append(contact)
    return contacts


def send():
    sender = 'saeedtempman@gmail.com'
    password = 'k@rs1z:)'
    smtp_server = 'smtp.gmail.com'
    port=587
    
    # Send email for each user
    for user, receiver in get_contacts():
        # create fresh message for each user
        message = MIMEMultipart("alternative")
        message["Subject"] = "Disk usage for you and your calligis at XXX"
        message["From"] = sender
        message["To"] = receiver

        # create content for specific user (highligh user)
        html = diskusage.get_preformatted(user=user, format_type='html')
        # create text file for specific user to be attach 
        filename = diskusage.get_preformatted(user=user, format_type='txt', to_file=True)
        # attachment perp
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename=usage.txt'
        )
        
        # add html message and attachment to message
        message.attach(MIMEText(html, 'html'))  
        message.attach(part)   
        
        # send message
        with smtplib.SMTP(smtp_server, port) as server:            
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())

            # for testing purpose
            print(f'Contetnt sent to {user} with email {receiver}')

if __name__ == '__main__':
    send()
