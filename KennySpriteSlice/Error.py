# Kenny Sprite Sheet Slicer
# Error.py
# Copyright Will Blankenship 2015


class Error(Exception):

    def __init__(self, message):
        self.message = message
