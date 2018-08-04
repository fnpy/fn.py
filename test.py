#!/usr/bin/env python

import doctest
import unittest

from tests import *

if __name__ == "__main__":

    import tests.test_doctest
    doctest.testmod(tests.test_doctest)

    unittest.main()
