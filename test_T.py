import T
import pytest

def test_member_x():
    t = T.T(4.3, -4.2, 3.1, 1.0)
    assert t.x == 4.3

def test_member_y():
    t = T.T(4.3, -4.2, 3.1, 1.0)
    assert t.y == -4.2

def test_member_z():
    t = T.T(4.3, -4.2, 3.1, 1.0)
    assert t.z == 3.1

@pytest.mark.parametrize("t, w", [(T.T(4.3, -4.2, 3.1, 1.0), 1.0),
                                  (T.T(4.3, -4.2, 3.1, 0.0), 0.0)])
def test_member_w(t, w):
    assert t.w == w


@pytest.mark.parametrize("t, expected", [(T.T(4.3, -4.2, 3.1, 1.0), True),
                                         (T.T(4.3, -4.2, 3.1, 0.0), False)])
def test_is_point(t, expected):
    assert t.is_point() == expected


@pytest.mark.parametrize("t, expected", [(T.T(4.3, -4.2, 3.1, 1.0), False),
                                         (T.T(4.3, -4.2, 3.1, 0.0), True)])
def test_is_vector(t, expected):
    assert t.is_vector() == expected

@pytest.mark.parametrize("a, b, expected", [(4.0000001, 4.00000000002, True),
                                            (5.0000001, 4.00000000002, False),
                                            (4.0000001, 4.00000000000, True)])
def test_eqaul(a, b, expected):
    assert T.T.equals(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(T.T(4.3, -4.2, 3.1, 0.0), T.T(4.3, -4.2, 3.1, 0.0), True),
                                            (T.T(3.3, -4.2, 3.1, 0.0), T.T(4.3, -4.2, 3.1, 0.0), False),
                                            (T.T(6.300001, -4.2, 3.1, 0.000001), T.T(6.3, -4.2, 3.1, 0.0), True)])
def test_equality(a, b, expected):
    assert (a == b) == expected

def test_addition():
    a = T.T(4.3, -4.2, 3.1, 0.0)
    b = T.T(4.3, -4.2, 3.1, 0.0)
    c = T.T(8.6, -8.4, 6.2, 0.0)
    assert (a + b) == c

def test_subtraction():
    a = T.T(4.3, -4.2, 3.1, 0.0)
    b = T.T(4.3, -4.2, 3.1, 0.0)
    c = T.T(0.0, 0.0, 0.0, 0.0)
    assert (a - b) == c