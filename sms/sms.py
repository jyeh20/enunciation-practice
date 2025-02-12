import smtplib
import sys
import os
import consts
from sms_types import Auth, CarrierError, EmailError, PasswordError
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("GOOGLE_APP_EMAIL")
PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")


class Sms:
    """
    An agent to send SMS messages to a given phone number.

    Attributes:
        phone_number: The phone number to send messages to.
        carrier: The carrier of the given phone number.
        auth: The authentication credentials for the sender agent.
    """

    def __init__(self, phone_number: str, carrier: str):
        self.recipient = phone_number + consts.CARRIERS[carrier]
        self.auth = self.get_auth(EMAIL, PASSWORD)
        self.server = smtplib.SMTP(consts.SMTP_SERVER, consts.SMTP_PORT)

    def get_carrier(self, carrier: str) -> str:
        """Get the carriers' email address. Throws an error if the given carrier
        is not recognized.

        Args:
            carrier (str): The name of the carrier.

        Returns:
            str: The carriers' email address.
        """
        if carrier not in consts.CARRIERS:
            raise CarrierError(f"Carrier {carrier} is not recognized.")
        return consts.CARRIERS[carrier]

    def get_auth(self, email: str | None, password: str | None):
        """
        Load the authentication from environment if they exist.

        Args:
            email (str | None): The email address to load.
            password (str | None): The password to load.

        Raises:
            EmailError: An error if the email address is not valid.
            PasswordError: An error if the password is not valid.

        Returns:
            Auth: The loaded authentication credentials.
        """
        if not email:
            raise EmailError("No email address given")
        if not password:
            raise PasswordError("No password given")
        return Auth(email, password)

    def send_message(self, message: str):
        """
        Send the given message to the recipient.

        Args:
            message (str): The message to send.
        """
        self.server.starttls()
        self.server.login(self.auth.email, self.auth.password)

        send_msg = f"""
        Subject: {consts.SUBJECT}

        {message}
        """

        print(f"Sending message: {send_msg}")
        self.server.sendmail(self.auth.email, self.recipient, send_msg)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        sys.exit(0)

    in_phone_number = sys.argv[1]
    in_carrier = sys.argv[2]
    in_message = sys.argv[3]

    sms = Sms(in_phone_number, in_carrier)
    sms.send_message(in_message)
