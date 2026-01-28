
import smtplib
import ssl


def send_email(message):
     host = "smtp.gmail.com"
     port = 587

     username = "your email"
     password = "your password"
     receiver = "receiver email"

     context = ssl.create_default_context()


     with smtplib.SMTP(host, port) as server:
         server.ehlo()
         server.starttls(context=context)
         server.ehlo()
         server.login(username, password)

         server.sendmail(
             username,
             receiver,
             f"Subject: Test Email\n\n{message}"
         )


if __name__ == "__main__":
    send_email("Hello, how are you?")



