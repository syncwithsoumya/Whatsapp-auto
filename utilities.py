"""

Necessary functions and variables

"""
import sys
mappings = {'3':'4','4':'8','5':'16'}
istacksize = 5000


def get_all_msgs(driver=None):
    return driver.find_elements_by_xpath("//span[@class='selectable-text invisible-space copyable-text']")


def get_specific_msg(position=None,driver=None):
    return driver.find_element_by_xpath(
            "(//span[@class='selectable-text invisible-space copyable-text'])[position()={}]".format(position + 1))


def get_last_recent_msg(driver=None):
    for i in range(0, len(get_all_msgs(driver=driver))):
        msg = get_specific_msg(position=i, driver=driver)
    return msg.text


def put_text(driver=None):
    return driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")


def click_default(driver=None):
    return driver.find_element_by_xpath("//span[contains(text(), 'Bot')]")


def click_notifications(driver=None):
    return driver.find_element_by_xpath("//div[.//span[@class='OUeyt']]/ancestor::div[@class='_3j7s9']")


def get_user_type(driver=None):
    usertype = driver.find_element_by_xpath("//span[@class='_1wjpf']/ancestor::div[@class='_2zCDG']")
    return usertype.text


def load_stack():
    return sys.setrecursionlimit(istacksize)