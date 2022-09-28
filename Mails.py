from email.mime.text import MIMEText
from smtplib import SMTP
 
# Casilla desde donde se envía el mail (necesito saber la clave)
from_address = "info@educacionit.com"
# Mensaje a enviar.
mensaje = "La próxima clase es el sábado 16."
# Construir el mensaje.
# Si tiene HTML uso:
# mime_message = MIMEText(mensaje, "text/html")
mime_message = MIMEText(mensaje, "plain")
mime_message["From"] = from_address
# Asunto del mail
mime_message["Subject"] = "Aviso de feriado"
# Datos del servidor SMTP.
smtp = SMTP("smtp.ejemplo.com")
# clave123 es la contraseña de la dirección que está en from_address.
smtp.login(from_address, "clave123")
 
mails_alumnos = [
    "juan@educacionit.com",
    "sofia@educacionit.com",
    "camila@educacionit.com",
    "matias@educacionit.com"
]
 
for mail in mails_alumnos:
    mime_message["To"] = mail
    smtp.sendmail(from_address, mail, mime_message.as_string())
 
smtp.quit()
