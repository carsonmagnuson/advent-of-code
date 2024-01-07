import solve


def test_v():
    start = (1, 1)
    input = [
        [".", ".", ".", ".", "."],
        [".", "S", "-", "7", "."],
        [".", "|", ".", "|", "."],
        [".", "L", "-", "J", "."],
        [".", ".", ".", ".", "."],
    ]
    output = sorted([(1,1), (1,2), (1,3), (2,3), (3,3), (3, 2), (3, 1), (2, 1)])
    assert sorted(solve.v(input, start)) == output

def test_shoelace():
    input = [(1,1), (1,2), (1,3), (2,3), (3,3), (3, 2), (3, 1), (2, 1)]
    assert solve.shoelace(input) == 4

def test_b():
    input = "test4.txt"
    assert solve.b(input) == 4
