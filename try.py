import smtplib
import pandas as pd

e = pd.read_excel("emails.xlsx")
emails = e["Emails"].values

your_email = "ahanabhattacherjee@gmail.com"
your_password = "niwv ezpk torl dwxd"

subject = "Test Email"
body = "Hello! How are you?"

message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(your_email, your_password)

for mail in emails:
    server.sendmail(your_email, mail, message)
    print("Email sent to:", mail)

server.quit()