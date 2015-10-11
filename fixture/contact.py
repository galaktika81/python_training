__author__ = 'galyna'

from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def modify_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name]"):
                contact = element.find_elements_by_css_selector('td')
                firstname = contact[2].text
                lastname = contact[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)