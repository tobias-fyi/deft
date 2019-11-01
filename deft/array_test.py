"""
deft.array_test :: Unit Tests for Deft Arrays
"""

import unittest

from array import bubble_sort


class TestArrayFuncs(unittest.TestCase):
    """Basic unit tests for array.py functions."""

    def test_bubble_sort(self):
        """Test the bubble_sort function against sorted array."""

        # Unsorted list to sort and compare
        unsorted_list = [10, 5, 20, 6, 3, 7, 5, 2, 8, 890, 56, 3, 26]

        # Create sorted lists using bubble_sort
        # and the built in Python array method
        bubble_sorted = bubble_sort(unsorted_list)
        builtin_sorted = sorted(unsorted_list)

        # Assert that the value at each index of the two are equal
        for i in range(len(builtin_sorted)):
            with self.subTest(i=i):
                self.assertEqual(bubble_sorted[i], builtin_sorted[i])


if __name__ == "__main__":
    unittest.main()
