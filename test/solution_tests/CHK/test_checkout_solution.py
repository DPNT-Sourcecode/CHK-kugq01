from solutions.CHK.checkout_solution import CheckoutSolution


def test_empty_string_returns_zero():
    solution = CheckoutSolution()
    assert solution.checkout("") == 0


def test_single_items_have_correct_price():
    solution = CheckoutSolution()
    assert solution.checkout("A") == 50
    assert solution.checkout("B") == 30
    assert solution.checkout("C") == 20
    assert solution.checkout("D") == 15


def test_multiple_items_without_offer():
    solution = CheckoutSolution()
    assert solution.checkout("AA") == 100
    assert solution.checkout("BB") == 60


def test_special_offer_for_A():
    solution = CheckoutSolution()
    assert solution.checkout("AAA") == 130
    assert solution.checkout("AAAA") == 180
    assert solution.checkout("AAAAA") == 230


def test_special_offer_for_B():
    solution = CheckoutSolution()
    assert solution.checkout("BB") == 45
    assert solution.checkout("BBBB") == 90


def test_mixed_basket():
    solution = CheckoutSolution()
    assert solution.checkout("ABCD") == 115
    assert solution.checkout("AAABB") == 175


def test_invalid_non_string_returns_minus_one():
    solution = CheckoutSolution()
    assert solution.checkout(123) == -1
    assert solution.checkout(None) == -1


def test_invalid_sku_returns_minus_one():
    solution = CheckoutSolution()
    assert solution.checkout("E") == -1
    assert solution.checkout("AE") == -1