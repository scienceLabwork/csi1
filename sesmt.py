import smtplib, ssl
from email.message import EmailMessage

def sendmail(umail,name,acc):
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "csi.it@nirmauni.ac.in"
        receiver_email = umail 
        password = "uvqilbbeamocehox"

        msg = EmailMessage()
        if(acc=="yes"):
            msg.set_content("""
Dear {},

Kudos for successfully registering in HackNUThon 4.0. We are excited to have you join us for this innovative and exciting event. Your registration details have been received and processed successfully.

Event Dates - 29th and 30th of April, 2023
Venue - Nirma University

We will be opening the team registration forms soon. Till then, please form a team of 3-4 participants from the same university.

Keep visiting the official website of HackNUThon 4.0 for the latest updates and do not forget to join the Discord server.
Website link: https://hacknuthon.rudrashah.in    
Discord link: https://discord.gg/pNgKexvW39

We noticed that you have requested for accommodation and meal facility. You will receive a confirmation mail for the same shortly.

We look forward to seeing you at HackNUThon 4.0 and wish you the best of luck.

For any queries, you can contact us -
Tanuj Patel - 8128914684 
Rajat Vanzara - 9662652679

Regards,
Team HackNUThon 4.0
Computer Society of India, Nirma University
            """.format(name))
        else:
            msg.set_content("""
Dear {},

Kudos for successfully registering in HackNUThon 4.0. We are excited to have you join us for this innovative and exciting event. Your registration details have been received and processed successfully.

Event Dates - 29th and 30th of April, 2023
Venue - Nirma University

We will be opening the team registration forms soon. Till then, please form a team of 3-4 participants from the same university.

Keep visiting the official website of HackNUThon 4.0 for the latest updates and do not forget to join the Discord server.
Website link: https://hacknuthon.rudrashah.in    
Discord link: https://discord.gg/pNgKexvW39

We look forward to seeing you at HackNUThon 4.0 and wish you the best of luck.

For any queries, you can contact us -
Tanuj Patel - 8128914684 
Rajat Vanzara - 9662652679

Regards,
Team HackNUThon 4.0
Computer Society of India, Nirma University
            """.format(name))

        msg['Subject'] = "Thank You for registering in HackNUThon 4.0 !!"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
        return "Sent"
    except:
        return "Error"