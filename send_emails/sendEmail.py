import smtplib
import config

def send_email(subject, msg):

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        message = "Subject: {} \n\n {}".format(subject, msg)

        recipient_EMAIL_ADDRESS = ["f20170619@pilani.bits-pilani.ac.in", "satyamanand4203@gmail.com"]

        server.sendmail(config.EMAIL_ADDRESS, recipient_EMAIL_ADDRESS, message)
        print('Email was "successfully" sent :)')
        server.quit()
    
    except:
        print('There was a failure in sending the "EMAIL".Please try contacting the owner.')


send_email("Subject of the Email", "Following is the BODY of your desired message")