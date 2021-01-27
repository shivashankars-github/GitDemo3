import pytest

from PytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExampleTwo(BaseClass):

    def test_getdata(self, dataload):
        log = self.getlogger()
        log.info(dataload[1])
        log.info(dataload[0])
