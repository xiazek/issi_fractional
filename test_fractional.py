import pytest
from fractional import Fractional

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(5, 6)),
        (Fractional(2, 5), Fractional(1, 5), Fractional(3, 5)),
        (Fractional(-1, 4), Fractional(1, 2), Fractional(1, 4)),
        (2, 2, 4),
    ]
)
def test_add(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(1, 6)),
        (Fractional(3, 4), Fractional(1, 4), Fractional(1, 2)),
        (Fractional(2, 5), Fractional(1, 5), Fractional(1, 5)),
    ]
)
def test_sub(a, b, expected):
    assert a - b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(1, 6)),
        (Fractional(2, 5), Fractional(5, 2), Fractional(1, 1)),
        (Fractional(-1, 4), Fractional(2, 3), Fractional(-1, 6)),
        # compare resilt with ingeger
        (Fractional(1, 4), 4, 1),
    ]
)
def test_mul(a, b, expected):
    assert a * b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(3, 2)),
        (Fractional(2, 5), Fractional(1, 5), Fractional(2, 1)),
        (Fractional(-1, 4), Fractional(2, 3), Fractional(-3, 8)),
        # 1/4 / 1/2 == 1/2,
        (Fractional(1, 4), Fractional(1, 2), Fractional(1, 2)),
    ]
)
def test_truediv(a, b, expected):
    assert a / b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(2, 4), Fractional(1, 2), True),
        (Fractional(1, 3), Fractional(1, 2), True),
        (Fractional(1, 2), Fractional(2, 4), True),
        (Fractional(3, 4), Fractional(2, 3), True),
        (Fractional(3, 4), Fractional(3, 4), True),
    ]
)
def test_comparisons(a, b, expected):
    # eq, lt, le, gt, ge
    assert (a == b) == (a.x * b.y == b.x * a.y)
    assert (a < b) == (a.x * b.y < b.x * a.y)
    assert (a <= b) == (a.x * b.y <= b.x * a.y)
    assert (a > b) == (a.x * b.y > b.x * a.y)
    assert (a >= b) == (a.x * b.y >= b.x * a.y)

# Edge cases
def test_zero_denominator():
    with pytest.raises(ValueError):
        Fractional(1, 0)

def test_zero_numerator():
    assert Fractional(0, 5) == Fractional(0, 1)

def test_negative():
    assert Fractional(-1, 2) == Fractional(1, -2)
    assert Fractional(-1, -2) == Fractional(1, 2)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), 1, Fractional(3, 2)),
        (1, Fractional(1, 2), Fractional(3, 2)),
        (Fractional(2, 5), 2, Fractional(12, 5)),
        (Fractional(-1, 4), 1, Fractional(3, 4)),
    ]
)
def test_add_int(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), 1, Fractional(-1, 2)),
        (1, Fractional(1, 2), Fractional(1, 2)),
        (Fractional(2, 5), 2, Fractional(-8, 5)),
        (Fractional(-1, 4), 1, Fractional(-5, 4)),
    ]
)
def test_sub_int(a, b, expected):
    assert a - b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), 2, Fractional(1, 1)),
        (2, Fractional(1, 2), Fractional(1, 1)),
        (Fractional(2, 5), 5, Fractional(2, 1)),
        (Fractional(-1, 4), 2, Fractional(-1, 2)),
    ]
)
def test_mul_int(a, b, expected):
    assert a * b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), 2, Fractional(1, 4)),
        (2, Fractional(1, 2), Fractional(4, 1)),
        (Fractional(2, 5), 2, Fractional(1, 5)),
        (Fractional(-1, 4), 2, Fractional(-1, 8)),
    ]
)
def test_truediv_int(a, b, expected):
    assert a / b == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), 1, False),
        (Fractional(3, 2), 1, True),
        (Fractional(2, 5), 0, True),
        (Fractional(-1, 4), 0, False),
    ]
)
def test_comparisons_int(a, b, expected):
    assert (a > b) == expected

@pytest.mark.parametrize(
    "frac, expected_str",
    [
        (Fractional(1, 2), "1/2"),
        (Fractional(-3, 4), "-3/4"),
        (Fractional(10, -5), "-2/1"),
        (Fractional(0, 7), "0/1"),
        (Fractional(2, 2), "1/1"),
    ]
)
def test_str(frac, expected_str):
    assert str(frac) == expected_str

