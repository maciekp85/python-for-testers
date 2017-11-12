from model.contact import Contact


def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="+12 111 222 333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", byear="1985",
                               address2="test secondary address", phone2="", notes="test notes"))
    app.contact.modify_first_contact(Contact(title="New title"))


def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                               title="Test title", company="Test company", address="test address",
                               home="+12 111 222 333", mobile="111222333", work="777888999", fax="",
                               email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", byear="1985",
                               address2="test secondary address", phone2="", notes="test notes"))
    app.contact.modify_first_contact(Contact(company="New company"))

