DROP TABLE IF EXISTS tbCustomers;


CREATE TABLE tbCustomers
(
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_name TEXT,
  address TEXT
);
DROP TABLE IF EXISTS tbOrders;

CREATE TABLE tbOrders
(
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  subscription_id INTEGER,
  purchase_date DATE,
  FOREIGN KEY (customer_id) REFERENCES tbCustomers(id),
  FOREIGN KEY (subscription_id) REFERENCES tbSubscriptions(id)
);
DROP TABLE IF EXISTS tbSubscriptions;

CREATE TABLE tbSubscriptions
(
  subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT,
  price_per_month DECIMAL,
  subscription_length TEXT
);
