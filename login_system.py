import pandas as pd

class LoginSystem:
    def __init__(self, user_file_path):
        """
        Initializes the LoginSystem.

        Args:
            user_file_path (str): The file path to the Excel file containing user data.
        """
        try:
            self.user_data = pd.read_excel(user_file_path)
        except FileNotFoundError:
            print(f"Error: The file at {user_file_path} was not found.")
            self.user_data = pd.DataFrame()

    def authenticate_user(self):
        """
        Authenticates a user based on login ID and password input.

        If the user data is not loaded, it prints an error.
        On successful authentication, it calls the greet_user method.
        On failure, it prints an invalid credentials message.
        """
        if self.user_data.empty:
            print("User data is not loaded. Cannot authenticate.")
            return

        login_id = input("Enter your Login ID: ")
        password = input("Enter your Password: ")

        user_record = self.user_data[(self.user_data['LoginID'] == login_id) & (self.user_data['Password'] == password)]

        if not user_record.empty:
            self.greet_user(user_record)
        else:
            print("\nInvalid Login ID or Password.")

    def greet_user(self, user_record):
        """
        Prints a welcome message based on the user's role.

        Args:
            user_record (pd.DataFrame): A DataFrame row containing the authenticated user's data.
        """
        role = user_record.iloc[0]['Role']
        name = user_record.iloc[0]['Name']

        if role == 'admin':
            print("\nWelcome admin")
        elif role == 'user':
            print(f"\nWelcome {name}")
        else:
            print("\nLogin successful, role is unknown.")

if __name__ == "__main__":
    user_file = r"C:\Users\acer\Desktop\Sample Management System\Users.xlsx"
    authenticator = LoginSystem(user_file)
    authenticator.authenticate_user()