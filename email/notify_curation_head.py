from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

total_time = 0
count = 0

recipients = {
  {
    "name": "Jui Brahme",
    "email": "juibrahme@gmail.com"
  }
}

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'speakers.json')
)

with open(filepath, 'r') as list:
  speaker = json.load(list)[-1]

for recipient in recipients:
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
      <p><em><strong>Note to {recipient['name']} (Curation Team Head):</strong><br>
      This is Jagdish from the tech team. We’ve received a new speaker registration on the website. Below is the exact email that was automatically sent to the registrant, just keeping you in the loop for your review and further action.</em></p>

      <hr style="margin: 30px 0; border: none; border-top: 1px solid #ccc;">

      <p>Hi {speaker['name']},</p>

      <p>Thank you for registering as a speaker for <strong>TEDxPVGCOET 2025</strong>!</p>

      <p>We’re excited to review your interest in sharing insights on <strong>{speaker['domain']}</strong> and how your experience with <strong>{speaker['organization']}</strong> contributes to our theme of conscious innovation. Your submission has been received successfully.</p>

      <p>Here’s a quick summary of the information you shared:</p>
      <ul>
        <li><strong>Name:</strong> {speaker['name']}</li>
        <li><strong>Email:</strong> {speaker['email']}</li>
        <li><strong>Age:</strong> {speaker['age']}</li>
        <li><strong>Domain:</strong> {speaker['domain']}</li>
        <li><strong>Organization:</strong> {speaker['organization']}</li>
        <li><strong>LinkedIn:</strong> <a href="{speaker['linkedin']}">{speaker['linkedin']}</a></li>
        <li><strong>Instagram:</strong> <a href="{speaker['instagram']}">{speaker['instagram']}</a></li>
        <li><strong>Phone Number:</strong> {speaker['phone_number']}</li>
        <li><strong>Portfolio:</strong> <a href="{speaker['portfolio']}">{speaker['portfolio']}</a></li>
        <li><strong>Audience Impact Statement:</strong> {speaker['audience_impact']}</li>
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
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")

print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Average time taken per mail: {total_time / count} seconds")
