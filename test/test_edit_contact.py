from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Edit Jan", middlename="Edit middlename", lastname="Edit Kowalski", nickname="edit janek",
                               title="Edit Test title", company="edit Test company", address="edit test address",
                               home="", mobile="", work="", fax="",
                               email="jan.edit@test.pl", email2="jan.edit2@test.pl", byear="2005",
                               address2="edit test secondary address", phone2="", notes="edit test notes"))
    app.session.logout()
