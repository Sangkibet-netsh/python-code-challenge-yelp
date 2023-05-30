
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        customers = []
        for review in self.reviews:
            customer = review.customer()
            customers.append(customer)
        return list(set(customers))

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def average_star_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])
        return total_ratings / len(self.reviews)
    

  

restaurant1 = Restaurant("Pizza Place")
restaurant2 = Restaurant("Burger Joint")

print(restaurant1.name) 