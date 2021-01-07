class Account:
    def __init__(self, name, age,business,contact):
        self.name = name
        self.age = age
        self.business = business
        self.contact = contact

    def edit_name(self, name):
        'setting the name'
        self.name = name
        
    def edit_age(self, age):
        'setting the age'
        self.age = 'age'
        
    def edit_business(self, business):
        'edit the business type'
        self.business = 'business'

    def display(self):
        #'display all information of account'
        print( 'Name:{}\nAge:{}\nField of Business:{}\nContact number:{}'.format(self.name,self.age,self.business,self.contact))

    

    
user_1 = Account('test_user_1','20','Manufacturing','07352092345')

user_1.edit_name('Jack')
user_1.display()
