from model.contact import Contact
from random import randrange


def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="111222333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", email3="jan.kowalski3@test.pl", byear="1985",
                               address2="test secondary address", phone2="45566677", notes="test notes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(title="New title")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# The test will be parametrized in next lessons group
# def test_modify_contact_company(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
#                                title="Test title", company="Test company", address="test address",
#                                home="+12 111 222 333", mobile="111222333", work="777888999", fax="",
#                                email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", byear="1985",
#                                address2="test secondary address", phone2="", notes="test notes"))
#     app.contact.modify_first_contact(Contact(company="New company"))

