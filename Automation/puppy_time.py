import smtplib, ssl

# need to test code
port = input('Enter port')
email = input('Enter email: ')
password = input.getPass('Enter password: ')

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)