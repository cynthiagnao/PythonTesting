import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield #whatever you write after this keyword will be excuted after test_fixtureDemo(setup) is executed
    print("I will be executed last") #ex: close the browser, delete cookies at the end of the test execution

@pytest.fixture()
def dataLoad():
    print ("user profile data is being created")
    return["Cynthia", "Gnao", "cgsoft.com"] #it returns thoses datas

@pytest.fixture(params=[("chrome", "Cynthia", "Gnao"),("Firefox", "cgsoft.com"),("IE", "JJ")]) #the fixture on the 1st run picks Chrome, ...
def crossBrowser(request):
    return request.param

