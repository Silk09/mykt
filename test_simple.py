def test_addition():
    assert 1 + 1 == 2


def test_quadratic_discriminant():
    a, b, c = 2, -3, 1
    discriminant = b * b - 4 * a * c
    assert discriminant == 1

    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    assert root1 == 1.0
    assert root2 == 0.5

def test_addition():
    assert 1 + 1 == 2


def test_addition():
    assert 1 + 1 == 2

