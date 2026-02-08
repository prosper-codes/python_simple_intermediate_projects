import  requests
import selectorlib
import  smtplib
from email.message import EmailMessage
import sqlite3

connection = sqlite3.connect("data.db")

SENDER = "senders email"
PASSWORD = "your password"
RECEIVER = "receivers email"

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
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_mail(messeage):
    email_message = EmailMessage()
    email_message["Subject"]  = "New Tour Detected"
    email_message["body"] = messeage

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    print("email was sent")
    gmail.quit()



def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)",row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print (rows)
    return rows

if __name__ =="__main__":
    while True:

        scarped = scrape(URl)
        extracted = extract(scarped)
        print(extracted)


        if extracted != "No upcoming tours":
            row = read(extracted)
            if not  row:
                store(extracted)
                send_mail(messeage="hey we found a message")
