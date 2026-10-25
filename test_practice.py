"""
Unit Tests for Practice Exercises
---------------------------------
Teammates can practice running automated unit tests with:
    python -m unittest test_practice.py
"""

import unittest
from practice_kibo_math import calculate_distance
from exercise_3_coordinate_printer import compute_bounding_box

class TestPracticeMath(unittest.TestCase):

    def test_euclidean_distance_zero(self):
        p1 = (1.0, 2.0, 3.0)
        p2 = (1.0, 2.0, 3.0)
        self.assertAlmostEqual(calculate_distance(p1, p2), 0.0, places=6)

    def test_euclidean_distance_known(self):
        p1 = (0.0, 0.0, 0.0)
        p2 = (3.0, 4.0, 0.0)
        self.assertAlmostEqual(calculate_distance(p1, p2), 5.0, places=6)

    def test_bounding_box(self):
        pts = [(0.0, 1.0, 2.0), (5.0, -1.0, 3.0)]
        bbox = compute_bounding_box(pts)
        self.assertEqual(bbox["x_range"], (0.0, 5.0))
        self.assertEqual(bbox["y_range"], (-1.0, 1.0))
        self.assertEqual(bbox["z_range"], (2.0, 3.0))

if __name__ == "__main__":
    unittest.main()
