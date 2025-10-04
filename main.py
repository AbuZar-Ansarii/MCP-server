from fastmcp import FastMCP
import random
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

mcp = FastMCP(name='simple calculator server')

@mcp.tool
def add_numbers(a:int, b:int)->int:
    'this tool return sum of two given numbers'
    return a + b

@mcp.tool
def generate_randon_num()->int:
    'this tool generate randon number'
    num = random.randint(1,100)
    return num

mcp.resource('info://server')
def server_info()->str:
    'get infotmation about the server'

    info = {
        'name': 'simple calculator',
        'version': '1.0.0',
        'description': 'a basic mcp server with math tool',
        'tools': ['add','random'],
        'author': 'Mohd Abuzar'
    }
    return json.dumps(info,indent=2)


# ⚡ Configure your email credentials here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "fake.emailt1t2@gmail.com"
SENDER_PASSWORD = "klkezzmoqqnhnhgb" 

@mcp.tool()
def send_email(receiver: str, subject: str, content: str) -> str:
    """Send an email to the given receiver with subject and content."""
    try:
        # Validate receiver email
        validate_email(receiver)

        # Create email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(content, "plain"))

        # Send using SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver, msg.as_string())

        return f"✅ Email sent successfully to {receiver}"
    except EmailNotValidError:
        return "❌ Invalid receiver email address"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

if __name__ == "__main__":
    mcp.run(transport ='http', host ='0.0.0.0', port =8000)
