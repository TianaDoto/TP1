'''content of test_sample.py'''

def inc(number):
    '''This function to increment a number'''
    return number + 1

def test_answer():
    '''This function to test the inc function'''
    assert inc(3) == 5
