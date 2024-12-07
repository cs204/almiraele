from bank import value

def test_здравствуйте ():
    assert value("здравствуйте, Боб!") == 0

def test_здрасте():
    assert value("здрасте,Боб!") == 20

def test_hello():
    assert value("Hello, Harry!") == 100

