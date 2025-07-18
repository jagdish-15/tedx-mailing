from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

total_time = 0
count = 0

recipients = {
  {
    "name": "Aarya Gandhe",
    "email": "aaryagandhe@gmail.com"
  },
  {
    "name": "Sargun Gurudatta",
    "email": "sargungurudatta2004@gmail.com"
  },
  {
    "name": "Jagdish Prajapati",
    "email": "jagadishdrp@gmail.com"
  }
}

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'sponsors.json')
)

with open(filepath, 'r') as list:
  sponsor = json.load(list)[-1]

for recipient in recipients:
  try:
    subject = "🤝 Sponsorship Interest Confirmed – TEDxPVGCOET 2025"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #ffffff; padding: 20px; color: #333;">
      <!-- Top Banner (TEDxPVGCOET style) -->
      <div style="background-color: #000; color: white; padding: 20px 30px; border-bottom: 4px solid #e62b1e; display: flex; align-items: center; justify-content: space-between;">
        <div style="font-size: 28px; font-weight: bold;">
          <span style="color: #e62b1e;">TED</span><span style="color: white;">x</span>PVGCOET
        </div>
        <div style="font-size: 12px; color: #ccc;">
          x = independently organized TED event
        </div>
      </div>

      <p><em><strong>Note to {recipient['name']} (Finance Team Head):</strong><br>
      This is Jagdish from the tech team. We’ve received a new sponsor registration on the website. Below is the exact email that was automatically sent to the registrant, just keeping you in the loop for your review and further action.</em></p>

      <hr style="margin: 30px 0; border: none; border-top: 1px solid #ccc;">

      <p>Hi {sponsor['name']},</p>

      <p>Thank you for expressing interest in sponsoring <strong>TEDxPVGCOET 2025</strong>.</p>

      <p>We’ve received your details and are grateful for your support as a <strong>{sponsor['tier']}</strong>. Your contribution within the range of <strong>₹{sponsor['range']}</strong> is deeply appreciated, and we’re excited to explore how we can collaborate further.</p>

      <p>Here’s a summary of the information you provided:</p>
      <ul>
        <li><strong>Name:</strong> {sponsor['name']}</li>
        <li><strong>Organization:</strong> {sponsor['organization']}</li>
        <li><strong>Designation:</strong> {sponsor['designation']}</li>
        <li><strong>Email:</strong> {sponsor['email']}</li>
        <li><strong>Phone Number:</strong> {sponsor['phone_number']}</li>
        <li><strong>Sponsorship Tier:</strong> {sponsor['tier']}</li>
        <li><strong>Contribution Range:</strong> ₹{sponsor['range']}</li>
        <li><strong>Website/Social Link:</strong> <a href="{sponsor['link']}">{sponsor['link']}</a></li>
        <li><strong>Expectations from Sponsorship:</strong> {sponsor['expectations']}</li>
        <li><strong>Sponsored Similar Events Before:</strong> {sponsor['have_sponsored_before']}</li>
      </ul>

      <p>Our sponsorship team will be in touch soon to finalize the partnership and share branding, booth, and engagement opportunities.</p>

      <p>Thank you again for supporting ideas worth spreading.</p>

      <p>Warmly,<br>
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
