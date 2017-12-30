import re
from random import randrange
from model.contact import Contact


def test_random_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="111222333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", email3="jan.kowalski3@test.pl", byear="1985",
                               address2="test secondary address", phone2="45566677", notes="test notes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contacts_list_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="111222333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", email3="jan.kowalski3@test.pl", byear="1985",
                               address2="test secondary address", phone2="45566677", notes="test notes"))
    old_contacts = db.get_contact_list()
    for contact in old_contacts:
        contact_from_database = contact
        contact_from_home_page = app.contact.get_contact_info_from_home_page(contact)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact)
        assert contact_from_home_page.firstname == contact_from_database.firstname
        assert contact_from_home_page.lastname == contact_from_database.lastname
        assert contact_from_home_page.address == contact_from_database.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_database)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_database)
        assert contact_from_edit_page.firstname == contact_from_database.firstname
        assert contact_from_edit_page.lastname == contact_from_database.lastname
        assert contact_from_edit_page.address == contact_from_database.address
        assert merge_phones_like_on_home_page(contact_from_edit_page) == merge_phones_like_on_home_page(contact_from_database)
        assert merge_emails_like_on_home_page(contact_from_edit_page) == merge_emails_like_on_home_page(contact_from_database)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
