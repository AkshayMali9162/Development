import imaplib,email

read_msg = imaplib.IMAP4_SSL("imap.gmail.com")

password = ""       #getpass.getpass("Password Please  : ")
email = ""

print(read_msg.login(email,password))

print(read_msg.list())
read_msg.select("INBOX")

typ,data = read_msg.search(None, 'SUBJECT "Automated Email from Python SMTP Protocol"' )
# print(typ,data)
# print(typ)
emailid = data[0]
# print(emailid)
result ,email_data = read_msg.fetch(emailid,'(RFC822)')
# print(result ,email_data)
raw  = email_data[0][1]
# print(raw)
t = raw.decode("utf-8")

print(t)
