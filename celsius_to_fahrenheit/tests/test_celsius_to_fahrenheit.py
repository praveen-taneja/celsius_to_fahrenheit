from celsius_to_fahrenheit.celsius_to_fahrenheit import celsius_to_fahren

def test_celsius_to_fahrenheit():

    assert celsius_to_fahren(0)[0] == 32
    assert celsius_to_fahren(100)[0] == 212
    assert celsius_to_fahren("xyz")[0] == None