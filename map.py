import sys
map = [
    [8,8,4,4,'^'],
    [4,9,6,4,8],
    [8,6,4,1,2],
    [4,8,2,6,3],
    ['*',6,8,8,4],
]

def safe_index(x, y):
    if any(v < 0 for v in (x, y)):
        return None
    try:
        return map[x][y]
    except IndexError:
        return None

def surround(x, y):
    return [
        ('n', x - 1, y),
        ('e', x, y + 1),
        ('s', x + 1, y),
        ('w', x, y - 1),
    ]

def search(x, y, coins, path):
    cost = safe_index(x, y)
    if not cost:
        return
    if isinstance(cost, int):
        coins -= cost
        if coins < 5:
            return
    else:
        if cost == '^':
            if coins == 5:
                print path
                return True
            else:
                return False
    for d, x, y in surround(x, y):
        sub_path = list(path) + [d]
        if search(x, y, coins, sub_path):
            return True

def test_search():
    assert True == search(0, 4, 5, [])
    assert True == search(0, 3, 9, [])
    assert True == search(1, 4, 13, [])

if __name__ == "__main__":
    # test_search()
    assert True == search(4, 0, 35, [])

