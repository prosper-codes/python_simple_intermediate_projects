
import  smtplib
from email.message import EmailMessage

SENDER = "takundanhau89@gmail.com"
PASSWORD = "hxwgxqcjcikexbcs"
RECEIVER = "prospernews2012@gmail.com"


def send_mail(image_path):
    email_message = EmailMessage()
    email_message["Subject"]  = "Movement dectected"
    email_message.set_content("Hey , we noticed movement in your monitored area")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype = "png")


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_mail(image_path="images/80.png")
    print("email has been sent successfully")