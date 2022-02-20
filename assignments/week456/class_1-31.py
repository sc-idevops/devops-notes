#!/usr/bin/env python
# -*- coding: utf-8 -*-

#requests library makes web requests. You have to install with pip.
import requests
#This is included with python install and you use this to do stuff with jsons
import json
import datetime
import os
from faker import Faker
import time

faker = Faker()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)

#string
website_url = "http://127.0.0.1:8000/get_contacts/"

#integer
list_count = 0

#float
list_percentage = 0.0

#list
data_list = []

#dictionary
json_dict_object = {}

first_name = faker.first_name()
last_name = faker.last_name()
phone = faker.phone_number()
email = faker.email()

#.format named string replacement. THIS IS THE WAY I WANT YOU TO DO STRING REPLACEMENT!!!!!!
insertion_payload = "http://127.0.0.1:8000/save_contact?first_name={first_name}&last_name={last_name}&email={email}&phone={phone}&health=100".format(first_name=first_name,
                                                                                                                                          last_name=last_name,
                                                                                                                                          email=email,
                                                                                                                                          phone=phone)

inert_payload = requests.get(insertion_payload)

print("Sleep for 5 seconds wait for insertion.")
time.sleep(5)
#using requests library to call teh .get webrequests method on url. There is also post, put, update, delete
web_request = requests.get(website_url, verify=False)

#used for json endpoints to automatically convert the json string being retrieved in teh web_request object to a python object you can use to look in your debugger.
json_content = web_request.json()

#{"results": [{"id": 1, "first_name": "John", "last_name": "BadAss", "email": "grant.zukel", "phone": "7029855378"}, {"id": 2, "first_name": "John", "last_name": "BadAss2", "email": "grant.zukel2", "phone": "7029855372"}]}
#how to do 4 loop in python
for contact in json_content["results"]:
    first_name_loop = contact["first_name"]
    last_name_loop = contact["last_name"]
    email_loop = contact["email"]
    phone_loop = contact["phone"]
    id_loop = contact["id"]
    if first_name_loop == first_name:
        print(first_name,"value found operation successful")