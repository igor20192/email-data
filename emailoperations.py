import os
import fire
import re
import csv
import pathlib


class EmailDate:
    def __init__(self):
        self.email_list = []

    def email_not_valid(self, data):
        for email in data:

            if (
                not re.findall("@", email)
                or len(re.findall("@", email)) > 1
                or len(email[: email.find("@")]) < 1
                or len(email[email.find("@") + 1 : email.rfind(".")]) < 1
                or len(email[email.rfind(".") + 1 :]) < 1
                or len(email[email.rfind(".") + 1 :]) > 5
                or not email[email.rfind(".") + 1 :].rstrip().isalpha()
                and not email[email.rfind(".") + 1 :].rstrip().isnumeric()
            ):

                self.email_list.append(email.rstrip())

    def add_dir_emails(self):
        self.email_list.clear()
        lst = []
        for filename in os.listdir("emails"):
            if (pathlib.Path(filename).suffix) == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    flext = f
                    self.email_not_valid(flext)

            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        lst.append(row["email"])

                    self.email_not_valid(lst)

        print(f"Invalid emails ({len(self.email_list)}):")
        [print(f"\t{email}") for email in self.email_list]

    def get_email_text(self, ltr):
        self.email_list.clear()
        lst = []
        try:
            for filename in os.listdir("emails"):
                if (pathlib.Path(filename).suffix) == ".txt":
                    with open(f"emails/{filename}", "r") as f:
                        for email in f:
                            if re.findall(ltr, email) and self.email_valid(email):
                                self.email_list.append(email.rstrip())

                else:
                    with open(f"emails/{filename}", "r") as fb:
                        reader = csv.DictReader(fb, delimiter=";")
                        for row in reader:
                            lst.append(row["email"])
                        for eml in lst:
                            if re.findall(ltr, eml) and self.email_valid(eml):
                                self.email_list.append(eml.rstrip())

            print(f"Found emails with '{ltr}' in email ({len(set(self.email_list))}):")
            [print(f"\t{email}") for email in set(self.email_list)]

        except Exception as exc:
            print(exc)
            print(
                "For detailed information on this command, run: python emailoperations.py -s --help"
            )

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

    def get_domain_email(self):
        self.email_list.clear()
        for filename in os.listdir("emails"):
            if pathlib.Path(filename).suffix == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    for email in f:
                        if self.email_valid(email):
                            self.email_list.append(
                                email[email.find("@") + 1 :].rstrip()
                            )

            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        eml = row["email"]
                        if self.email_valid(eml):
                            self.email_list.append(eml[eml.find("@") + 1 :].rstrip())

        self.group_domain()

    def group_domain(self):
        domain_st = set()
        for domain in sorted(set(self.email_list)):
            for filename in os.listdir("emails"):
                if pathlib.Path(filename).suffix == ".txt":
                    with open(f"emails/{filename}", "r") as f:
                        for email in f:
                            if email[
                                email.find("@") + 1 :
                            ].rstrip() == domain and self.email_valid(email):
                                domain_st.add(email.rstrip())

                else:
                    with open(f"emails/{filename}", "r") as fb:
                        reader = csv.DictReader(fb, delimiter=";")
                        for row in reader:
                            eml = row["email"]
                            if eml[
                                eml.find("@") + 1 :
                            ].rstrip() == domain and self.email_valid(eml):
                                domain_st.add(eml.rstrip())

            print(f"Domain {domain} ({len(domain_st)})")
            [print(f"\t{email}") for email in sorted(domain_st)]
            domain_st.clear()

    def email_sent_log(self, path_file):
        log_email = set()
        lst = []
        try:
            with open(path_file, "r") as f:
                for email in f:
                    log_email.add(email[email.find("'") + 1 : -3].rstrip())
                    lst.append(email[email.find("'") + 1 : -3].rstrip())

            return log_email
        except Exception as exc:
            print(exc)

    def all_emails(self):
        self.email_list.clear()
        for filename in os.listdir("emails"):
            if pathlib.Path(filename).suffix == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    for email in f:
                        if self.email_valid(email.rstrip()):
                            self.email_list.append(email.rstrip())

            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        eml = row["email"]
                        if self.email_valid(eml.rstrip()):
                            self.email_list.append(eml.rstrip())

        return set(self.email_list)

    def find_email_not_logs(self, path_to_logs_file):
        try:
            result = self.all_emails().difference(
                self.email_sent_log(path_to_logs_file)
            )
            print(f"Emails not sent ({len(result)}):")
            [print(f"\t{eml}") for eml in sorted(result)]
        except Exception:
            print(
                "For detailed information on this command, run: python emailoperations.py -feil --help"
            )


a = EmailDate()
if __name__ == "__main__":
    fire.Fire(
        {
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
