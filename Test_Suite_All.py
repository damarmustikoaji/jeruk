import unittest
import os
import jpype as jp
from TESTSUITE.Login import login_test

from PUBLIC_FUNCTION import FUNC_LIBRARY

direct = os.getcwd()

class Test_Suite_All(unittest.TestCase):

    driver = FUNC_LIBRARY.function.driver

    def test_Issue(self):

        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(login_test.Login_Test),
            ])

        runner1=unittest.TextTestRunner()
        runner1.run(smoke_test)

    def tearDown(self):
        #shutdown JVM
        jp.shutdownJVM()
        Test_Suite_All.driver.quit()

if __name__ == '__main__':
    unittest.main()
