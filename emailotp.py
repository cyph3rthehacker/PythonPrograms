import smtplib 
import random

otpint =random.randint(0,9999)
otp=str(otpint)
def send_email():
        re= 'receivers email'
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("enter sender email", "passwd here") 
        message = "Otp is_"+otp+" "
        s.sendmail("sender email", re, message)
        print('email send successfully')
        s.quit()
        
send_email()
uotp=input("enter otp to login: ")
if uotp==otp:
    print('_________success______________')
else:
    print('fail********')
    
//enable less secured app on your gmail settings