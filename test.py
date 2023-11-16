import requests

# Function to make requests and write TRUE/FALSE to a text file
def test_route(email):
    params = {
        'email': email,
        'city': 'Lima'
    }
    response = requests.get('http://127.0.0.1:5000/', params=params)

# List of 20 different email parameters
emails = [
    "test1@email.com",
    "test2@email.com",
    "test3@email.com",
    "test4@email.com",
    "test5@email.com",
    "test6@email.com",
    "test7@email.com",
    "test8@email.com",
    "test9@email.com",
    "test10@email.com",
    "test11@email.com",
    "test12@email.com",
    "test13@email.com",
    "test14@email.com",
    "test15@email.com",
    "test16@email.com",
    "test17@email.com",
    "test18@email.com",
    "test19@email.com",
    "test20@email.com",
]

def count_and_percentage(filename):
    total = 0
    true_count = 0
    false_count = 0

    # Read the file and count occurrences of TRUE and FALSE
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "TRUE" in line:
                true_count += 1
            elif "FALSE" in line:
                false_count += 1
            total += 1

    # Calculate percentages
    true_percentage = (true_count / total) * 100 if total > 0 else 0
    false_percentage = (false_count / total) * 100 if total > 0 else 0

    # Print the results
    print(f"Total: {total}")
    print(f"TRUE count: {true_count}, Percentage: {true_percentage:.2f}%")
    print(f"FALSE count: {false_count}, Percentage: {false_percentage:.2f}%")

def clear_file(filename):
    with open(filename, 'w') as file:
        pass

# Clear the file
clear_file('output.txt')
# Test the route with each email and write the output to output.txt
for email in emails:    
    test_route(email)
# Count the number of TRUEs and FALSEs in the output.txt file
count_and_percentage("output.txt")
