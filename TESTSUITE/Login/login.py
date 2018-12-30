from TESTSUITE.Login import object_repository
from PUBLIC_FUNCTION import FUNC_LIBRARY

class Login(object):
    """docstring for Login."""
    obj     = object_repository.Object_Repository
    func    = FUNC_LIBRARY.function

    def Login(self, driver, test, LogStatus):
        driver  = driver
        Login.func.wait_XPATH(self, driver, Login.obj.login, test, LogStatus, "Waiting element "+Login.obj.login)
        Login.func.click_XPATH(self, driver, Login.obj.login, test, LogStatus, "Click element "+Login.obj.login)
        Login.func.wait_XPATH(self, driver, Login.obj.form, test, LogStatus, "Waiting element "+Login.obj.form)

    def Fill(self, driver, test, LogStatus):
        driver  = driver
        Login.func.fill_XPATH(self, driver, Login.obj.user_data, test, LogStatus, "Fill field "+Login.obj.user_data, "damar")
        Login.func.fill_XPATH(self, driver, Login.obj.password, test, LogStatus, "Fill field "+Login.obj.password, "123qwe")

    def LoginProcess(self, driver, test, LogStatus):
        driver  = driver
        Login.func.click_XPATH(self, driver, Login.obj.loginbtn, test, LogStatus, "Click element "+Login.obj.loginbtn)

    def Alert(self, driver, test, LogStatus):
        driver  = driver
        Login.func.wait_XPATH(self, driver, Login.obj.alert, test, LogStatus, "Waiting element "+Login.obj.alert)
        Login.func.get_text_XPATH(self, driver, Login.obj.alert, test, LogStatus, "")
