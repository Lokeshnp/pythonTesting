import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last!")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abc", "Xyz", "Abcxyz@gmail.com"]


@pytest.fixture(params=[("chrome", "QA", "ABC"), ("firefox", "DEV"), ("ie", "UAT")])
def crossBrowser(request):
    return request.param



