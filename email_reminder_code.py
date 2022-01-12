import os
print(os.getcwd())
os.chdir('C:\\Users\\Lenovo\\Desktop\\email')
print(os.getcwd())
import datetime
format= "%Y %d %b %I:%M %p"
import sys
d=datetime.datetime.today()

one_day=datetime.timedelta(days=1)

e=d.strftime(format)
today=datetime.datetime.strptime(e,format)
f='%A'

three_day=datetime.timedelta(days=3)
with open('schedule.txt','r') as fid:
  a=fid.readlines()
for line in a:


  b=line.split('-')
  c=b[0].strip(' ')
  topic=b[1]
  class_day=datetime.datetime.strptime(c,format)
  
  if   d.strftime(f)=='Friday': 
  
    if (class_day.date() - today.date()) == three_day:

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        mail_content='This is a reminder mail for your class on {0} at {1}. Please join the class on time.'.format(topic,c)
#The mail addresses and password
        sender_address = sys.argv[1]
        sender_pass = sys.argv[2]
        receiver_address = '01malonline@gmail.com'
#Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'OneLearn course series reminder'   #The subject line
#The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        break
  elif (d.strftime(f) =='Monday') or (d.strftime(f) == 'Tuesday') or (d.strftime(f) =='Wednesday') or (d.strftime(f) =='Thursday'):
    if (class_day.date() - today.date())==one_day: 
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        mail_content='This is a reminder mail for your class on {0} at {1}. Please join the class on time.'.format(topic,c)
#The mail addresses and password
        sender_address = sys.argv[1]
        sender_pass = sys.argv[2]
        receiver_address = '01malonline@gmail.com'
#Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'OneLearn course series reminder'   #The subject line
#The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        break
  else:
       print('no class')
       break
