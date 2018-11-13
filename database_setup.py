"""
Database setup, all calling methods
"""

from db_utilities import *


def add_db_customer(connect=None,name=None,phone=None,existing=None,subscribe='Y'):
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql_add_customer, (default_prefix + name, phone, existing, subscribe))
        connect.commit()
        status = 200
    except Exception as e:
        status = 400
    finally:
        connect.close()
    return status


def del_db_customer(connect=None, name=None):
    print "name={}".format(name)
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql_del_customer, (default_prefix + name))
        connect.commit()
        status = 200
    except Exception as e:
        status = 400
    finally:
        connect.close()
    return status


def mod_db_customer(connect=None,name=None,phone=None,existing=None,subscribe='Y'):
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql_mod_customer, (default_prefix + name, phone, existing, subscribe, default_prefix + name))
        connect.commit()
        status = 200
    except Exception as e:
        status = 400
    finally:
        connect.close()
    return status

