from appium import webdriver
import time

# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'localhost:5555',
#     'appPackage': 'com.example.myapplication',
#     'appActivity': '.MainActivity',
#     'noReset': True
# }

desired_caps = dict()
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'localhost:5555'
desired_caps['appPackage'] = 'com.google.android.calculator'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

# Example interaction: click on digit 7
driver.find_element_by_id('com.google.android.calculator:id/digit_7').click()

# Pause so you can see the action
time.sleep(2)

# Close the session
driver.quit()