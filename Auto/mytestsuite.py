import unitestdemo
import unittest
#
# mysuite = unittest.TestSuite()
# mysuite.addTest(unitestdemo.MyTestCase("test_something"))
# mysuite.addTest(unitestdemo.MyTestCase("test_other"))

cases = unittest.TestLoader().loadTestsFromTestCase(unitestdemo.MyTestCase)
mysuite = unittest.TestSuite([cases])
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)