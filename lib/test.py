from customer import Customer

from restaurant import Restaurant

# Create some customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create some restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Add reviews for customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test the methods
print(customer1.given_name())  
print(customer1.family_name())  
print(customer1.full_name())  



print(Customer.all())  # Output: [customer1, customer2]

print(customer1.restaurants())  # Output: [restaurant1, restaurant2]
print(customer2.restaurants())  # Output: [restaurant1]

print(restaurant1.reviews())  # Output: [review1, review3]
print(restaurant1.customers())  # Output: [customer1, customer2]

print(restaurant1.average_star_rating())  
