import os
import smtplib
import imghdr
from email.message import EmailMessage

password = os.getenv("EMAIL-PASSWORD")
sender = "anayvalath@yahoo.com"
receiver = "anayvalath@yahoo.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    yahoo = smtplib.SMTP("smtp.mail.yahoo.com", 465)
    yahoo.ehlo()
    yahoo.starttls()
    yahoo.login(sender, password)
    yahoo.sendmail(sender, receiver, email_message.as_string())
    yahoo.quit()


if __name__ == "__main__":
    send_email(image_path="images/19.png")
