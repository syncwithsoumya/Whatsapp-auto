"""

Database connections
"""
import pymysql as py

# TODO: Setup DB and connect methods


def db_connection():
    conn = py.connect('localhost', user='root', password='Amazon_2020',db='whatsapp')
    return conn



