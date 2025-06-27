from email.message import EmailMessage
import smtplib as sm

EMAIL_EMISOR = "carloseliassalazaryunes@gmail.com"
PASSWORD_EMISOR = "qjtn asvz iixw vmma"
EMAIL_RECEPTOR = "carlosericksalazar@gmail.com"

def enviar_gmail(name, body):
    message = body
    email = EmailMessage()
    email["from"] = EMAIL_EMISOR
    email["to"] = EMAIL_RECEPTOR
    email["Subject"] = f"De {name}"
    email.set_content(message)

    with sm.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_EMISOR, PASSWORD_EMISOR)
        smtp.send_message(email)
        print("Mensaje enviado")


# enviar_gmail("juanito", "hola solicito sus servicios")
