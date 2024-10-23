from sum_and_product import calculateProduct, calculateSum


def test_sum():
    assert calculateSum([]) == 0

    assert calculateSum([2, 4, 6, 8, 10]) == 30


def test_product():
    assert calculateProduct([]) == 1

    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
