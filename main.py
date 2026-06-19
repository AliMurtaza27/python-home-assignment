# ==========================================
# Task 1: Student Profile Generator
# ==========================================
print("----- Task 1: Student Profile Generator -----")
full_name = input("Enter Full Name: ")
age = input("Enter Age: ")
fav_subject = input("Enter Favorite Subject: ")
city = input("Enter City: ")

print("\n----- STUDENT PROFILE -----")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Favorite Subject: {fav_subject}")
print(f"City: {city}")

# Display total number of characters in the student's name
name_length = len(full_name)
print(f"Total characters in name: {name_length}")
print("-" * 30)

# ==========================================
# Task 2: Online Shopping Receipt
# ==========================================
print("\n----- Task 2: Online Shopping Receipt -----")
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price_per_item = float(input("Enter Price Per Item: "))

# Calculations
total_cost = quantity * price_per_item
discount_amount = total_cost * 0.10
final_bill = total_cost - discount_amount

# Display receipt neatly
print("\n----- RECEIPT -----")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Item: {price_per_item}")
print(f"Total Cost: {total_cost}")
print(f"10% Discount Amount: {discount_amount}")
print(f"Final Bill After Discount: {final_bill}")
print("-" * 30)

# ==========================================
# Task 3: Password Strength Checker
# ==========================================
print("\n----- Task 3: Password Strength Checker -----")
password = input("Enter a password: ")

# Checking conditions and storing in Boolean variables
is_length_valid = len(password) >= 8
contains_at_symbol = "@" in password

print(f"Length Check: {is_length_valid}")
print(f"Contains @ : {contains_at_symbol}")
print("-" * 30)

# ==========================================
# Task 4: Movie Watchlist Manager
# ==========================================
print("\n----- Task 4: Movie Watchlist Manager -----")
# Create an empty list
movie_list = []

# Take inputs for 4 movies
m1 = input("Enter Movie 1: ")
m2 = input("Enter Movie 2: ")
m3 = input("Enter Movie 3: ")
m4 = input("Enter Movie 4: ")

# Store them in the list
movie_list.append(m1)
movie_list.append(m2)
movie_list.append(m3)
movie_list.append(m4)

print(f"Complete List: {movie_list}")

# Replace the second movie (Index 1)
new_movie = input("Enter a new movie to replace the second one: ")
movie_list[1] = new_movie

# Remove the last movie
movie_list.pop()

print(f"Updated List: {movie_list}")
print("-" * 30)

# ==========================================
# Task 5: Travel Budget Planner
# ==========================================
print("\n----- Task 5: Travel Budget Planner -----")
hotel_cost = float(input("Enter Hotel Cost: "))
food_cost = float(input("Enter Food Cost: "))
transport_cost = float(input("Enter Transport Cost: "))
shopping_cost = float(input("Enter Shopping Cost: "))

# Calculate total
total_budget = hotel_cost + food_cost + transport_cost + shopping_cost
print(f"Total Budget: {total_budget}")

# Check affordability
trip_affordable = total_budget <= 50000
print(f"Trip Affordable: {trip_affordable}")
print("-" * 30)

# ==========================================
# Task 6: Smart Username Creator
# ==========================================
print("\n----- Task 6: Smart Username Creator -----")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_year = input("Enter Birth Year: ")

# Extract last two digits of birth year
year_last_two = birth_year[-2:]

# Combine and convert to lowercase
username = (first_name + last_name + year_last_two).lower()
print(f"Username: {username}")
print("-" * 30)

# ==========================================
# Task 7: Classroom Attendance List
# ==========================================
print("\n----- Task 7: Classroom Attendance List -----")
# Create a list containing 5 student names using user input
students = []
for i in range(1, 6):
    s_name = input(f"Enter Student {i} Name: ")
    students.append(s_name)

# Add one new student
new_student = input("Enter one new student to add: ")
students.append(new_student)

# Remove one student entered by the user
remove_student = input("Enter the name of the student to remove: ")
if remove_student in students:
    students.remove(remove_student)
else:
    print("Student not found in list.")

# Sort the list alphabetically
students.sort()

# Display results
print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")
print(f"Total students: {len(students)}")
print(f"Updated lists: {students}")
print("-" * 30)