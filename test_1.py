import Account_class
import pytest

def test_edit_name():
    edited_name = Account_class.user_1.edit_name(John)
    assert edited_name == 'John'

    

