from turbo_disco.foo import bar

def test_pass():
    bar()

def test_fail():
    assert False
