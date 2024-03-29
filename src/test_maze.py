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
        self.assertEqual(num_rows, len(maze._cells))
        self.assertEqual(num_cols, len(maze._cells[0]))

    def test_create_cells_given_zero_dimensions_should_be_empty(self):
        # Given
        num_rows = 0
        num_cols = 0
        # Then
        self.assertRaises(ValueError, lambda : Maze(0, 0, num_rows, num_cols, 10, 10))
    
    def test_create_cells_given_negative_int_dimensions_should_raise_value_error(self):
        # Given
        num_rows = -1
        num_cols = -1
        self.assertRaises(ValueError, lambda : Maze(0, 0, num_rows, 0, 10, 10))
        self.assertRaises(ValueError, lambda : Maze(0, 0, 0, num_cols, 10, 10))

    def test_break_entrance_and_exit(self):
        # Given
        num_rows = 2
        num_cols = 2
        # When
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Then
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_rows-1][num_cols-1].has_bottom_wall)

    def test_remove_cells_visited(self):
        # Given
        num_rows = 12
        num_cols = 10
        # When
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Then
        for i in range(0, len(maze._cells)):
            for j in range(0, len(maze._cells[i])):
                self.assertFalse(maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()