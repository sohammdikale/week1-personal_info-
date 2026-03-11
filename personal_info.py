# Personal Information Manager
# Author: Your Name
# Description: Simple Python program to store and display personal information

# Welcome message
print("=" * 40)
print("PERSONAL INFORMATION MANAGER")
print("=" * 40)

# Static information
name = "soham dikale"
age = 20
city = "chh.sambhajinagar"
hobby = "coding"

# Ask user input
print("\nPlease enter some information:")

favorite_food = input("What is your favorite food? ")

# Check if input is empty
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What is your favorite food? ")

favorite_color = input("What is your favorite color? ")

while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What is your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display information
print("\n" + "=" * 40)
print("YOUR INFORMATION")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

# Goodbye message
print("\nThank you for using the program!")
print("=" * 40)
