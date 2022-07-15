from os import read
import os
import fire
import glob
import re
import csv
import pathlib


class EmailDate:
    def __init__(self):
        self.email_list = []

    def email_valid(self, data):
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
        lst = []
        for filename in os.listdir("emails"):
            if (pathlib.Path(filename).suffix) == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    flext = f
                    self.email_valid(flext)

            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        lst.append(row["email"])

                    self.email_valid(lst)

        os.system(r" >task_1_answer.txt")

        with open("task_1_answer.txt", "a") as fl:
            fl.write(f"Invalid emails ({len(self.email_list)}):\n")
            [fl.write(f"\t{email}\n") for email in self.email_list]

    def get_email_text(self, ltr):
        self.email_list.clear()
        lst = []
        for filename in os.listdir("emails"):
            if (pathlib.Path(filename).suffix) == ".txt":
                with open(f"emails/{filename}", "r") as f:
                    for email in f:
                        if re.findall(ltr, email):

                            self.email_list.append(email.rstrip())

            else:
                with open(f"emails/{filename}", "r") as fb:
                    reader = csv.DictReader(fb, delimiter=";")
                    for row in reader:
                        lst.append(row["email"])
                    for eml in lst:
                        if re.findall(ltr, eml):
                            self.email_list.append(eml.rstrip())

        os.system(r" >task_2_answer.txt")
        with open("task_2_answer.txt", "a") as fl:
            fl.write(
                f"Found emails with 'agustin' in email ({len(self.email_list)}):\n"
            )
            [fl.write(f"\t{email}\n") for email in self.email_list]


a = EmailDate()
if __name__ == "__main__":
    fire.Fire(
        {
            "--incorrect-emails": a.add_dir_emails,
            "-ic": a.add_dir_emails,
            "--search": a.get_email_text,
            "-s": a.get_email_text,
        }
    )
