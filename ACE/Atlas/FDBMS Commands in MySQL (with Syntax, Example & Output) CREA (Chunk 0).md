---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:35:38.745248'
id: 32a9077a
links: []
modified: '2026-05-07T20:35:38.745248'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: FDBMS Commands in MySQL (with Syntax, Example & Output) CREA (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: e691a56d5143
source: WINSEM2025-26_CSE2007_ETH_AP2025264000241_2025-12-16_Reference-Material-I.docx
page: 0
title: FDBMS Commands in MySQL (with Syntax, Example & Output) CREA (Chunk 0)
keywords: ['MySQL', 'FDBMS Commands', 'CREATE DATABASE', 'CREATE TABLE', 'ALTER TABLE', 'DROP TABLE', 'INSERT', 'SELECT', 'Employees']
created: 2026-05-08 02:05:38
tree_path: DBMS > Page 0 > FDBMS Commands in MySQL (with Syntax, Example & Ou
---

FDBMS Commands in MySQL (with Syntax, Example & Output) CREATE DATABASE SYNTAX: Create database databasename; Ex:-create database vitap; Display the databases Show databases; HOW TO USE DATABASE Use databasename; Use vitap; 🔷 DDL (Data Definition Language) ✅ 1. CREATE Use: Create a table Syntax (MySQL): CREATE TABLE table_name ( column_name datatype, column_name datatype ); Example: CREATE TABLE Employees ( EmpID INT, Name VARCHAR(50), Salary INT ); Output: Query OK, 0 rows affected ✅ 2. ALTER Use: Modify table structure ➤ Add Column ALTER TABLE Employees ADD Email VARCHAR(50); Output: Query OK, 0 rows affected ➤ Modify Column ALTER TABLE Employees MODIFY Salary DECIMAL(10,2); Output: Query OK, 0 rows affected ➤ Drop Column ALTER TABLE Employees DROP Email; Output: Query OK, 0 rows affected ✅ 3. DROP Use: Delete table permanently DROP TABLE Employees; Output: Query OK, 0 rows affected ✅ 4. TRUNCATE Use: Delete all rows (structure remains) TRUNCATE TABLE Employees; Output: Query OK, 0 rows affected ✅ 5. RENAME Use: Rename table ALTER TABLE Employees RENAME TO EmpDetails; Output: Query OK, 0 rows affected COMMENT ALTER TABLE table_name MODIFY column_name datatype COMMENT 'column description'; SHOW CREATE TABLE kk; 🔷 DML (Data Manipulation Language) ✅ 1. INSERT Use: Insert data INSERT INTO Employees (EmpID, Name, Salary) VALUES (101, 'Ramesh', 35000); Output: Query OK, 1 row affected ✅ 2. SELECT Basic SELECT Syntax SELECT column1, column2 FROM table_name; Example SELECT Name, Salary FROM Employees; ➡️ Displays Name and Salary of all employees. 2️⃣ SELECT All Columns SELECT * FROM table_name; Example SELECT * FROM Employees; ➡️ Displays all columns and all records. 3️⃣ SELECT with WHERE (Condition) SELECT column1, column2 FROM table_name WHERE condition; Example SELECT Name, Salary FROM Employees WHERE Salary > 30000; ➡️ Shows employees with salary greater than 30000. 4️⃣ SELECT with AND / OR SELECT * FROM table_name WHERE condition1 AND condition2; Example SELECT * FROM Employees WHERE Department = 'IT' AND Salary > 40000; SELECT * FROM Employees WHERE Department = 'HR' OR Department = 'Finance'; 5️⃣ SELECT with DISTINCT SELECT DISTINCT column_name FROM table_name; Example SELECT DISTINCT Department FROM Employees; ➡️ Displays unique department names only. 6️⃣ SELECT with ORDER BY SELECT * FROM table_name ORDER BY column_name ASC|DESC; Example SELECT * FROM Employees ORDER BY Salary DESC; ➡️ Sorts employees by salary (highest first). 7️⃣ SELECT with LIMIT SELECT * FROM table_name LIMIT number; Example SELECT * FROM Employees LIMIT 5; ➡️ Shows first 5 records only. 8️⃣ SELECT with LIKE (Pattern Matching) SELECT * FROM table_name WHERE column_name LIKE pattern; Example SELECT * FROM Employees WHERE Name LIKE 'A%'; ➡️ Names starting with A. SELECT * FROM Employees WHERE Name LIKE '%an%'; ➡️ Names containing "an". 9️⃣ SELECT with BETWEEN SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2; Example SELECT * FROM Employees WHERE Salary BETWEEN 20000 AND 50000; 🔟 SELECT with IN SELECT * FROM table_name WHERE column_name IN (value1, value2); Example SELECT * FROM Employees WHERE Department IN ('IT', 'HR'); 1️⃣1️ SELECT with Aggregate Functions SELECT COUNT(*) FROM table_name; SELECT AVG(Salary) FROM Employees; SELECT MAX(Salary), MIN(Salary) FROM Employees; 1️⃣2️ SELECT with GROUP BY SELECT Department, COUNT(*) FROM Employees GROUP BY Department; ➡️ Shows number of employees in each department. 1️⃣3️ SELECT with HAVING SELECT Department, COUNT(*) FROM Employees GROUP BY Department HAVING COUNT(*) > 5; Use: Retrieve data SELECT Name, Salary FROM Employees; Output: ✅ 3. UPDATE Use: Update existing data UPDATE Employees SET Salary = 40000 WHERE EmpID = 101; Output: Query OK, 1 row affected ✅ 4. DELETE Use: Delete specific rows DELETE FROM Employees WHERE EmpID = 101; Output: Query OK, 1 row affected ✅ 5. MERGE (UPSERT in MySQL) ➡ MySQL uses INSERT … ON DUPLICATE KEY UPDATE INSERT INTO Employees (EmpID, Name, Salary) VALUES (101, 'Ramesh', 45000) ON DUPLICATE KEY UPDATE Salary = 45000; Output: Query OK, 1 row affected ✅ 6. CALL Use: Execute stored procedure CALL IncreaseSalary(101); Output: Query OK, 0 rows affected ✅ 7. EXPLAIN Use: Show query execution plan EXPLAIN SELECT * FROM Employees; Output (sample): ✅ 8. LOCK TABLE Use: Lock table LOCK TABLES Employees WRITE; Output: Query OK, 0 rows affected Unlock: UNLOCK TABLES; 🔷 DCL (Data Control Language) ✅ 1. GRANT Use: Give permission GRANT SELECT, INSERT ON Employees TO 'user1'@'localhost'; select user,host from mysql.user; Output: Query OK, 0 rows affected ✅ 2. REVOKE Use: Remove permission REVOKE INSERT ON Employees FROM 'user1'@'localhost'; Output: Query OK, 0 rows affected 🔷 TCL (Transaction Control Language) ✅ 1. COMMIT Use: Save changes COMMIT; Output: Query OK, 0 rows affected ✅ 2. ROLLBACK Use: Undo changes ROLLBACK; Example 1: ROLLBACK with INSERT Step 1: Create table CREATE TABLE EmpDetails ( EmpID INT, Name VARCHAR(50), Salary INT ) ENGINE=InnoDB; Step 2: Start transaction START TRANSACTION; Step 3: Insert records INSERT INTO EmpDetails VALUES (1, 'Kiran', 30000); INSERT INTO EmpDetails VALUES (2, 'Ravi', 25000); Step 4: Check data SELECT * FROM EmpDetails; Output (temporary): +-------+-------+--------+ | EmpID | Name | Salary | +-------+-------+--------+ | 1 | Kiran | 30000 | | 2 | Ravi | 25000 | +-------+-------+--------+ Step 5: ROLLBACK ROLLBACK; Step 6: Check again SELECT * FROM EmpDetails; Output: Query OK, 0 rows affected ✅ 3. SAVEPOINT Use: Create checkpoint SAVEPOINT A; Rollback to savepoint: ROLLBACK TO A; Output: Query OK, 0 rows affected

### Related Concepts
- [[CREATE DATABASE]]
- [[ALTER TABLE]]
- [[FDBMS Commands]]
- [[INSERT]]
- [[DROP TABLE]]
- [[SELECT]]
- [[Employees]]
- [[CREATE TABLE]]
- [[MySQL]]
