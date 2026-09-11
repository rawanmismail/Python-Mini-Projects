from age import adult

def test_adult():
    assert adult(18) == True
    assert adult(17) == False
    assert adult(20) == True
    assert adult(0) == False
    assert adult(-1) == False
