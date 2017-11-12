from model.contact import Contact


def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title="New title"))


def test_modify_contact_company(app):
    app.contact.modify_first_contact(Contact(company="New company"))

