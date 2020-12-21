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

def test_is_point():
    t = T.T(4.3, -4.2, 3.1, 1.0)
    assert t.is_point() == True

def test_is_vector():
    t = T.T(4.3, -4.2, 3.1, 1.0)
    assert t.is_vector() == False
    
def test_is_point():
    t = T.T(4.3, -4.2, 3.1, 0.0)
    assert t.is_point() == False
    
def test_is_vector():
    t = T.T(4.3, -4.2, 3.1, 0.0)
    assert t.is_vector() == True
    