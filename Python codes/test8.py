import smtplib
import getpass


email_object = smtplib.SMTP('smtp.gmail.com',587)
print(email_object.ehlo())
print(email_object.starttls())
password = ""       #getpass.getpass("Password Please  : ")
email = ""
email_object.login(email,password)

from_add = "@gmail.com"

to_add = "@gmail.com"
subject = "Automated Email from Python SMTP Protocol"
message = "Hello ... This message is from Automated generated Python SMTP Protocol !!"
message1 = "Please do not replay to this email!!"





msg = "Subject : " +subject  +'\n' + message + '\n' + message1 


print(email_object.sendmail(from_add,to_add,msg))
print(email_object.quit())