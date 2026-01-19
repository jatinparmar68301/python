#example of in and not in operator in python 
fruits = ["apple", "banana", "mango", "orange", "grapes", "pineapple", "papaya", "watermelon", "strawberry", "kiwi"]
print(fruits) 
favorite_fruit = input("what is your favorite fruit name :")
isFound = favorite_fruit in fruits
print(isFound)

isNotFound = favorite_fruit not in fruits
print(isNotFound)

# vegetables = ("potato", "onion", "tomato", "brinjal", "okra", "cabbage", "cauliflower", "spinach", "bottle gourd", "ridge gourd")

# favorite_vegis = input("what is your favorite vegetable name :")
# isFound = favorite_vegis in vegetables
# print(isFound)

# isNotFound = favorite_vegis not in vegetables
# print(isNotFound)

# india = {"name": "india", "capital": "new delhi", "currency": "indian rupee", "continent": "asia", "population": "large", "government": "democracy", "national_animal": "tiger", "national_bird": "peacock", "national_flower": "lotus", "timezone": "ist"}

# key = input("what do you want to know about india? :")
# isFound = key in india
# print(isFound)

# isNotFound = key not in india
# print(isNotFound)


# countries = "india china usa canada australia japan germany france italy brazil"
# country = input("where are you from :")
# isFound = country in countries
# print(isFound)

# isNotFound = country not in countries
# print(isNotFound)