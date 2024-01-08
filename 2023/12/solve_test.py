import solve

def test_parse():
    """Test parsing function"""
    output = solve.parse("test1.txt")
    assert output == [
        ("???.###", [1, 1, 3]),
        (".??..??...?##.", [1, 1, 3]),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6]),
        ("????.#...#...", [4, 1, 1]),
        ("????.######..#####.", [1, 6, 5]),
        ("?###????????", [3, 2, 1]),
    ]


def test_perms():
    """Test permutations function"""
    output = solve.perms("??..??...?##.", [1,1,3])
    assert output == 4

def test_a():
    """Test part A solution"""
    output = solve.a("test1.txt")
    assert output == 21
