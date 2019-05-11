#!/usr/bin/python

import sys

class Main():

    def __init__(self):
        self._user_input = None

    def read_user_input(self, user_input):
        self._user_input = user_input

    def get_user_input(self):
        return self._user_input

    def main(self):
        # takes the first argument given
        user_input = sys.argv[1]
        self.read_user_input(user_input)
        print(user_input)

if __name__ == '__main__':
    Main().main()
