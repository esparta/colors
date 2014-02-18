# -*- encoding: utf-8 -*-
from __future__ import absolute_import
import unittest
from colors import color, strip_color


class Test_Colors(unittest.TestCase):
    """
    Test for Colors module
    """
    def setUp(self):
        """
        Set up the whole test
        """
        pass

    def test_nocolors(self):
        """We should have the original text with no parameters """
        self.assertEqual(color("RED"), "RED")

    def test_redcolor(self):
        """
        Test if we get a correct red
        """
        self.assertEqual(color("RED", foreground="red"), '\x1b[31mRED\x1b[0m')

    def test_error_on_bad_color_string(self):
        """Test if we have an exception with a bad string color """
        with self.assertRaises(Exception):
            color("RED", "fushia")

    def test_integer_color(self):
        """Test if we can use a integer as a color """
        self.assertEqual(color("RED", 1), '\x1b[38;5;1mRED\x1b[0m')

    def test_error_on_bad_color_int(self):
        """Test if we have an exception with a bad color number """
        with self.assertRaises(Exception):
            color("RED", 911)

    def test_background_color(self):
        """Test the background color with string """
        self.assertEqual(color("RED", background="red"), '\x1b[41mRED\x1b[0m')

    def test_style_color(self):
        """Test the style with a string """
        self.assertEqual(color('BOLD', style='bold'), '\x1b[1mBOLD\x1b[0m')

    def test_error_setting_style_color(self):
        """Test if we have an exception setting the style """
        with self.assertRaises(Exception):
            color("BOLD", style="MAYUSCULAS")

    def test_error_on_bad_color_notint(self):
        """Test if we have an exception with a bad color number """
        with self.assertRaises(Exception):
            color("RED", 911.11)

    def test_error_on_bad_style(self):
        """Test if we have an exception with a bad color number """
        with self.assertRaises(Exception):
            color("RED", background="cursivas")

    def test_remove_color(self):
        """ We can get the original message without the colors """
        self.assertEqual(strip_color(color("RED", "red")), "RED")


