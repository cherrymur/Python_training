from model.contact import Contact
import jsonpickle
import os.path
import random
import string
import getopt
import sys


# parameter for current script
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["numbers of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
               Contact(firstname="", middlename="", lastname="", nickname="", title="",
                       company="", address="", homephone="", mobilephone="", workphone="",
                       faxphone="", email="", email2="", email3="", homepage="", address2="",
                       secondaryphone="", notes="")
           ] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 10), company=random_string("company", 10),
                       address=random_string("address", 10),
                       homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
                       workphone=random_string("workphone", 10), faxphone=random_string("faxphone", 10),
                       email=random_string("email", 10), email2=random_string("email2", 10),
                       email3=random_string("email3", 10),
                       homepage=random_string("homepage", 10), address2=random_string("address2", 10),
                       secondaryphone=random_string("secondaryphone", 10), notes=random_string("notes", 10))
               for i in range(5)
           ]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) # file.json создание файла

with open(file_path, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata)) # changed to pinckle because we want to generate from .json file .py file