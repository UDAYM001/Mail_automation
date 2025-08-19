import smtplib
from email.mime.text import MIMEText

# 🔽 Add your recipient email addresses inside the list below
emails = [
    "musk56273@gmail.com",
    "piyuphde@gmail.com",
    "avimrasaha@gmail.com",
    "stn@gmail.com",
    "varsgari123@gmail.com",
    "rawvarun11@gmail.com",
    "jasohanty16@gmail.com",
    "mdbasheru06@gmail.com",
    "chi5@gmail.com",
    "hrushaeagala2004@gmail.com",                              ## these are dummy mails 
    "mylapyathridevi@gmail.com",
    "rk62014072@gmail.com",
    "moni2223@gmail.com",
    "atcramanibonda2004@gmail.com",
    "adahitha2005@gmail.com",
    "kasirnika521@gmail.com",
    "nilesauhan2004@gmail.com",
    "ayushchaswal12345678@gmail.com",
    "padmajyothi06@gmail.com",
    "yerrala172@gmail.com",
    "kavyagaelli208@gmail.com",
    "muskan35163@gmail.com",
    "souas5504@gmail.com",
    "karrisa3333@gmail.com",
    "meenakshimosa@gmail.com",
    "sae.r2005@gmail.com",
    "m383rayapati@gmail.com",
    "na28102003@gmail.com",
    "apakalla20@gmail.com",
    "japkaur2713@gmail.com",
    "chandkapothala7@gmail.com",
    "srisamruthaveedhi@gmail.com",
    "shankmilind447@gmail.com",
]


# ✉️ Email subject and body
subject = "i am a data center batch student from wipro"
body = """
Hello,

i have few doubs on the sections and the meetings 
those who know telugu reply back to this mail there is only two members
in my batch " im am 16th batch " i want to clarify about the log sheets 
modules, and the rps kindly reply to this main if any one who knows telugu

Regards,
Uday
"""


# 🔐 Your Gmail credentials
sender_email = "udaymanchu001@gmail.com"           # Replace with your Gmail
password = "eluc wrzq skue ddaq"     # Replace with your Gmail App Password (no spaces)

# ✅ Send email to all recipients
for recipient in emails:
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient

    try:
        # Use TLS (Port 587)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient, msg.as_string())

        print(f"✅ Email sent to: {recipient}")
    except Exception as e:
        print(f"❌ Failed to send to {recipient}: {e}")
