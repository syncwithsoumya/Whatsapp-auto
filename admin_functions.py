"""
Admin process controller

"""


def admin_menu():
    menu = """
    Hello Admin ! I can help you with the below options
    1. Troubleshooting Status
    2. Add Customer
    3. Delete Customer
    4. Modify Customer
    5. Escalate product issue
    """
    return menu


def admin_response_code_valid(service=None):
    data = str(service.lower()).split(" ")
    print data
    if len(data) >= 1:
        for i in range(0, len(data)):
            print data[i] in ['menu', 'Menu', ]
            if data[i] in ['menu', 'Menu', ]:
                response = admin_menu()
                break
            elif i == len(data) - 1:
                response = admin_selected_service(service)
    elif service in ['1', '2', '3', '4', '5'] or service.lower().startswith("ref") or service.lower().startswith("Add-")\
            or service.lower().startswith("Del-") or service.lower().startswith("Mod-"):
        response = admin_selected_service(service)
    else:
        response = 'Please type "Menu"(without quotes)'
    return response


def admin_selected_service(service=None):
    ref_no = service.lower().startswith("ref")
    add_flag = service.lower().startswith("add-")
    del_flag = service.lower().startswith("del-")
    mod_flag = service.lower().startswith("mod-")
    if service == '1' or ref_no:
        response = troubleshooting_status(service)
    elif service == '2' or add_flag:
        response = add_customer(service)
    elif service == '3' or del_flag:
        response = del_customer(service)
    elif service == '4' or mod_flag:
        response = mod_customer(service)
    elif service == '5':
        response = escalate()
    else:
        response = 'Incorrect Response Code. Please try again'
    return response


def troubleshooting_status(ref=None):
    if ref == '1':
        return "Please share your ref number"
    else:
        return "Your reference number is under process."


def add_customer(text=None):
    if text == '2':
        return "Please type \"Add-\",\"Number\",\"Username\",\"Purpose\",\"Existing\""
    else:
        return "Added Successfully"


def del_customer(text=None):
    if text == '2':
        return "Please type \"Del-\",\"Number\",\"Username\",\"Purpose\",\"Existing\""
    else:
        return "Deleted Successfully"


def mod_customer(text=None):
    if text == '2':
        return "Please type \"Mod-\",\"Number\",\"Username\",\"Purpose\",\"Existing\""
    else:
        return "Modified Successfully"


def escalate():
    return "It's done !"
