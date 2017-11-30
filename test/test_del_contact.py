from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="111222333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl",
                               email3="jan.kowalski3@test.pl", byear="1985",
                               address2="test secondary address", phone2="45566677", notes="test notes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

