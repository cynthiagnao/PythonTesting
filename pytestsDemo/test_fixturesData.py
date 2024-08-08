import pytest

from pytestsDemo.BaseClass import BaseClass


#from pytestsDemo.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0]) #connect teh logs to the html report file
        log.info(dataLoad[2])
        print(dataLoad[2])

