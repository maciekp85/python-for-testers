from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit test name", header="edit header name", footer="edit footer name"))
    app.session.logout()
