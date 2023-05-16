from app.models import Bartender

def test_bartender():
    bartender = Bartender(name = 'moe', hometown = 'springfield', birthyear = 1925)
    assert bartender.name == 'moe'
    assert bartender.hometown == 'springfield'
    assert bartender.birthyear == 1925