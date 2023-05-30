
from review import Review

class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self._given_name = name
        self._family_name = family_name
        self.all_customers.append(self)


    def given_name(self):
        return self._given_name
    

    def family_name(self):
        return self._family_name
    

    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    

    @classmethod
    def all(cls):
        return cls.all_customers

    
    def restaurants(self):
        reviewed_restaurants = []
        for review in Review.all():
            restaurant = review.restaurant()
            if restaurant not in reviewed_restaurants:
                reviewed_restaurants.append(restaurant)
        return [restaurant.name() for restaurant in reviewed_restaurants]


    def add_review(self, restaurant, rating):
        Review(self, restaurant, rating)


    def num_reviews(self):
        return len(self.reviews())

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                customers.append(customer)
        return customers





