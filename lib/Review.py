from customer import Customer

from restaurant import Restaurant

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Pizza Place")
restaurant2 = Restaurant("Burger Joint")
restaurant3 = Restaurant("Taco Bell")
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
    
    # def __str__(self):
    #     return f"Review: {self.customer.full_name()} rated {self.rating} stars

    
review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant1, 5)
# review3 = Review(customer1, restaurant2, 3)

print(review1.customer())
print(restaurant1.average_star_rating()) 

