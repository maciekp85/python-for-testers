from model.group import Group


def test_add_contact_to_group(app, json_contacts, orm):
    contact = json_contacts
    group = Group(name="test")
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert orm.check_if_contact_is_in_group(contact, contacts_not_in_group) is False
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert orm.check_if_contact_is_in_group(contact, contacts_in_group) is True
