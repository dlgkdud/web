from sudoku import Sudoku

def test_check_method_if_true():
    sudokus = Sudoku()
    true_board = [
        [4,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
    ]
    assert sudokus.sudoku_check(true_board) == True

def test_check_method_if_false():
    sudokus = Sudoku()
    false_board = [
        [7,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,8,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
    ]
    assert sudokus.sudoku_check(false_board) == False

def test_invalid_size_check():
    sudokus = Sudoku()
    invalid_board = [
        [7,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2]
    ]
    assert sudokus.sudoku_check(invalid_board) == False

def test_invalid_board_int():
    sudokus = Sudoku()
    invalid_board = 1
    assert sudokus.sudoku_check(invalid_board) == False

def test_invalid_board_empty_list():
    sudokus = Sudoku()
    invalid_board = []
    assert sudokus.sudoku_check(invalid_board) == False

def test_invalid_board_float():
    sudokus = Sudoku()
    invalid_board = 0.1
    assert sudokus.sudoku_check(invalid_board) == False

def test_invalid_board_element_not_int():
    sudokus = Sudoku()
    invalid_board = [
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
      [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    ]
    assert sudokus.sudoku_check(invalid_board) == False 