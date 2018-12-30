import os
import jpype as jp

class StartReporting():
    #set classpath
    classpath = os.pathsep.join(("lib/bson-3.3.0.jar", "lib/extentreports-2.41.2.jar", "lib/freemarker-2.3.23.jar","lib/jsoup-1.9.2.jar","lib/mongodb-driver-3.3.0.jar","lib/mongodb-driver-core-3.3.0.jar","lib/sqlite-jdbc-3.8.11.1.jar"))
    #start JVM
    jp.startJVM(jp.getDefaultJVMPath(),"-ea", "-Djava.class.path=%s" % classpath)
    #store extent function
    ExtentReports   = jp.JClass('com.relevantcodes.extentreports.ExtentReports')
    ExtentTest      = jp.JClass('com.relevantcodes.extentreports.ExtentTest')
    LogStatus       = jp.JClass('com.relevantcodes.extentreports.LogStatus')
    extent          = ExtentReports("REPORT/Report.html")
