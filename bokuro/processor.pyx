import codecs
import os

class ReferenceProcessor(object):
    def __init__(self):
        pass

    def read(self, str path):
        with codecs.open(path, 'r') as f:
            raw_lines = f.readlines()
