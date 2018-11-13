"""
Admin process controller

"""
from database_setup import *
from database_connection import *


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
    elif service in ['1', '2', '3', '4', '5'] or service.lower().startswith("ref") or service.lower().startswith("add-")\
            or service.lower().startswith("del-") or service.lower().startswith("mod-"):
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
        response = add_customer(service,connect=db_connection())
    elif service == '3' or del_flag:
        response = del_customer(service,connect=db_connection())
    elif service == '4' or mod_flag:
        response = mod_customer(service,connect=db_connection())
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


def add_customer(text=None,connect=None):
    if text == '2':
        return "Please type \"Add-\"Number\",\"Username\",\"Existing\" E.g. Add-1234567890,xyz,n"
    else:
        data= str(text.split("-")[1]).split(",")
        print "data->{}" .format(data)
        name= str(data[1]).replace(" ", "")
        no= str(data[0]).replace(" ", "")
        exist = str(data[2]).replace(" ", "")
        print "--{},{},{}".format(name,no,exist)
        status = add_db_customer(connect=connect, name=name,phone=no,existing=exist)
        if status == 200:
            return "Added Successfully"
        else:
            return "There is some issues. Try again !"


def del_customer(text=None, connect=None):
    if text == '3':
        return "Please type \"Del-\"Username\" E.g. Del-xyz"
    else:
        data = text.split("-")
        print data
        name = str(data[1]).replace(" ", "")
        print "name-{}".format(name)
        status = del_db_customer(connect=connect,name=name)
        if status == 200:
            return "Deleted Successfully"
        else:
            return "There is some issues. Try again !"


def mod_customer(text=None, connect=None):
    if text == '4':
        return "Please type \"Mod-\"Number\",\"Username\",\"Existing\" E.g. Mod-1234567890,xyz,n"
    else:
        data = str(text.split("-")[1]).split(",")
        print data
        name = str(data[1]).replace(" ", "")
        no = str(data[0]).replace(" ", "")
        exist = str(data[2]).replace(" ", "")
        status = mod_db_customer(connect=connect,name=name, phone=no, existing=exist)
        if status == 200:
            return "Modified Successfully"
        else:
            return "There is some issues. Try again !"


def escalate():
    return "It's done !"
