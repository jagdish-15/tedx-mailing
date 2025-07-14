from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'speakers.json')
)

with open(filepath, 'r') as list:
  recipient = json.load(list)[-1]

try:
  subject = "🎤 Speaker Registration Received – TEDxPVGCOET 2025"
  body = f"""
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>{subject}</title>
  </head>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #ffffff; padding: 20px; color: #333;">
    <p>Hi {recipient['name']},</p>

    <p>Thank you for registering as a speaker for <strong>TEDxPVGCOET 2025</strong>!</p>

    <p>We’re excited to review your interest in sharing insights on <strong>{recipient['domain']}</strong> and how your experience with <strong>{recipient['organization']}</strong> contributes to our theme of conscious innovation. Your submission has been received successfully.</p>

    <p>Here’s a quick summary of the information you shared:</p>
    <ul>
      <li><strong>Name:</strong> {recipient['name']}</li>
      <li><strong>Email:</strong> {recipient['email']}</li>
      <li><strong>Age:</strong> {recipient['age']}</li>
      <li><strong>Domain:</strong> {recipient['domain']}</li>
      <li><strong>Organization:</strong> {recipient['organization']}</li>
      <li><strong>LinkedIn:</strong> <a href="{recipient['linkedin']}">{recipient['linkedin']}</a></li>
      <li><strong>Instagram:</strong> <a href="{recipient['instagram']}">{recipient['instagram']}</a></li>
      <li><strong>Phone Number:</strong> {recipient['phone_number']}</li>
      <li><strong>Portfolio:</strong> <a href="{recipient['portfolio']}">{recipient['portfolio']}</a></li>
      <li><strong>Audience Impact Statement:</strong> {recipient['audience_impact']}</li>
    </ul>

    <p>Our curation team will carefully review your application and reach out shortly with the next steps. If you have any questions or updates, feel free to reply to this email.</p>

    <p>Warm regards,<br>
    <strong>Team TEDxPVGCOET</strong></p>
  </body>
  </html>
  """
  print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
  this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
  if this_time > 0:
    print(f"Mail sent in {this_time:.2f} seconds")
except Exception as e:
  print(f"Failed to send mail to {recipient['name']}: {e}")
