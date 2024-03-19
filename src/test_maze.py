import unittest
from maze import Maze

class TestMaze(unittest.TestCase):

    def test_create_cells_given_positive_int_dimensions_should_exist(self):
        # Given
        num_rows = 12
        num_cols = 10
        # When
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Then
        self.assertEqual(num_rows, len(maze._cells[0]))
        self.assertEqual(num_cols, len(maze._cells))

    def test_create_cells_given_zero_dimensions_should_be_empty(self):
        # Given
        num_rows = 0
        num_cols = 0
        # When
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Then
        self.assertEqual(0, len(maze._cells))
    
    def test_create_cells_given_negative_int_dimensions_should_raise_value_error(self):
        self.assertRaises(ValueError, lambda : Maze(0, 0, -1, 0, 10, 10))
        self.assertRaises(ValueError, lambda : Maze(0, 0, 0, -1, 10, 10))
