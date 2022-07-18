from emailoperations import EmailDate

a = EmailDate()


def test_email_valid():
    assert a.email_valid("igor.ud@gmail.com") == True
    assert a.email_valid("max@@.asd.com") == False
    assert a.email_valid(".@asffff.info") == True
    assert a.email_valid("igor@u.com") == True
    assert a.email_valid("ig@.com") == False
    assert a.email_valid("igor@gmail.c") == True
    assert a.email_valid("igr.ud@gm.") == False
    assert a.email_valid("max@net.info") == True
    assert a.email_valid("dasd@rico.commm") == False
    assert a.email_valid("igor@gmail.333") == True
    assert a.email_valid("niks@hot.aia1") == False
