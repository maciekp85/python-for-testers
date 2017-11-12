from model.contact import Contact


def test_modify_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="New title"))
    app.session.logout()


def test_modify_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="New company"))
    app.session.logout()
