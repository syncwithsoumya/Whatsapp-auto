"""

Customer Related functions

"""

from random import randint
from utilities import mappings


def menu():
    menu = """
    Hello ! I can help you with the below options
    1. Service
    2. Complete Setup (DVR + Camera) 
    3. 4 Channel DVR
    4. 8 Channel DVR
    5. 16 Channel DVR
    6. Camera
    7. Request Call Back
    8. Unsubscribe*
    Please only type out the required option(e.g: 1 or 2 or etc) and I will assist you. 
    [Note: I may be slow in responding please wait a while before placing 2nd request]
    [* If You will unsubscribe you will never be communicated from Surela Infotech]
    """
    return menu


def response_code_valid(service=None):
    data = str(service.lower()).split(" ")
    print data
    if len(data) > 1:
        for i in range(0, len(data)):
            print data[i] in ['issue', 'issues', 'problem', 'problems', 'help', 'fix', 'want', 'working']
            if data[i] in ['issue', 'issues', 'problem', 'problems', 'help', 'fix', 'want', 'working']:
                response = menu()
                break
            elif i == len(data) - 1:
                response = selected_service(service)
    elif service in ['1', '2', '3', '4', '5', '6', '7','8'] or service.lower().startswith("ref"):
        response = selected_service(service)
    else:
        response = 'Could n\'t understand you. Please request with texts e.g help me, i need fix or etc..'
    return response


def selected_service(service=None):
    bool = service.lower().startswith("ref")
    print bool
    if service == '1':
        num = randint(999, 9999)
        response = servicing(num)
    elif service == '2':
        response = complete_setup()
    elif service in ['3', '4', '5']:
        mappings[service]
        response = channel_dvr(channel=int(mappings[service]))
    elif service == '6':
        response = camera()
    elif service == '7':
        response = callback()
    else:
        response = 'Incorrect Response Code. Please try again'

    return response


def servicing(number=None):
    sample_code = 'REF{}'.format(number)
    msg = "Your servicing is filed with Reference Number - {}".format(sample_code)
    return msg


def complete_setup():
    doclink = 'www.google.com'
    return "Your complete quotation can be found in the link {}".format(doclink)


def channel_dvr(channel=None):
    if channel == 4:
        doclink = 'www.google.com/4/'
    if channel == 8:
        doclink = 'www.google.com/8/'
    if channel == 16:
        doclink = 'www.google.com/16/'
    return "Your quotation for {} channel can be found in the link {}".format(channel, doclink)


def camera():
    return "Thanks for your interest. We will contact you shortly"


def callback():
    return "Your number is registered and you will receive a callback from our sales team as soon as possible"


def unsubscribe():
    return "You repect your decision. Have a good day :-) !"


