import solve

def test_parse():
    """Testing parsing func."""
    output = solve.parse("test1.txt")
    assert output == [
        [".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", "."]
    ]
def test_empties():
    """Testing function that finds empty rows/cols."""
    output = solve.parse("test1.txt")
    assert solve.empties(output) == ([3, 7], [2, 5, 8])

def test_vertices():
    """Testing galaxy coord function"""
    output = solve.parse("test1.txt")
    assert sorted(solve.vertices(output)) == sorted([(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 0), (9, 4)])

def test_distance():
    """Testing distance function"""
    gal1 = (9, 0)
    gal2 = (9, 4)
    empties = ([3, 7], [2, 5, 8])
    assert solve.distance(gal1, gal2, empties, 1) == 5

def test_a():
    """Testing part A solution"""
    assert solve.a("test1.txt") == 374

def test_b():
    """Testing part B solution"""
    assert solve.b("test1.txt", 100) == 8410
