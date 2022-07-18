from emailoperations import EmailDate

a = EmailDate()


def test_email_valid():
    assert a.email_valid("igor.ud@gmail.com") == True
    assert a.email_valid("max@@.asd.com") == False
    assert a.email_valid(".@asffff.info") == True
    assert a.email_valid("@.gmail.com") == False
    assert a.email_valid("igor@u.com") == True
    assert a.email_valid("ig@.com") == False
    assert a.email_valid("igor@gmail.c") == True
    assert a.email_valid("igr.ud@gm.") == False
    assert a.email_valid("max@net.info") == True
    assert a.email_valid("dasd@rico.commm") == False
    assert a.email_valid("igor@gmail.333") == True
    assert a.email_valid("niks@hot.aia1") == False


def test_add_dir_emails():
    a.add_dir_emails()
    assert a.email_list == [
        "wyman.com",
        "ynolanjones.com",
        "nernserhickle.biz",
        "brad84gmail.com",
        "yahoo.com",
        ".com",
        "com",
        "com",
        "com",
        "@hegmann.info",
    ]


def test_get_email_text():
    a.get_email_text("agustin")
    assert sorted(a.email_list) == sorted(
        [
            "agustin.ziemann@hilpert.info",
            "marquardt.agustina@bins.org",
            "agustin16@gmail.com",
            "agustina.reilly@yahoo.com",
            "agustin.dare@kreiger.biz",
        ]
    )


def test_get_domain_email():
    a.get_domain_email()
    assert sorted(a.email_list) == sorted(
        ["gmail.com", "gmail.com", "gmail.com", "mail.ru"]  # dir emails_test
    )


def test_email_sent_log():
    assert a.email_sent_log(
        "/home/igor/bc387adcbde0d0bacbd547dba57ca857/log-test.logs"
    ) == {
        "kyra05@pollich.com",
        "abigayle.davis@jenkins.com",
        "ccrist@yahoo.com",
        "mcglynn.magdalena@yahoo.com",
        "ivy.hodkiewicz@hotmail.com",
    }


def test_all_emails():
    assert a.all_emails() == {
        "igor@gmail.com",
        "serg@gmail.com",
        "kirstin@mail.ru",
        "kyra05@pollich.com",
        "abigayle.davis@jenkins.com",
        "ccrist@yahoo.com",
        "mcglynn.magdalena@yahoo.com",
        "ivy.hodkiewicz@hotmail.com",
    }
