import pytest

@pytest.mark.usefixtures("setup")
class TestExampleOne:


    def test_methodone1(self):
        print("I will exectute steps in fixture method")

    def test_methodone2(self):
        print("I will exectute steps in fixture method")

    def test_methodone3(self):
        print("I will exectute steps in fixture method")

    def test_methodone4(self):
        print("I will exectute steps in fixture method")

