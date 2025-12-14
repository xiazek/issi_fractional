import pytest
from fractional import Fractional

@pytest.mark.parametrize(
    "x, y, normalize, exp_x, exp_y, exp_orig_x, exp_orig_y, exp_str",
    [
        # basic without normalization flag
        # internal (x,y) are always normalized; originals keep only sign normalization
        (1, 2, False, 1, 2, 1, 2, "1/2"),
        (1, -2, False, -1, 2, -1, 2, "-1/2"),
        (-1, -2, False, 1, 2, 1, 2, "1/2"),
        # with normalization flag: originals are also gcd-normalized
        (2, 4, True, 1, 2, 1, 2, "1/2"),
        (3, -6, True, -1, 2, -1, 2, "-1/2"),
        (-3, -6, True, 1, 2, 1, 2, "1/2"),
        (0, -7, True, 0, 1, 0, 1, "0/1"),
    ]
)
def test_initializer_parametrized(x, y, normalize, exp_x, exp_y, exp_orig_x, exp_orig_y, exp_str):
    f = Fractional(x, y, normalize)
    assert (f.x, f.y) == (exp_x, exp_y)
    assert (f.original_x, f.original_y) == (exp_orig_x, exp_orig_y)
    assert str(f) == exp_str

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(5, 6)),
        (Fractional(2, 5), Fractional(1, 5), Fractional(3, 5)),
        (Fractional(-1, 4), Fractional(1, 2), Fractional(1, 4)),
        # with int
        (Fractional(1, 2), 1, Fractional(3, 2)),
        (1, Fractional(1, 2), Fractional(3, 2)),
        (Fractional(2, 5), 2, Fractional(12, 5)),
        (Fractional(-1, 4), 1, Fractional(3, 4)),
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
        # with int
        (Fractional(1, 2), 1, Fractional(-1, 2)),
        (1, Fractional(1, 2), Fractional(1, 2)),
        (Fractional(2, 5), 2, Fractional(-8, 5)),
        (Fractional(-1, 4), 1, Fractional(-5, 4)),
    ]
)
def test_sub(a, b, expected):
    assert a - b == expected

@pytest.mark.parametrize(
    "a, b, expected, expected_str",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(1, 6), '1/6'),
        (Fractional(2, 5), Fractional(5, 2), Fractional(1, 1), '1/1'),
        (Fractional(-1, 4), Fractional(2, 3), Fractional(-1, 6), '-1/6'),
        # with int
        (Fractional(1, 4), 4, 1, "1/1"),
        (Fractional(1, 2), 2, Fractional(1, 1), "1/1"),
        (2, Fractional(1, 2), Fractional(1, 1), "1/1"),
        (Fractional(2, 5), 5, Fractional(2, 1), "2/1"),
        (Fractional(-1, 4), 2, Fractional(-1, 2), "-1/2"),
    ]
)
def test_mul(a, b, expected, expected_str):
    assert a * b == expected
    assert str(a * b) == expected_str

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Fractional(1, 2), Fractional(1, 3), Fractional(3, 2)),
        (Fractional(2, 5), Fractional(1, 5), Fractional(2, 1)),
        (Fractional(-1, 4), Fractional(2, 3), Fractional(-3, 8)),
        (Fractional(1, 4), Fractional(1, 2), Fractional(1, 2)),
        # with int
        (Fractional(1, 2), 2, Fractional(1, 4)),
        (2, Fractional(1, 2), Fractional(4, 1)),
        (Fractional(2, 5), 2, Fractional(1, 5)),
        (Fractional(-1, 4), 2, Fractional(-1, 8)),
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
        # with int
        (Fractional(1, 2), 1, False),
        (Fractional(3, 2), 1, True),
        (Fractional(2, 5), 0, True),
        (Fractional(-1, 4), 0, False),
    ]
)
def test_comparisons(a, b, expected):
    # eq, lt, le, gt, ge
    if isinstance(b, Fractional):
        assert (a == b) == (a.x * b.y == b.x * a.y)
        assert (a < b) == (a.x * b.y < b.x * a.y)
        assert (a <= b) == (a.x * b.y <= b.x * a.y)
        assert (a > b) == (a.x * b.y > b.x * a.y)
        assert (a >= b) == (a.x * b.y >= b.x * a.y)
    else:
        assert (a > b) == expected

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
    "frac, expected_repr",
    [
        (Fractional(1, 2), "Fractional(1, 2)"),
        (Fractional(-3, 4), "Fractional(-3, 4)"),
        (Fractional(10, -5), "Fractional(-2, 1)"),
        (Fractional(0, 7), "Fractional(0, 1)"),
        (Fractional(2, 2), "Fractional(1, 1)"),
    ]
)
def test_repr(frac, expected_repr):
    assert repr(frac) == expected_repr

@pytest.mark.parametrize(
    "frac, expected_str",
    [
        (Fractional(1, 2), "1/2"),
        (Fractional(-3, 4), "-3/4"),
        (Fractional(10, -5), "-10/5"),
        (Fractional(0, 7), "0/7"),
        (Fractional(2, 2), "2/2"),
    ]
)
def test_str(frac, expected_str):
    assert str(frac) == expected_str

@pytest.mark.parametrize(
    "frac1, frac2, expected_str",
    [
        (Fractional(1, 2), Fractional(1, 4), "1/2 + 1/4 = 3/4"),
        (Fractional(3, 6), Fractional(2, 4), "3/6 + 2/4 = 1/1"),
        (Fractional(1, 1), Fractional(2, 2), "1/1 + 2/2 = 2/1"),
        (Fractional(3, -1), Fractional(2, -2), "-3/1 + -2/2 = -4/1"),
    ]
)
def test_str_representation(frac1, frac2, expected_str):
    result = frac1 + frac2
    actual_str = f"{str(frac1)} + {str(frac2)} = {str(result)}"
    assert actual_str == expected_str


@pytest.mark.parametrize(
    "left, right",
    [
        (Fractional(1, 2), Fractional(1, 2)),  # the same value
        (Fractional(2, 4), Fractional(1, 2)),  # reduced equivalent
        (2, Fractional(2, 1)),                 # int consistent with Fractional(2, 1)
        (Fractional(3, 1), 3),                 # Fractional(2, 1) consistent with int
    ],
)
def test_hash(left, right):
    assert hash(left) == hash(right)