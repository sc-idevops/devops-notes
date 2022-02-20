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
            phone TEXT NOT NULL UNIQUE,
            health INTEGER NOT NULL
            );
            """
        database_cursor.execute(create_table_sql_statement)
    except Exception as e:
        print(e)

    try:
        create_table_sql_statement = """
            CREATE TABLE special_powers (
            power_id INTEGER PRIMARY KEY,
            contact_id INTEGER NOT NULL,
            power_name TEXT NOT NULL,
            power_description TEXT NOT NULL,
            power_dmg TEXT NOT NULL
            );
            """
        database_cursor.execute(create_table_sql_statement)
    except Exception as e:
        print(e)

    return database_cursor

@app.route('/damage_person', methods=['GET'])
def damage_person():
    query_parameters = request.args
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()

    damage_from_id = query_parameters.get("damage_from_id")
    damage_to_id = query_parameters.get("damage_to_id")

    """
    how to call api and use for testing.
    http://127.0.0.1:8000/damage_person?damage_from_id=1&damage_to_id=2
    """

    sql_statement = "SELECT power_dmg FROM special_powers WHERE contact_id='{damage_from_id}';".format(damage_from_id=damage_from_id)
    database_cursor.execute(sql_statement)
    power_dmg = int(database_cursor.fetchone()[0])

    sql_statement = "SELECT health FROM contacts WHERE contact_id='{damage_to_id}';".format(damage_to_id=damage_to_id)
    database_cursor.execute(sql_statement)
    damaged_player_health = int(database_cursor.fetchone()[0])
    damaged_player_health = damaged_player_health - power_dmg
    new_current_player_health = damaged_player_health
    print(new_current_player_health)

    sql_statement = "UPDATE contacts set health='{health}' WHERE contact_id='{damage_to_id}';".format(damage_to_id=damage_to_id, health=new_current_player_health)
    database_cursor.execute(sql_statement)
    connection.commit()

    return "damaged"

@app.route('/save_power', methods=['GET'])
def save_power():
    query_parameters = request.args
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()

    contact_id = query_parameters.get("contact_id")
    power_name = query_parameters.get("power_name")
    power_description = query_parameters.get("power_description")
    power_dmg = query_parameters.get("power_dmg")


    """
    how to call api and use for testing.
    http://127.0.0.1:8000/save_power?contact_id=1&power_name=Midas&power_description=turn to gold&power_dmg=5
    """

    database_cursor.execute('''INSERT INTO special_powers(contact_id, power_name, power_description, power_dmg) VALUES ('{contact_id}', '{power_name}', '{power_description}', '{power_dmg}')'''.format(contact_id=contact_id, power_name=power_name, power_description=power_description, power_dmg=power_dmg))
    connection.commit()
    return "saved"

@app.route('/get_powers/', methods=['GET'])
def get_powers():
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()
    sql_statement = "SELECT * FROM special_powers;"
    database_cursor.execute(sql_statement)
    all_data_from_cursor = database_cursor.fetchall()
    length_of_contacts = (len(all_data_from_cursor))
    json_dictoionary = { "results": [] }
    for power in all_data_from_cursor:
        id = power[0]
        contact_id = power[1]
        power_name = power[2]
        power_desc = power[3]
        power_dmg = power[4]

        try:
            sql_statement = "SELECT first_name FROM contacts WHERE contact_id='{contact_id}';".format(contact_id=contact_id)
            database_cursor.execute(sql_statement)
            first_name = database_cursor.fetchone()[0]
            json_dictoionary["results"].append({"id": id, "contact_id": contact_id, "power_description":power_desc, "power_dmg": power_dmg, "contact_name": str(first_name), "power_name": power_name})
        except Exception as e:
            first_name = str(e)
            json_dictoionary["results"].append({"id": id, "contact_id": contact_id, "power_description":power_desc, "power_dmg": power_dmg, "contact_name": str(first_name), "power_name": power_name})

    return json.dumps(json_dictoionary)

@app.route('/save_contact', methods=['GET'])
def save_contact():
    query_parameters = request.args
    connection = create_connection("pythonsqlite.db")
    database_cursor = connection.cursor()

    first_name = query_parameters.get("first_name")
    last_name = query_parameters.get("last_name")
    email = query_parameters.get("email")
    phone = query_parameters.get("phone")
    health = query_parameters.get("health")

    print(first_name,last_name,email,phone,health)

    """
    http://127.0.0.1:8000/get_contacts/
    http://127.0.0.1:8000/save_contact?first_name=Grant&last_name=Zukel&email=grant.zukel@gmail.com&phone=7029855372&health=100
    """

    database_cursor.execute('''INSERT INTO contacts(first_name, last_name, email, phone, health) VALUES ('{first_name}', '{last_name}', '{email}', '{phone}', '{health}')'''.format(first_name=first_name,last_name=last_name,email=email,phone=phone, health=health))
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
        print(contact)
        id = contact[0]
        first_name = contact[1]
        last_name = contact[2]
        email = contact[3]
        phone = contact[4]
        health = contact[5]
        json_dictoionary["results"].append({"id": id, "first_name": first_name, "last_name":last_name, "email": email, "phone": phone, "health": health})

    return json.dumps(json_dictoionary)

if __name__ == '__main__':
    print("test")
    connection = create_connection("./pythonsqlite.db")
    database_cursor = connection.cursor()
    database_cursor = create_database(database_cursor)
    connection.close()
    app.run(host='127.0.0.1', port=8000)
