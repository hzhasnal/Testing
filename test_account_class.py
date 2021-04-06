
import Account_class
from Account_class import *
import pytest

user_1 = Account('test_user_1','20','Manufacturing','07352092345')

#display
print(user_1.display_info)

def test_edit_name():
    edited_name = user_1.edit_name('none')
    assert edited_name == 'none'

def test_edit_age():
    edited_age = user_1.edit_age('27')
    assert edited_age == '27'

def test_edit_business():
    edited_business = user_1.edit_business('Luxury_goods')
    assert edited_business == 'Luxury_goods'

def test_edit_contact():
    edited_contact = user_1.edit_contact('12345678910')
    assert edited_contact == '12345678910'

def test_delete_name():
    deleted_name = user_1.delete_name()
    assert deleted_name == None

def test_delete_contact():
    deleted_contact = user_1.delete_contact()
    assert deleted_contact == None

def test_display_info():
    displayed_info = user_1.display_info
    assert displayed_info == 'Name:test_user_1\nAge:20\nField of Business:Manufacturing\nContact number:07352092345'