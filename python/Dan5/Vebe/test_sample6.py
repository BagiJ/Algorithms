import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["merlinux.eu", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param)
    def fin():
        print ("finalizing %s" % smtp)
        smtp.close()
    request.addfinalizer(fin)
    return smtp