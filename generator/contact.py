from model.contact import Contact
import jsonpickle
import random
import string
import getopt
import sys
import os.path

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
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
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_numbers():
    return random.randint(100000000000, 999999999999)


def random_fax():
    return random.randint(100000, 999999)


def random_year():
    return random.choice(range(1950, 2001))


#####################
# generating emails
#####################


domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def random_emails(length):
    return get_random_name(letters, length) + '@' + get_random_domain(domains)


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                                   title="", company="", address="",
                                   home="", mobile="", work="", fax="",
                                   email="", email2="", email3="", byear="",
                                   address2="", phone2="", notes="")] + [

    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 20), nickname=random_string("nickname", 10),
            title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 10),
            home=random_phone_numbers(), mobile=random_phone_numbers(), work=random_phone_numbers(), fax=random_fax(),
            email=random_emails(7), email2=random_emails(7), email3=random_emails(7), byear=random_year(),
            address2=random_string("address2: ", 10), phone2=random_phone_numbers(), notes=random_string("notes: ", 10))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
