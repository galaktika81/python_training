__author__ = 'galyna'


from test.test_phone import merge_phones_like_on_home_page
from model.contact import Contact

def test_contacts_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert(len(contacts_from_home_page) == len(contacts_from_db))
    contacts_from_home_page.sort(key=Contact.id_or_max)
    contacts_from_db.sort(key=Contact.id_or_max)
    for c in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[c].firstname == contacts_from_db[c].firstname
        assert contacts_from_home_page[c].lastname == contacts_from_db[c].lastname
        assert contacts_from_home_page[c].address == contacts_from_db[c].address
        assert contacts_from_home_page[c].all_emails==merge_emails_like_on_home_page(contacts_from_db[c])
        assert contacts_from_home_page[c].all_phones_from_home_page==merge_phones_like_on_home_page(contacts_from_db[c])


# def test_contact_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3])))
