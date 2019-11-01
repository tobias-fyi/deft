"""
deft.format_test :: Unit Tests for Deft Formatting
"""

import unittest

from deftools import DeftString


class TestDeftStrings(unittest.TestCase):
    """Unit tests for deft.DeftString."""

    def test_caps_ratio(self):
        """Simple test of capitalization ratio calculation."""

        test_string = "Hello World!"
        hand_calc = round(2 / 12, 6)

        self.assertAlmostEqual(DeftString(test_string).caps_ratio(), hand_calc)


if __name__ == "__main__":
    unittest.main()
