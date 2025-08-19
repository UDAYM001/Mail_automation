📧 Bulk Gmail Sender
🚀 Send personalized emails to multiple recipients in one go using Gmail SMTP. Perfect for batch notifications, reminders, or clarifying doubts in groups.

✨ Features

📋 Batch Emailing – Send emails to hundreds of recipients.
🔐 Secure – Uses Gmail SMTP with TLS encryption.
📝 Customizable Content – Easily set your subject and message body.
📥 Inline Recipient List – No external files needed; just update the list.
⚡ Error Logging – See which emails were sent successfully or failed.


⚙️ Requirements
Python 3.6+
Internet connection
Gmail account with App Password (if 2FA is enabled)


🛠 Installation & Setup

Clone the repository
git clone https://github.com/yourusername/BulkGmailSender.git
cd BulkGmailSender


Install dependencies (standard library included by default)

pip install --upgrade pip


Update the script

sender_email → Your Gmail address
password → Gmail App Password
emails → List of recipients
subject → Email subject line
body → Email content

🚀 Usage

Run the script:

python bulk_email_sender.py
The script will send the email to all recipients.

✅ Success and ❌ failure messages are printed for each email.

🛡 Security Notes

Never use your Gmail main password; always use an App Password.

Keep your credentials private. Avoid pushing them to public repos.

📄 Example
subject = "Team Reminder"
body = """
Hello Team,

Just a quick reminder about the meeting tomorrow at 10 AM.

Regards,
Uday
"""

🌟 Future Enhancements

📧 HTML email support for rich formatting
📎 Attachment support to send files along with emails
📊 CSV import for large recipient lists
⏱ Scheduled sending for timed email campaigns

📝 License
MIT License – feel free to use and modify!
