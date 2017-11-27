from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_id("maintable")) > 0:
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_id("maintable")) > 0:
            wd.find_element_by_link_text("home page").click()

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("edit.php"):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        # submit edition for contact with a random index
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        # select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm choice with popup dialog box
        wd.switch_to_alert().accept()
        self.go_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_xpath("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=first_name, middlename="", lastname=last_name, nickname="janek",
                                   title="Test title", company="Test company", address="test address",
                                   home=all_phones[0], mobile=all_phones[1], work=all_phones[2], fax="",
                                   email="jan.kowalski@test.pl", email2="jan.kowalski2@test.pl", byear="1985",
                                   address2="test secondary address", phone2=all_phones[3], notes="test notes", id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=homephone, work=workphone, mobile=mobilephone,
                       phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone, phone2=secondaryphone)
