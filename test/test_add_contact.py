import pytest
from model.contact import Contact
import random
import string


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
