from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time
import sys


def check_user_needs():
    menu = """
    Hello ! I can help you with the below options
    1. Lodge a complaint
    2. Check complaint status
    3. Request a callback
    Please only type out the required option and I will assist you. 
    [Note: We may be slow in responding please wait a while before placing 2nd request]
    """
    return menu


def selected_service(service=None):
    bool = service.startswith("REF")
    print bool
    if service == '1':
        num = randint(999,9999)
        response = complaint(num)
    elif service == '2' or bool:
        response = status(service)
    elif service == '3':
        response = callback()
    elif len(service.split(" ")) >= 1:
        for i in range(0,len(service.split(" "))):
            if str(service.split(" ")[i]).lower() in ['issue','issues','problem','problems','help','fix']:
                response = check_user_needs(service)
            else:
                response = "Sorry please say ask me a valid question."
    else:
        response = 'Incorrect Response Code. Please try again'

    return response


def complaint(number=None):
    sample_code = 'REF{}'.format(number)
    msg = "You complaint is filed under Reference Number - {}".format(sample_code)
    return msg


def status(code=None):
    if code == '2':
        return "Please share your ref number"
    else:
        return "Your reference number is under process."


def callback():
    return "Your number is registered and you will receive a callback as soon as possible"


def analyse_text(question=None):
    q_intents = ['what', 'what\'s', 'why','who','who\'re' 'how', 'how\'s', 'whom', 'where', 'which', 'whose', 'when']
    q_obj_intents = ['name', 'age', 'created']
    answers = ['I am :-) Bot.','2 months ;-)','Mr. Soumya ;-)']
    tokens = question.split(" ")
    if tokens[0].lower() in q_obj_intents:
        if "?" in tokens or tokens.lower() in q_intents:
            indx = q_obj_intents.index(tokens[0].lower())
            print indx
            print answers[indx]
            return answers[indx]
    else:
        return '''I am not sure what you are asking for, I am currently in development, 
        Please ask the questions which I can answer.
         Like [hi,hello,how are you ?,what is your age ?,what is your name ?,bye]'''


def send_msg():
    try:

        cc = driver.find_elements_by_xpath("//span[@class='selectable-text invisible-space copyable-text']")
        for i in range(0,len(cc)):
            msg = driver.find_element_by_xpath("(//span[@class='selectable-text invisible-space copyable-text'])[position()={}]".format(i+1))
            # print (msg.text)
        time.sleep(5)
        response = selected_service(str(msg.text))
        id = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
        id.clear()
        id.send_keys(response)
        id.send_keys(Keys.RETURN)
        time.sleep(1)
        clic = driver.find_element_by_xpath("//span[contains(text(), 'Prachi')]")
        # print (clic)
        clic.click()

    except Exception as e:
        # print ("Exception-2")
        sender()


def sender():
    time.sleep(20)
    try:
        e = driver.find_element_by_xpath("//div[.//span[@class='OUeyt']]/ancestor::div[@class='_3j7s9']")
        ac = ActionChains(driver)
        ac.click(e).perform()
        send_msg()
    except:
        # print ("Exception")
        send_msg()


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    while True:
        sender()
