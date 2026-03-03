from quick_calc.calculator import Calculator


def test_full_addition_flow():
    """
    Simulates a user performing: 5 + 3
    """
    calc = Calculator()

    a = 5
    b = 3
    result = calc.add(a, b)

    assert result == 8


def test_clear_after_operation():
    """
    Simulates performing an operation and then pressing clear.
    """
    calc = Calculator()

    calc.add(10, 5)
    cleared_value = calc.clear()

    assert cleared_value == 0.0