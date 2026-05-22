import pandas as pd

def login_system():
    
    df = pd.read_excel(r"C:\Users\acer\Desktop\Sample Management System\Users.xlsx")

    login_id = input("Enter your Login ID: ")
    password = input("Enter your Password: ")

    user_record = df[(df['LoginID'] == login_id) & (df['Password'] == password)]

    if not user_record.empty:
        role = user_record.iloc[0]['Role']
        name = user_record.iloc[0]['Name']

        if role == 'admin':
            print("\nWelcome admin")
        elif role == 'user':
            print(f"\nWelcome {name}")
        else:
            print("\nLogin successful, role is unknown.")
    else:
        print("\nInvalid Login ID or Password.")

if __name__ == "__main__":
    login_system()