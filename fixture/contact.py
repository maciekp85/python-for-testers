from selenium.webdriver.support.select import Select

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

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # select group
        self.select_group_by_name(group)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_group(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("new_group"))
        options = select.options
        if len(options) > 1:
            select.select_by_value(options[1].get_attribute("value"))

    def select_group_by_name(self, group):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("new_group"))
        options = select.options
        if len(options) > 1:
            select.select_by_visible_text(group.name)

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
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=first_name, middlename="", lastname=last_name, nickname="janek", address=address,
                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, title="Test title", company="Test company",
                             fax="", byear="1985", address2="test secondary address", notes="test notes", id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_element_by_xpath("//input[@id='" + contact.id + "']/parent::td/parent::tr")
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        secondaryaddress = wd.find_element_by_name("address2").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstemail = wd.find_element_by_name("email").get_attribute("value")
        secondemail = wd.find_element_by_name("email2").get_attribute("value")
        thirdemail = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       address2=secondaryaddress, home=homephone, work=workphone, mobile=mobilephone,
                       phone2=secondaryphone, email=firstemail, email2=secondemail, email3=thirdemail)

    def get_contact_info_from_edit_page(self, contact):
        wd = self.app.wd
        self.open_contact_to_edit(contact)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        secondaryaddress = wd.find_element_by_name("address2").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstemail = wd.find_element_by_name("email").get_attribute("value")
        secondemail = wd.find_element_by_name("email2").get_attribute("value")
        thirdemail = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       address2=secondaryaddress, home=homephone, work=workphone, mobile=mobilephone,
                       phone2=secondaryphone, email=firstemail, email2=secondemail, email3=thirdemail)

    def get_contact_info_from_home_page(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        for row in wd.find_elements_by_xpath("//input[@id='" + contact.id + "']/parent::td/parent::tr"):
            cells = row.find_elements_by_xpath("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("id")
            last_name = cells[1].text
            first_name = cells[2].text
            address = cells[3].text
            all_emails = cells[4].text
            all_phones = cells[5].text
        return Contact(firstname=first_name, middlename="", lastname=last_name, nickname="janek", address=address,
                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, title="Test title", company="Test company",
                             fax="", byear="1985", address2="test secondary address", notes="test notes", id=id)

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
