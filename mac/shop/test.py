import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

user_name = 'Himani'
head = """
    <strong>Hello, Greetings From Nisarg Trivedi!</strong> We have received your order and hereby, We have shared your shopping bill. Your order will be delivered within 5-6 working days! Thank You for shopping with us, Have A Good Day
    """

message = Mail(
    from_email='nisargtrivedi054@gmail.com',
    to_emails='trivedihimani30@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content=head)

file = r'C:\Users\Nisarg Trivedi\PycharmProjects\MyAwesomeCart\mac\4WOVRA2.pdf'
with open(file, 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('attachment.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)