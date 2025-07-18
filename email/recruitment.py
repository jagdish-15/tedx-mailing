from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'recruitment-test.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "🎉 You're Officially a Part of TEDxPVGCOET!"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">

      <p>Dear <strong>{recipient['firstName']} {recipient['lastName']}</strong>,</p>

      <p>I am thrilled to extend my heartfelt congratulations on your selection to the <strong>TEDxPVGCOET</strong> team! 🌟 Your performance during the interview process demonstrated your passion, enthusiasm, and potential to make a significant impact.</p>

      <p>You have been chosen for the <strong>{recipient['team']}</strong> and appointed as the <strong>{recipient['role']}</strong> within the team. Your skills and experiences will play a crucial role in helping us achieve our mission of spreading innovative ideas and inspiring stories within our community.</p>

      <h3>🚀 To kickstart your journey with us, please complete the following steps:</h3>
      <ul>
        <li><strong>📄 Check Your Offer Letter:</strong> Please find your official selection letter attached below this email for your reference.</li>
        <li><strong>📱 Join Our WhatsApp Group:</strong> Stay connected with your fellow team members and receive important updates.</li>
      </ul>

      <p><strong>WhatsApp Group Link:</strong><br>
      <a href="https://chat.whatsapp.com/ChehTR7dq4z9uX21hy1ACC">https://chat.whatsapp.com/ChehTR7dq4z9uX21hy1ACC</a></p>

      <p>🚫 <em>Please Note: These links and details should not be shared with anyone else, as they are exclusively for selected team members.</em></p>

      <p>Once again, congratulations on joining the <strong>TEDxPVGCOET</strong> team! We are excited about the journey ahead and the positive impact we will create together.</p>

      <p>If you have any immediate questions or require further information, please do not hesitate to reach out to us at <strong>+91 70581 82571 (Abhijeet Thore)</strong>.</p>

      <p>Warm regards,<br>
      <strong>Abhijeet Thore</strong><br>
      Licensee & Organizer<br>
      TEDxPVGCOET</p>

    </body>
    </html>
    """
    attachmentPath = os.path.abspath(
      os.path.join(os.path.dirname(__file__), '..', 'attachments', f"{recipient['firstName']}_{recipient['lastName']}.jpg")
    )
    attachment_paths = [attachmentPath]
    print(f"Sending mail to {recipient['firstName'] + " " + recipient['lastName']} ({recipient['email']})...")
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
