from unittest import main
from test.tests import *
from colour_runner.runner import *

if __name__ == '__main__':
    runner = ColourTextTestRunner(verbosity=2)
    main(testRunner=runner)
