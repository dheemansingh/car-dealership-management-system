🚗 First Motors - Car Dealership Management System

A Python and MySQL based Car Dealership Management System that allows customers to buy and sell cars, raise service requests, and enables the dealership to manage inventory and transactions efficiently.

## Features

### 🔍 View Car Collection

* View the complete dealership inventory.
* Filter cars by:

  * Make
  * Model
  * Price Range
  * Driven Kilometers

### 🛒 Buy a Car

* Browse available inventory.
* Select a vehicle using its registration number.
* Confirm purchase.
* Automatically removes the car from inventory.
* Records the transaction in the accounts database.
* Updates dealership balance.

### 🚘 Sell a Car

* Customers can sell their vehicles to the dealership.
* Vehicle details are added to inventory.
* Dealership purchase amount is deducted from balance.
* Resale price is automatically adjusted with a profit margin.
* Transaction is recorded in the accounts database.

### 🔧 Service Requests

* Customers can raise service requests.
* Stores vehicle details and issue description.
* Maintains a service request database.

### 💰 Financial Tracking

* Tracks dealership balance using a text file.
* Records all buying and selling transactions.

---

## Technologies Used

* Python 3
* MySQL
* mysql-connector-python

---

## Database Tables

### Collection

Stores available cars in inventory.

| Column     | Description         |
| ---------- | ------------------- |
| reg_no     | Registration Number |
| make       | Manufacturer        |
| model      | Vehicle Model       |
| driven_kms | Kilometers Driven   |
| type       | Vehicle Type        |
| price      | Selling Price       |

### Accounts

Stores transaction history.

| Column                | Description             |
| --------------------- | ----------------------- |
| reg_no                | Registration Number     |
| make                  | Manufacturer            |
| model                 | Vehicle Model           |
| reason_of_transaction | Transaction Description |
| amount                | Transaction Amount      |

### Service

Stores customer service requests.

| Column | Description               |
| ------ | ------------------------- |
| reg_no | Registration Number       |
| make   | Manufacturer              |
| model  | Vehicle Model             |
| issue  | Service Issue Description |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dheemansingh/car-dealership-management-system.git
cd car-dealership-management-system
```

### 2. Install dependencies

```bash
pip install mysql-connector-python
```

### 3. Create the database

```sql
CREATE DATABASE car_dealership;
```

Import the schema from:

```text
database_schema.sql
```

### 4. Configure MySQL credentials

Open `main.py` and update:

```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="car_dealership"
```

### 5. Create balance file

Create:

```text
current_balance.txt
```

Example:

```text
10000000
```

### 6. Run the project

```bash
python main.py
```

---

## Sample Workflow

### Customer Buying a Car

1. View collection.
2. Select registration number.
3. Confirm purchase.
4. Vehicle removed from inventory.
5. Transaction recorded.
6. Dealership balance updated.

### Customer Selling a Car

1. Enter vehicle details.
2. Dealership purchases vehicle.
3. Vehicle added to inventory.
4. Selling price adjusted for profit.
5. Transaction recorded.

---

## Future Improvements

* GUI using Tkinter or PyQt
* User authentication system
* Invoice generation
* Customer management module
* Search optimization
* Transaction analytics dashboard
* Web-based version using Flask or Django

---

## Project Author

**Dheeman Singh**


---

## License

This project is open-source and available for educational purposes.
