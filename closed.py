closer = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def parse(i):
    stack = []
    for idx, c in enumerate(i):
        if c in closer.keys():
            stack.append(c)
        else:
            try:
                tail = stack.pop()
            except IndexError:
                return idx
            if closer[tail] != c:
                return idx

if __name__ == "__main__":
    rv = parse('{]')
    assert 1 == rv, '%s != 1' % rv
    assert 4 == parse('({})}()')
    rv = parse('[[(({{{{{{}}}}((((){}[}())))[[[[]]]]}}))]]')
    assert 22 == rv, '%s != 22' % rv

    puzzle = """{{[{{{{}}{{}}}[]}[][{}][({[((
    {{[][()()]}}{[{{{}}}]}))][()]
    {[[{((()))({}(())[][])}][]()]
    }{()[()]}]})][]]}{{}[]}}"""
    print parse(''.join(p.strip() for p in puzzle.splitlines()))
