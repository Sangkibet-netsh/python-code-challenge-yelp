
from review import Review
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self.all_restaurants.append(self)


    def name(self):
        return self._name
    

    def reviews(self):
        restaurant_reviews = []
        for review in Review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return [review.rating() for review in restaurant_reviews]
       
    
    # def restaurants(self):
    #     reviewed_restaurants = []
    #     for review in Review.all():
    #         restaurant = review.restaurant()
    #         if restaurant not in reviewed_restaurants:
    #             reviewed_restaurants.append(restaurant)
    #     return [restaurant.name() for restaurant in reviewed_restaurants]
    


    # def customers(self):
    #     reviewed_customers = []
    #     for review in self.reviews():
    #         reviewed_customers.append(review.customer())
    #     return  [customer.name() for customer in list(set(reviewed_customers))]
    
    def customers(self):
        reviewed_customers = []
        for review in self.reviews():
            reviewed_customers.append(review.customer)
        return list(set(reviewed_customers))

    


    def average_star_rating(self):
        total_ratings = 0
        for review in self.reviews():
            total_ratings += review.rating()
        if len(self.reviews()) > 0:
            return total_ratings / len(self.reviews())
        else:
            return 0.0


    @classmethod
    def all(cls):
        return cls.all_restaurants
    
    # def __repr__(self):
    #     return f"Restaurant(name='{self._name}')"

