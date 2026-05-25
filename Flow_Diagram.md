# Terminal Inventory System - Flow Diagram

This document outlines the user and data flow for the terminal-based inventory management system.

---

## 1. System Entry Point (All Users)

1.  **Application Start**: The user runs the Python script.
2.  **Login Prompt**: The system asks for a **Login ID** and **Password**.
    -   The user also has an option to type `request` to apply for a new account.
3.  **Authentication Check**:
    -   **Success**: The system checks the `Users.xlsx` file. If the credentials match, it identifies the user's **Role** (Admin, Warehouse Staff, End User) and proceeds to the appropriate role-based menu.
    -   **Failure**: It displays an "Invalid credentials" message and returns to the login prompt.
    -   **Request Account**: If the user chose to request an account, proceed to the **Account Request Workflow**.

---

## 2. Account Request Workflow

1.  **Prompt for Details**: The system asks the new user to enter their desired **Login ID**, **Password**, **Full Name**, and requested **Role** (Warehouse Staff or End User).
2.  **Store Request**: The system saves this information to a new row in the `Users.xlsx` file with a status of **"Pending"**.
3.  **Confirmation**: A message is displayed confirming that the request has been submitted for admin approval. The application then exits.

---

## 3. Role-Based Menus

### 3.1 Admin (Warehouse Manager) Menu

*After a successful login, the Admin sees the following options:*

1.  **Approve Account Requests**:
    -   The system displays all users with a "Pending" status from `Users.xlsx`.
    -   The Admin can select a user and choose to **Approve** or **Deny** the request.
    -   **Approve**: The user's status in `Users.xlsx` is changed to **"Active"**.
    -   **Deny**: The user's row is deleted from `Users.xlsx`.
2.  **Manage Product Catalog**:
    -   **Add New Item**: The Admin is prompted to enter a **Product Name**, **Description**, and initial **Quantity** (usually 0). A new row is added to `Items.xlsx`.
    -   **Delete Item**: The Admin can select an existing item from a list to permanently remove it from `Items.xlsx`.
3.  **View Audit Log**:
    -   The system reads `History.xlsx` and prints a formatted log of all stock changes (who, what, when, how many).
4.  **Logout**: Returns to the main login prompt.

### 3.2 Warehouse Staff (Receiver) Menu

*After a successful login, the Warehouse Staff sees the following options:*

1.  **Add Stock (Receive Shipment)**:
    -   The system displays a list of all products from `Items.xlsx`.
    -   The user selects a product.
    -   The user is prompted to enter the **quantity** of the item being added.
    -   The system updates the **Quantity** for that item in `Items.xlsx`.
    -   A new entry is created in `History.xlsx` recording the user, item, quantity added, and timestamp.
2.  **Logout**: Returns to the main login prompt.

### 3.3 End User (Consumer) Menu

*After a successful login, the End User sees the following options:*

1.  **View Available Items**:
    -   The system displays a list of all products from `Items.xlsx` along with their current stock **Quantity**.
2.  **Consume/Checkout Item**:
    -   The user selects a product from the list.
    -   The user is prompted to enter the **quantity** they wish to check out.
    -   **Validation**: The system checks if the requested quantity is available.
        -   **Sufficient Stock**: The system subtracts the quantity from the item's total in `Items.xlsx`. A new entry is created in `History.xlsx` recording the transaction.
        -   **Insufficient Stock**: An error message is shown, and the transaction is cancelled.
3.  **Logout**: Returns to the main login prompt.

---

## 4. Data Files (The "Database")

-   **`Users.xlsx`**: Contains columns for `LoginID`, `Password`, `Name`, `Role`, and `Status`.
-   **`Items.xlsx`**: Contains columns for `ProductID`, `ProductName`, `Description`, and `Quantity`.
-   **`History.xlsx`**: Contains columns for `Timestamp`, `UserID`, `ProductID`, `Action` (e.g., "Stock In", "Stock Out"), and `QuantityChanged`.