import mimetypes
import os
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# auth data
SENDER = os.getenv("SMTP_ID")
PASSWORD = os.getenv("SMTP_PWD")

# add recipents seperating by comma, if a lot of addresses-open with contecst
# manager, or implement script with seperated files if too much of them.
RECIPENT = (
    "tatewa1862@wifame.com",
    "capaxax466@pubpng.com",
)
CC = ("",)
TO = ("",)

# specify subject and text if needed
SUBJECT = "Good morning!"
# if html needed, open it with contecst manager and add 'html' in function
TEXT = """
Consectetur ab ea corporis accusantium et repellat.
Amet minima corporis culpa repellendus nisi.
Nam magnam incidunt quia numquam non Exercitationem?
"""


def make_attachments(mime_mult_obj):
    """Grab the files in folder 'attachments' and create the attachment"""
    for filename in os.listdir("attachments"):
        # extract file types depending on extension and make final MIME object
        # to send by email
        file_type_full = mimetypes.guess_type(filename)[0]
        if file_type_full:
            file_type, sub_filetype = file_type_full.split("/")
        else:
            file_type, sub_filetype = None, None

        if file_type == "text":
            with open(os.path.join("attachments", filename), encoding="utf-8") as file:
                file_obj = MIMEText(file.read(), sub_filetype)

        elif file_type == "audio":
            with open(os.path.join("attachments", filename), "rb") as file:
                file_obj = MIMEAudio(file.read(), sub_filetype)

        elif file_type == "application":
            with open(os.path.join("attachments", filename), "rb") as file:
                file_obj = MIMEApplication(file.read(), sub_filetype)

        elif file_type == "image":
            with open(os.path.join("attachments", filename), "rb") as file:
                file_obj = MIMEImage(file.read(), sub_filetype)

        else:
            # if no extension, make MIMEBase class and configure it
            with open(os.path.join("attachments", filename), "rb") as file:
                file_obj = MIMEBase(file_type, sub_filetype)
                file_obj.set_payload(file.read())
                encoders.encode_base64(file_obj)
        # add_header method adds header to MIME object to let it be attached
        file_obj.add_header("content-disposition", "attachment", filename=filename)
        # attach it to common MIMEMultipart class object
        mime_mult_obj.attach(file_obj)


def make_email_body(text, subject, to, cc, is_attachment=False):
    """Create the final meassage to send"""
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["To"] = ",".join(to)
    msg["Cc"] = ",".join(cc)
    if text:
        msg.attach(MIMEText(text))
    if is_attachment:
        make_attachments(msg)

    return msg.as_string()


def send_email(sender, password, recipient, msg_object):
    """Connect host to server as auth, send email and close connection"""
    # create encrypted SMTP connection host-server
    server = smtplib.SMTP(host=f"smtp.{sender[sender.index('@') + 1:]}", port=587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, recipient, msg_object)


def main():
    try:
        print("Processing...")
        send_email(SENDER, PASSWORD, RECIPENT, make_email_body(TEXT, SUBJECT, TO, CC))
        print("The message has been sent!")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
