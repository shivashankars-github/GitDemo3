import pytest



@pytest.fixture(scope='class')
def setup():
    print("I will execute first")
    yield
    print("I will be execute     last")


@pytest.fixture(scope=  'class')
def dataload():
    print("user data is being created")
    return ["rahul", "shetty", "academy.com"]



@pytest.fixture(params=[("chrome","rahul","shetty"), ("firefox","shiva","ravi"), ("IE",)])
def crossbrowser(request):
    return request.param