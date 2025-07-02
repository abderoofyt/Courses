"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.

# Display the menu options for each iteration of the loop.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
inbox = []  # List to store email objects

def populate_inbox():
    global inbox
    inbox.append(Email("alice@example.com", "Meeting Reminder", "Don't forget our meeting at 3 PM."))
    inbox.append(Email("bob@example.com", "Weekend Plans", "Are we still on for Saturday?"))
    inbox.append(Email("charlie@example.com", "Project Update", "The latest changes have been pushed to GitHub."))

def list_emails():
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"From: {email.email_address}\nSubject: {email.subject_line}\n\n{email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email index.")

def view_unread_emails():
    unread_emails = [email for email in inbox if not email.has_been_read]
    if unread_emails:
        for index, email in enumerate(unread_emails):
            print(f"{index}: {email.subject_line}")
    else:
        print("No unread emails.")


# --- Email Program --- #
populate_inbox()

while True:
    user_choice = int(
        input(
            """
Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: """
        )
    )

    if user_choice == 1:
        list_emails()
        try:
            email_index = int(input("Enter the index of the email to read: "))
            read_email(email_index)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif user_choice == 2:
        view_unread_emails()

    elif user_choice == 3:
        print("Exiting application.")
        break

    else:
        print("Oops - incorrect input.")
