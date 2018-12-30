class Object_Repository(object):
    """docstring for Object_Repository."""

    #button
    login       = '//button[@id="login-button"]'
    loginbtn    = '//button[@class="sc-kgoBCf hCeJXv" and @type="blue"]'

    #object
    form        = '//div[@class="no-close sc-kAzzGY gHwzRk"]'

    #field
    user_data   = '//input[@name="user_data"]'
    password    = '//input[@name="password"]'

    #alert
    alert       = '//div[@class="sc-kGXeez eoifcZ" and contains(text(), "Username or email is required")]'
