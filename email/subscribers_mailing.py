from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = [os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'Brochure.pdf')
)]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "TEDxPVGCOET | Reaching Out for a Potential Collaboration (Suggest subject)"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">

      <!-- Top Banner (TEDxPVGCOET style) -->
      <div style="background-color: #000; color: white; padding: 20px 30px; border-bottom: 4px solid #e62b1e;">
        <div style="font-size: 28px; font-weight: bold;">
          <span style="color: #e62b1e;">TED</span><span style="color: white;">x</span>PVGCOET
        </div>
        <div style="font-size: 12px; color: #ccc; margin-top: 4px;">
          x = independently organized TED event
        </div>
      </div>

      <!-- Main Content -->
      <p>Hello {recipient['name']}</p>
      
      <p>
        Hey FitFeast team!<br><br>

        Hope you're doing well! I'm Aarya Gandhe from TEDxPVGCOET, and we're hosting our flagship TEDx event on 13th September in Pune.<br><br>

        <strong>Our Theme:</strong> "Drishti" represents how one person's vision can bring fresh insights and drive meaningful change.<br><br>

        <strong>Why you're perfect for this:</strong> Your brand embodies 'Drishti' perfectly - [Protein Bar Company] represents the vision of transforming how people fuel their bodies and minds through convenient, nutritious protein solutions that support active lifestyles. Your products reflect the transformative power of proper nutrition and the foresight to create fuel that empowers people to pursue their goals with sustained energy and focus. Great ideas, like great nutrition, provide the perfect foundation and stamina needed to pursue meaningful visions and inspire creative breakthroughs through peak physical and mental performance.<br><br>

        We are actively seeking partners to collaborate with us on this exciting journey. In return, we are pleased to offer your brand the following exclusive sponsorship benefits:<br><br>

        <ul>
          <li><strong>Enhanced Brand Visibility:</strong> Prominent logo placement throughout the event</li>
          <li><strong>Media Coverage:</strong> Access to pre- and post-event promotions across our digital platforms</li>
          <li><strong>On-Site Brand Showcase:</strong> Booths, banners, and product visibility at the venue</li>
          <li><strong>Logo Integration:</strong> Featured on tickets, badges, flyers, and other event collaterals</li>
          <li><strong>Access to Health-Conscious Audience:</strong> Connect with 500+ engineering students and professionals focused on fitness and performance</li>
          <li><strong>Brand Feature in Event Newsletter:</strong> Reach 1000+ engaged subscribers including fitness enthusiasts</li>
          <li><strong>Post-Event Analytics:</strong> Receive audience insights and engagement metrics to measure ROI</li>
          <li><strong>Sponsor Spotlight:</strong> Long-term or title sponsors will receive a dedicated feature on our website, telling your brand's story.</li>
        </ul>

        We're seeking select partners for performance nutrition collaborations - think protein bar sampling stations for sustained energy during our full-day event, exclusive discount vouchers for your protein collections, branded fitness accessories, or co-branded wellness kits that our health-conscious and performance-focused audience would genuinely appreciate.  <br><br>

        Quick 10-minute call to explore this? We can share our detailed partnership deck and discuss sponsorship packages that work best for both of us.<br><br>

        Drop your contact or reach us at <a href="mailto:tedx@pvgcoet.ac.in">tedx@pvgcoet.ac.in</a><br><br>

        Excited to create inspiring experiences and performance-driven visions together!<br><br>

        Best,<br>

        Aarya Gandhe <br>
        Treasurer, Team TEDxPVGCOET
      </p>

      <!-- Bottom Banner -->
      <div style="height: 10px; background: linear-gradient(to right, #e62b1e, #000, #e62b1e); margin-top: 20px;"></div>
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
