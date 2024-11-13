DROP TABLE IF EXISTS traffic;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL
);

CREATE TABLE traffic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    ip TEXT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    received_traffic REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

INSERT INTO customers (id, customer_name) VALUES
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Alice Johnson'),
(4, 'Bob Brown');

INSERT INTO traffic (id, customer_id, ip, date, received_traffic) VALUES
(101, 1, '192.168.218.159', '2022-01-05 10:15:00', 150.00),
(102, 2, '192.168.5.110', '2022-07-15 13:45:00', 200.00),
(103, 3, '192.168.214.201', '2022-02-25 18:30:00', 250.00),
(104, 4, '192.168.224.118', '2024-03-07 12:00:00', 300.00),
(105, 2, '192.168.218.159', '2024-03-15 14:00:00', 120.00),
(106, 4, '192.168.5.110', '2024-03-18 15:00:00', 400.00),
(107, 1, '192.168.214.201', '2023-01-10 10:30:00', 180.00),
(108, 3, '192.168.224.118', '2023-02-28 14:00:00', 220.00),
(109, 2, '192.168.218.159', '2023-03-01 16:15:00', 175.00),
(110, 4, '192.168.5.110', '2023-03-10 17:45:00', 300.00),
(111, 1, '192.168.214.201', '2023-03-20 13:00:00', 140.00),
(112, 3, '192.168.224.118', '2024-03-22 09:00:00', 260.00),
(113, 2, '192.168.218.159', '2024-03-25 15:30:00', 110.00),
(114, 4, '192.168.5.110', '2024-04-01 12:00:00', 320.00),
(115, 1, '192.168.214.201', '2024-04-05 11:15:00', 150.00),
(116, 3, '192.168.224.118', '2023-04-08 14:45:00', 290.00),
(117, 4, '192.168.214.201', '2023-04-10 16:30:00', 210.00),
(118, 2, '192.168.224.118', '2025-04-12 18:00:00', 125.00),
(119, 1, '192.168.218.159', '2025-04-15 12:30:00', 165.00),
(120, 3, '192.168.214.201', '2025-04-18 14:15:00', 270.00),
(121, 4, '192.168.224.118', '2025-04-20 10:45:00', 190.00),
(122, 1, '192.168.218.159', '2025-04-22 09:30:00', 130.00),
(123, 2, '192.168.224.118', '2025-04-25 11:00:00', 160.00),
(124, 3, '192.168.218.159', '2026-04-28 14:00:00', 240.00),
(125, 4, '192.168.214.201', '2026-04-30 17:15:00', 210.00),
(126, 1, '192.168.224.118', '2026-05-02 13:45:00', 170.00);