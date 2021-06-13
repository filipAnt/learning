"""Class exercises - book instructions for programmer 9.1 ->"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is {self.name.title()}.')
        print(f'Restaurant is serving {self.cuisine} cuisine.')

    def open_restaurant(self):
        print(f'Restaurant {self.name} is open from 8 AM to 19 PM')

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers


my_restaurant = Restaurant('Hong-ha', 'chinese')
# print(my_restaurant.number_served)
# my_restaurant.number_served = 5
# print(my_restaurant.number_served)
restaurant_1 = Restaurant('KebabMAX', 'turkish')
# restaurant_1.set_number_served(10)
# print(restaurant_1.number_served)
restaurant_2 = Restaurant('Pizza', 'italian')


# restaurant_2.increment_number_served(3)
# restaurant_2.increment_number_served(8)
# restaurant_2.increment_number_served(1)
# print(restaurant_2.number_served)


# my_restaurant.describe_restaurant()
# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# my_restaurant.open_restaurant()

class User():
    def __init__(self, first_name, last_name, email_address, login):
        self.name = first_name
        self.surname = last_name
        self.email = email_address
        self.login = login
        self.login_attempts = 0

    def describe_user(self):
        print(f'User full name is: {self.name} {self.surname}',
              f'User login is {self.login}',
              f'User email address is {self.email}', sep='\n')

    def greet_user(self):
        print(f'Hello {self.login}. have a nice day!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('Janusz', 'Kowalski', 'j.kowalski@email.com', 'janusz1992')
user_2 = User('Jan', 'Nwoak', 'jan.n@gmail.com', 'jan888')
user_3 = User('Sebastian', 'Plachecki', 'sosna@email.com', 'welmutka')
user_4 = User('Kamil', 'Tumulec', 'kamo@email.com', 'TUMULEC')


# for user in [user_1, user_2, user_3, user_4]:
#     print(user.describe_user())
#     print(user.greet_user())

# user_4.increment_login_attempts()
# user_4.increment_login_attempts()
# user_4.increment_login_attempts()
# print(user_4.login_attempts)
# user_4.reset_login_attempts()
# print(user_4.login_attempts)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'M&Ms', 'cookie']

    def show_flavors(self):
        print(f'available flavors: {", ".join(self.flavors)}')


# ice_cream_stand_1 = IceCreamStand('GoodLood', 'ice cream stand')
# print(ice_cream_stand_1.show_flavors())

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can remove post', 'can ban user']

    def show_privileges(self):
        print(f'admin privileges: {", ".join(self.privileges)}')

class Admin(User):
    def __init__(self, first_name, last_name, email_address, login):
        super().__init__(first_name, last_name, email_address, login)
        self.privileges = Privileges()


# main_admin = Admin('john', 'doe', 'xxx@email.com', 'johnydoe')
# main_admin.privileges.show_privileges()

