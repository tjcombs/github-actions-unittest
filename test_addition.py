# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:20:16 2020

@author: tjcombs

"""

import unittest
from addition import add_one

class TestMath(unittest.TestCase):
    
    def test_add_one(self):
        # Test that adding one to zero is one
        self.assertEqual(add_one(0), 1)

if __name__ == '__main__':
    unittest.main()