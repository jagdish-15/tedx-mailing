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
    subject = "Collaboration Opportunity - TEDxPVGCOET X ASMITA ORGANIC FARMS"
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
      
      <p>Hey Asmita Organic Farms team!</p>

      <p>Hope you're doing well! I'm Aarya Gandhe from <strong>TEDxPVGCOET</strong>, and we're hosting our flagship TEDx event on <strong>13th September</strong> in Pune.</p>

      <p><strong>Our Theme: "Drishti"</strong> represents how one person's vision can bring fresh insights and drive meaningful change.</p>

      <p><strong>Why you're perfect for this:</strong><br>
      Your brand embodies 'Drishti' perfectly – Asmita Organic Farms represents the vision of reconnecting people with pure, natural nutrition through organic farming practices that honor both the earth and our bodies. Your rice crisps and energy bites reflect the transformative power of choosing clean, wholesome ingredients and the foresight to create nourishing snacks that fuel both physical vitality and mental clarity. Great ideas, like great organic nutrition, grow from authentic foundations – and your farm-fresh, energy-boosting treats provide the sustained focus and natural fuel needed to pursue meaningful visions and drive innovative breakthroughs.</p>

      <p>We are actively seeking partners to collaborate with us on this exciting journey. In return, we are pleased to offer your brand the following exclusive sponsorship benefits:</p>

      <ul>
        <li><strong>Enhanced Brand Visibility:</strong> Prominent logo placement throughout the event</li>
        <li><strong>Media Coverage:</strong> Access to pre- and post-event promotions across our digital platforms</li>
        <li><strong>On-Site Brand Showcase:</strong> Booths, banners, and product visibility at the venue</li>
        <li><strong>Logo Integration:</strong> Featured on tickets, badges, flyers, and other event collaterals</li>
        <li><strong>Brand Feature in Event Newsletter:</strong> Reach 1000+ engaged subscribers including wellness and sustainability enthusiasts</li>
        <li><strong>Post-Event Analytics:</strong> Receive audience insights and engagement metrics to measure ROI</li>
      </ul>

      <p><strong>Sponsor Spotlight:</strong> Long-term or title sponsors will receive a dedicated feature on our website, telling your brand's story.</p>

      <p>We're seeking select partners for organic wellness collaborations – think sampling stations featuring your rice crisps and energy bites, exclusive discount vouchers for your organic snack collections, and inclusion in our goodie bags to ensure all our attendees experience the purity and nourishment that makes Asmita Organic Farms special.</p>

      <p><strong>Quick 10-minute call to explore this?</strong> We can share our detailed partnership deck and discuss sponsorship packages that work best for both of us.</p>

      <p>Drop your contact or reach us at <a href="mailto:tedx@pvgcoet.ac.in">tedx@pvgcoet.ac.in</a></p>

      <p>Excited to create inspiring experiences and organically-driven visions together!</p>

      <p>Best,<br>
      Aarya Gandhe<br>
      Treasurer, Team TEDxPVGCOET</p>

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
