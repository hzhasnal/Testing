#This is the code for the account class
#written by harith zahrin bin hasnal
#The code below is for the user to edit information about themselves

class Account:
    def __init__(self, name, age,business,contact):
        self.name = name
        self.age = age
        self.business = business
        self.contact = contact
#edit information
    def edit_name(self, name):
        'setting the name'
        self.name = name
        return self.name
        
    def edit_age(self, age):
        'setting the age'
        self.age = age
        return self.age
        
    def edit_business(self, business):
        'edit the business type'
        self.business = business
        return self.business
    
    def edit_contact(self, contact):
        'edit contact number'
        self.contact = contact
        return self.contact

    def delete_name(self):
        'delete the name'
        self.name = None
        return self.name
    
    def delete_contact(self):
        'delete the contact'
        self.contact = None
        return self.contact

    def delete_age(self):
        'delete the age'
        self.age = None
        return self.age


#display information
    @property
    def display_info(self):
        #'display all information of account'
       display = 'Name:{}\nAge:{}\nField of Business:{}\nContact number:{}'.format(self.name,self.age,self.business,self.contact)
       return display
    
#user_1 = Account('test_user_1','20','Manufacturing','07352092345')

#user_1.delete_age()
#print(user_1.display_info)