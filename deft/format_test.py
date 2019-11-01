"""
deft.format_test :: Unit Tests for Deft Formatting
"""

import unittest

from formatting import justify_center


class JustifyTest(unittest.TestCase):
    """Test cases for deft.formatting functions."""

    def test_justify_center(self):
        """Tests if string is justified correctly."""

        w = 16
        sym = "+"
        unjust = """ahoy
there
mateys"""

        just = """++++++ahoy++++++
+++++there++++++
+++++mateys+++++"""

        self.assertEqual(justify_center(unjust, w, sym), just)


if __name__ == "__main__":
    unittest.main()
