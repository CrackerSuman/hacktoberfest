import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Your email credentials
sender_email = 'your_email@gmail.com'
sender_password = 'your_email_password'

# Email subject and body
email_subject = 'Application: Your Name - Resume Attached'
email_body = 'Dear Hiring Manager,\n\nI am writing to express my interest in the position at your company. Please find attached my resume for your consideration.\n\nBest regards,\nYour Name'

# List of recipient email addresses
recipient_emails = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# Path to your resume file
resume_file_path = 'path_to_your_resume.pdf'

# Create an SMTP session for sending the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

for recipient_email in recipient_emails:
    # Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = email_subject

    # Attach the resume to the email
    with open(resume_file_path, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name='resume.pdf')
    part['Content-Disposition'] = f'attachment; filename=resume.pdf'
    message.attach(part)

    # Add the email body
    message.attach(MIMEText(email_body, 'plain'))

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())
    print(f"Sent email to {recipient_email}")

# Quit the SMTP server
server.quit()

print("All emails sent successfully.")
