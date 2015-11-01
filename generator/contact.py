from model.contact import Contact
from generator.random import random_string
import getopt
import sys
import os
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata= [Contact(firstname="", middlename="", lastname="")] + [
   Contact(firstname=random_string("fname", 15), middlename=random_string("mname", 15), lastname=random_string("lname", 15))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
