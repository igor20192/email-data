import os
import fire
import re
import csv
import pathlib
import logging


logging.basicConfig(
    filename="log.logs",
    format="[%(asctime)s] [%(levelname)s] => %(message)s",
    level="INFO",
)


class EmailOperations:
    def __init__(self):
        self.email_list = []

    # Function to detect invalid email
    def email_not_valid(self, data):
        for email in data:
            if not self.email_valid(email.rstrip()):
                self.email_list.append(email.rstrip())

    # Function for displaying invalid emails
    def add_dir_emails(self):
        try:
            self.email_list.clear()  # Clearing the list before use

            self.email_not_valid(self.open_file())

            # Displaying the number of invalid emails
            print(f"Invalid emails ({len(self.email_list)}):")
            # Output of invalid emails
            [print(f"\t{email}") for email in self.email_list]
        except Exception as exc:
            logging.info("Function add_dir_emails Exceptin  %s", exc)
            print(
                "For detailed information on this command, run:python emailoperations.py -ic --help"
            )

    # Function for searching letters by text
    def get_email_text(self, ltr):
        self.email_list.clear()  # Clearing the list before use
        try:

            for email in self.open_file():
                # Add found e-mail and check for validity(txt)
                if re.findall(ltr, email) and self.email_valid(email):
                    self.email_list.append(email.rstrip())

            # Displaying the number of found emails
            print(f"Found emails with '{ltr}' in email ({len(set(self.email_list))}):")
            # Output found emails
            [print(f"\t{email}") for email in set(self.email_list)]

        except Exception as exc:
            print(exc)
            print(
                "For detailed information on this command, run: python emailoperations.py -s --help"
            )
            logging.info("Functions get_email_text Exception: %s", exc)

    # Function for determining valid e-mails
    def email_valid(self, email):

        if (
            re.findall("@", email)
            and len(re.findall("@", email)) == 1
            and len(email[: email.find("@")]) >= 1
            and len(email[email.find("@") + 1 : email.rfind(".")]) >= 1
            and len(email[email.rfind(".") + 1 :]) >= 1
            and len(email[email.rfind(".") + 1 :]) < 5
            and email[email.rfind(".") + 1 :].rstrip().isalpha()
            or email[email.rfind(".") + 1 :].rstrip().isnumeric()
        ):

            return 1
        return 0

    # Function to group e-mail by domain
    def get_domain_email(self):
        self.email_list.clear()  # Clearing the list before use
        # Get all files from emails directory
        for email in self.open_file():
            if self.email_valid(email):
                # Adding all domains
                self.email_list.append(email[email.find("@") + 1 :].rstrip())

        self.group_domain()

    # Functiongroups emails by one domain and arranges domains
    def group_domain(self):
        domain_st = set()  # Plenty to add domains and remove duplicates
        add_email = self.open_file()  # add email
        for domain in sorted(set(self.email_list)):
            for email in add_email:
                if email[email.find("@") + 1 :].rstrip() == domain and self.email_valid(
                    email
                ):
                    # Add found domains and validate e-mail
                    domain_st.add(email.rstrip())

            # Domain and Quantity Output
            print(f"Domain {domain} ({len(domain_st)})")
            # Display e-mail in alphabetical order
            [print(f"\t{email}") for email in sorted(domain_st)]
            # Clearing the set before each loop
            domain_st.clear()

    # Function to determine all e-mails in the logs file
    def email_sent_log(self, path_file):
        log_email = set()
        try:
            with open(path_file, "r") as f:
                # Selecting all emails from Logs file
                for email in f:
                    log_email.add(email[email.find("'") + 1 : -3].rstrip())

            return log_email
        except Exception as exc:
            print(exc)
            logging.info("Function email_sent_log Exception: %s", exc)

    # Function to search all emails
    def all_emails(self):
        self.email_list.clear()  # Clearing the list before use
        # Get all files from emails directory
        for email in self.open_file():
            if self.email_valid(email.rstrip()):
                # Adding all valid e-mails
                self.email_list.append(email.rstrip())

        return set(self.email_list)

    # Function to search for emails that are not in the logs file
    def find_email_not_logs(self, path_to_logs_file):
        try:
            # We compare sets and get the necessary e-mail
            result = self.all_emails().difference(
                self.email_sent_log(str(path_to_logs_file))
            )

            # Displaying the number of e-mails
            print(f"Emails not sent ({len(result)}):")
            # Display e-mail in alphabetical order
            [print(f"\t{eml}") for eml in sorted(result)]
        except Exception as exc:
            print(
                "For detailed information on this command, run: python emailoperations.py -feil --help"
            )
            logging.info("Function find_email_not_logs Exception: %s", exc)

    @staticmethod
    def open_file():
        lst = []
        for filename in os.listdir("emails"):
            # Define the extension
            if pathlib.Path(filename).suffix == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    for email in f:
                        lst.append(email.rstrip())
            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        lst.append(row["email"])
        return lst


a = EmailOperations()
if __name__ == "__main__":
    fire.Fire(
        {  # Dictionary With commands to run the application
            "--incorrect-emails": a.add_dir_emails,
            "-ic": a.add_dir_emails,
            "--search": a.get_email_text,
            "-s": a.get_email_text,
            "--group-by-domain": a.get_domain_email,
            "-gbd": a.get_domain_email,
            "--find-emails-not-in-logs": a.find_email_not_logs,
            "-feil": a.find_email_not_logs,
        }
    )
