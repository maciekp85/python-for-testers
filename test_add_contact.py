# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Jan", middlename="", lastname="Kowalski", nickname="janek",
                        title="Test title", company="Test company", address="test address",
                        home="+12 111 222 333", mobile="111222333", work="777888999", fax="",
                        email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", byear="1985",
                        address2="test secondary address", phone2="", notes="test notes"))
    app.logout()
