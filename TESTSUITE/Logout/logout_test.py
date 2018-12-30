import unittest
import time

from PUBLIC_FUNCTION import FUNC_LIBRARY, variables, StartReporting

from TESTSUITE.Login import login

class Login_Test(unittest.TestCase):
    login           = login.Login
    report_test     = StartReporting.StartReporting

    #store extent function
    LogStatus       = report_test.LogStatus
    extent          = report_test.extent
    parent          = extent.startTest("Login Testcase")

    #setup
    def setUp(self):
        #declare to use Firefox
        self.driver = FUNC_LIBRARY.function.driver
        #make variable for easy access
        driver      = self.driver
        #maximize Firefox
        #driver.maximize_window()
        #go to url
        driver.get(variables.Variables.SERVER)

    #report_test_ALL login test
    test1      = extent.startTest("Login with empty field")
    def test_001_login(self):
        LogStatus = Login_Test.LogStatus
        #login test
        Login_Test.login.Login(self,self.driver, Login_Test.test1, LogStatus)
        Login_Test.login.LoginProcess(self,self.driver, Login_Test.test1, LogStatus)
        Login_Test.login.Alert(self,self.driver, Login_Test.test1, LogStatus)

    #shutdown jvm
    def test_009_ShutDownJVM(self):
        Login_Test.parent.appendChild(Login_Test.test1)
        Login_Test.extent.endTest(Login_Test.parent);
        #push data to report
        Login_Test.extent.flush()

if __name__ == '__main__':
    unittest.main()
