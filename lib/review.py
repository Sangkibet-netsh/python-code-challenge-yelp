

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
    
    def __repr__(self):
        return f"Review(customer={self._customer}, restaurant={self._restaurant}, rating={self._rating})"