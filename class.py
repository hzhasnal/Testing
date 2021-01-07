#In main page
class Account:
    def __init__(self, name, age,business,contact):
        self.name = name
        self.age = age
        self.business = business
        self.contact = contact
#Edit functions
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


#Info taken from resgistration
user_1 = Account('test_user_1','20','Manufacturing','07352092345')
user_1.display()
Edit = input('Would you like to edit your information? y/n: ') 


while Edit != 'y' and Edit != 'n':
    print('Please enter a suitable response')
    Edit = input('Would you like to edit your information? y/n: ') 

if Edit == 'y':
    #Edit name
    Name = input('Edit name: ')
    user_1.edit_name(Name)
    user_1.display()

    #Edit age
    Age = input('Edit age: ')
    user_1.edit_age(Age)
    user_1.display()