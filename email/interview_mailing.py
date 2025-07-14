from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = []

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'interview_test.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "TEDxPVGCOET Interview Confirmation (test)"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">

      <p>🌟 <strong>Greetings from TEDxPVGCOET!</strong> 🌟</p>

      <p>Hi <strong>{recipient['firstName'] + " " + recipient['lastName']}</strong>,</p>

      <p>We are thrilled to inform you that after a thorough selection process, <strong>you have been shortlisted</strong> for an interview with <strong>TEDxPVGCOET</strong>!</p>

      <h3>🗓 Interview Details:</h3>
      <ul>
        <li><strong>Date:</strong> {recipient['date']}</li>
        <li><strong>Time Slot:</strong> {recipient['timeSlot']}</li>
        <li><strong>Venue:</strong> Library, PVGCOET</li>
      </ul>

      <h3>✅ Interview Guidelines:</h3>
      <ul>
        <li>⏳ Reach at least <strong>20 minutes early</strong> with a <strong>printout of your resume</strong>.</li>
        <li>Complete the <strong>registration</strong> with our team at the <strong>Library Reading Hall</strong>.</li>
        <li>You will be guided to the interview room when it’s your turn.</li>
        <li>💻 If applicable (e.g., for Technical or Editorial or DnP roles), you may bring your <strong>laptop</strong> to showcase previous work.</li>
        <li>🆔 <strong>Carry your College ID Card</strong> – it is mandatory.</li>
        <li>📚 <strong>Maintain decorum in the library</strong>. Any disruption may result in interview cancellation.</li>
        <li>🚫 <strong>No personal belongings</strong> will be allowed inside the interview room (except permitted items).</li>
      </ul>

      <h3>📞 For Queries, Contact:</h3>
      <ul>
        <li>Abhijeet Thore – +91 70581 82571</li>
        <li>Avani Thakur – +91 90211 56296</li>
        <li>Aarya Gandhe – +91 98609 45719</li>
        <li>Varun Tammewar – +91 77199 01843</li>
      </ul>

      <p>Also, join our <strong>WhatsApp Interview Group</strong> here:<br>
      🔗 <a href="https://chat.whatsapp.com/FIy4AyarEQDLb8N75v3ixq?mode=ac_c">Join Interview Group</a></p>

      <p>🚫 <em>Please do not share this link with anyone else.</em></p>

      <p>Once again, thank you for your participation. We are truly excited to have you onboard and look forward to an <strong>inspiring conversation</strong> with you!</p>

      <p>Warm regards,<br>
      <strong>Abhijeet Thore</strong><br>
      TEDxPVGCOET</p>

    </body>
    </html>
    """
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
print(f"Average time taken per mail: {count / total_time} seconds")
