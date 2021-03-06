__author__ = 'galyna'

from model.contact import Contact
import re


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

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_by_id(self, id, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php?id='%s'" % id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cache = None

    def select_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_id(id).click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

        if contact.group is not None:
            selectGroup = wd.find_element_by_name('new_group')
            for option in selectGroup.find_elements_by_tag_name('option'):
                if option.text == contact.group.name:
                    option.click()
                    break

    def change_field_value(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(text)

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
                address = contact[3].text

                all_emails = contact[4].text
                all_phones = contact[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                        address=address, all_emails=all_emails, all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        self.__open_contact_by_index_and_mode__(index,7)

    def open_contact_view_by_index(self, index):
        self.__open_contact_by_index_and_mode__(index,6)

    def __open_contact_by_index_and_mode__(self, index, mode):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[mode]
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
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
