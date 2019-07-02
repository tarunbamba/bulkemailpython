import smtplib
import csv
yourmailaddress = 'your email id here' 
yourmailpassword = 'your email password here'     
with open('testdata.csv', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            ' row[4]  is the row where the email id exist in the csv
            mailto = row[4]
            with open('anyfilename.txt', 'r') as myfile:
                msg = myfile.read()
                ' you can use any mail server smtp and password
            mailServer = smtplib.SMTP('Smtp.gmail.com' , 587)
            mailServer.starttls()
            mailServer.login(yourmailaddress , yourmailpassword)
            mailServer.sendmail(yourmailaddress, mailto , msg)
            ' This will print the email id where the email send
            ' read data from your csv file.
            print("Mail sent to ",row[4])
print(" \n Email Sent complete... Thanks for using the Service")
mailServer.quit()
