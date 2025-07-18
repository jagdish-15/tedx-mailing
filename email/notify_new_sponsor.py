from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'sponsors.json')
)

with open(filepath, 'r') as list:
  recipient = json.load(list)[-1]

try:
  subject = "🤝 Sponsorship Interest Confirmed – TEDxPVGCOET 2025"
  body = f"""
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>{subject}</title>
  </head>
  <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #ffffff; color: #333;">

    <!-- Top Banner (TEDxPVGCOET style) -->
    <div style="background-color: #000; color: white; padding: 20px 30px; border-bottom: 4px solid #e62b1e; display: flex; align-items: center; justify-content: space-between;">
      <div style="font-size: 28px; font-weight: bold;">
        <span style="color: #e62b1e;">TED</span><span style="color: white;">x</span>PVGCOET
      </div>
      <div style="font-size: 12px; color: #ccc;">
        <br>
        x = independently organized TED event
      </div>
    </div>

    <!-- Main Content -->
    <div style="padding: 40px 30px;">
      <p>Hi {recipient['name']},</p>

      <p>Thank you for expressing interest in sponsoring <strong>TEDxPVGCOET 2025</strong>.</p>

      <p>We’ve received your details and are grateful for your support as a <strong>{recipient['tier']}</strong>. Your contribution within the range of <strong>₹{recipient['range']}</strong> is deeply appreciated, and we’re excited to explore how we can collaborate further.</p>

      <p>Here’s a summary of the information you provided:</p>
      <ul>
        <li><strong>Name:</strong> {recipient['name']}</li>
        <li><strong>Organization:</strong> {recipient['organization']}</li>
        <li><strong>Designation:</strong> {recipient['designation']}</li>
        <li><strong>Email:</strong> {recipient['email']}</li>
        <li><strong>Phone Number:</strong> {recipient['phone_number']}</li>
        <li><strong>Sponsorship Tier:</strong> {recipient['tier']}</li>
        <li><strong>Contribution Range:</strong> ₹{recipient['range']}</li>
        <li><strong>Website/Social Link:</strong> <a href="{recipient['link']}" style="color: #e62b1e;">{recipient['link']}</a></li>
        <li><strong>Expectations from Sponsorship:</strong> {recipient['expectations']}</li>
        <li><strong>Sponsored Similar Events Before:</strong> {recipient['have_sponsored_before']}</li>
      </ul>

      <p>Our sponsorship team will be in touch soon to finalize the partnership and share branding, booth, and engagement opportunities.</p>

      <p>Thank you again for supporting ideas worth spreading.</p>

      <p>Warmly,<br>
      <strong>Team TEDxPVGCOET</strong></p>
    </div>

    <!-- Bottom Banner -->
    <div style="height: 10px; background: linear-gradient(to right, #e62b1e, #000, #e62b1e); margin-top: 20px;"></div>

  </body>
  </html>
  """
  print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
  this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
  if this_time > 0:
    print(f"Mail sent in {this_time:.2f} seconds")
except Exception as e:
  print(f"Failed to send mail to {recipient['name']}: {e}")
