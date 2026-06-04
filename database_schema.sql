CREATE TABLE collection(
    srno INT,
    reg_no VARCHAR(10) PRIMARY KEY,
    make VARCHAR(100),
    model VARHCAR(100),
    price INT,
    driven_kms INT
);

CREATE TABLE service(
    srno INT,
    reg_no VARCHAR(10) PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR (100),
    issue VARCHAR(100)
);


CREATE TABLE accounts (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    reg_no VARCHAR(20),
    make VARCHAR(50),
    model VARCHAR(50),
    reason_of_transaction VARCHAR(200),
    amount INT
);