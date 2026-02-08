import  requests
import selectorlib
import  smtplib
from email.message import EmailMessage

SENDER = "takundanhau89@gmail.com"
PASSWORD = "hxwgxqcjcikexbcs"
RECEIVER = "takundanhau89@gmail.com"

URl = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """ Scrape the page source from URl"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extraxtor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extraxtor.extract(source)["tours"]
    return value


def send_mail(messeage):
    email_message = EmailMessage()
    email_message["Subject"]  = "New Tour Detected"


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    print("email was sent")
    gmail.quit()



def store(extracted):
    with open("data.txt", "a") as file :
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ =="__main__":
    scarped = scrape(URl)
    extracted = extract(scarped)
    print(extracted)
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_mail(messeage="hey we found a message")
