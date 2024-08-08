import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self): #will be executed in the pytest.fixture()
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self): #will be executed in the pytest.fixture()
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self): #will be executed in the pytest.fixture()
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self): #will be executed in the pytest.fixture()
        print("I will execute steps in fixtureDemo method")

