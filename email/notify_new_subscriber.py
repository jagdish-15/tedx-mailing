from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'mailing_list.json')
)

with open(filepath, 'r') as list:
  recipient = json.load(list)[-1]

try:
  subject = "✅ You’re Subscribed – TEDxPVGCOET Mailing List"
  body = f"""
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>{subject}</title>
  </head>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #ffffff; padding: 20px; color: #333;">
    <p>Hi {recipient['name']},</p>

    <p>Thanks for subscribing to the <strong>TEDxPVGCOET</strong> mailing list!</p>

    <p>You’ll now receive updates about speakers, tickets, and other exciting announcements leading up to the event.</p>

    <p>We look forward to staying connected!</p>

    <p>See you in your inbox,<br>
    <strong>Team TEDxPVGCOET</strong></p>
  </body>
  </html>
  """
  print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
  this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
  if this_time > 0:
    print(f"Mail sent in {this_time:.2f} seconds")
except Exception as e:
  print(f"Failed to send mail to {recipient}: {e}")
