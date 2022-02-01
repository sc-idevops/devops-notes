#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import sqlite3
from sqlite3 import Error
import json

app = Flask(__name__)

def create_connection(db_file_location_and_name):
    try:
        connection = sqlite3.connect(db_file_location_and_name)
        if not connection:
            return None
        return connection
    except Error as e:
        print(e)
        return None

def create_database(database_cursor):
    try:
        create_table_sql_statement = """
            CREATE TABLE contacts (
            contact_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE
            );
            """
        database_cursor.execute(create_table_sql_statement)
        return database_cursor
    except Exception as e:
        print(e)
        return database_cursor

@app.route('/save_contact', methods=['GET'])
def save_contact():
    query_parameters = request.args
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()

    first_name = query_parameters.get("first_name")
    last_name = query_parameters.get("last_name")
    email = query_parameters.get("email")
    phone = query_parameters.get("phone")

    """
    http://127.0.0.1:8000/get_contacts/
    http://127.0.0.1:8000/save_contact?first_name=John&last_name=BadAss2&email=grant.zukel2&phone=7029855372
    ?first_name=John&last_name=BadAss&email=grant.zukel@gmail.com&phone=7029855378
    """

    database_cursor.execute('''INSERT INTO contacts(first_name, last_name, email, phone) VALUES ('{first_name}', '{last_name}', '{email}', '{phone}')'''.format(first_name=first_name,last_name=last_name,email=email,phone=phone))
    connection.commit()
    return "saved"


@app.route('/get_contacts/', methods=['GET'])
def get_contacts():
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()
    sql_statement = "SELECT * FROM contacts;"
    database_cursor.execute(sql_statement)
    all_data_from_cursor = database_cursor.fetchall()
    length_of_contacts = (len(all_data_from_cursor))
    json_dictoionary = { "results": [] }
    for contact in all_data_from_cursor:
        id = contact[0]
        first_name = contact[1]
        last_name = contact[2]
        email = contact[3]
        phone = contact[4]
        json_dictoionary["results"].append({"id": id, "first_name": first_name, "last_name":last_name, "email": email, "phone": phone})


    return json.dumps(json_dictoionary)


if __name__ == '__main__':
    print("test")
    connection = create_connection("./pythonsqlite.db")
    database_cursor = connection.cursor()
    database_cursor = create_database(database_cursor)
    connection.close()

    app.run(host='127.0.0.1', port=8000)