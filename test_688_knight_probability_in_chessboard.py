from code_688_knight_probability_in_chessboard import Solution

def test_example_1():
    s = Solution()
    n=3
    k=2
    row=0
    column=0
    output = 0.06250
    assert s.knightProbability(n,k,row,column) == output

def test_example_2():
    s = Solution()
    n=1
    k=0
    row=0
    column=0
    output = 1
    assert s.knightProbability(n,k,row,column) == output

def test_example_3():
    s = Solution()
    n=3
    k=3
    row=0
    column=0
    output = 0.015625
    assert s.knightProbability(n,k,row,column) == output