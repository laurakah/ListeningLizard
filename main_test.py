#!/usr/bin/python

import unittest as u
import sys
import main

fake_read_user_input_called = False
fake_read_user_input_arg = None

def fake_read_user_input(user_input):
    global fake_read_user_input_called
    global fake_read_user_input_arg
    fake_read_user_input_called = True
    fake_read_user_input_arg = user_input

class MainTestCase(u.TestCase):

    def setUp(self):
        self.obj = main.Main()

        global fake_read_user_input_called
        fake_read_user_input_called = False
        global fake_read_user_input_arg
        fake_read_user_input_arg = None

    def tearDown(self):
        return


    def test_main_returns_none(self):
        self.assertEqual(self.obj.main(), None)

    def test_main_calls_read_user_input(self):
        self.obj.read_user_input = fake_read_user_input
        self.obj.main()
        self.assertEqual(fake_read_user_input_called, True)

    def test_main_passes_cmd_line_argument_to_read_user_input(self):
        self.obj.read_user_input = fake_read_user_input
        expected = "This is input!"
        sys.argv[1] = expected
        self.obj.main()
        self.assertEqual(fake_read_user_input_arg, expected)

    def test_read_user_input_passes_argument_to_user_input_field(self):
        expected = "Goodbye!"
        self.obj.read_user_input(expected)
        self.assertEqual(self.obj.get_user_input(), expected)


    # get_user_input() returns user input which has already been read

    def test_get_user_input_returns_none_by_default(self):
        self.assertEqual(self.obj.get_user_input(), None)

    def test_get_user_input_returns_user_input_field(self):
        self.obj._user_input = "Hallo!"
        self.assertEqual(self.obj.get_user_input(), "Hallo!")


    # test for making sure that user input state is the same for all tests on init

    def test_xget_user_input_returns_none_by_default(self):
        self.assertEqual(self.obj.get_user_input(), None)

if __name__ == "__main__":
    u.main()
