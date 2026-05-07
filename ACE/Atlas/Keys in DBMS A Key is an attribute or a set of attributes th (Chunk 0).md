---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:35:48.604268'
id: 378d71f8
links: []
modified: '2026-05-07T20:35:48.604268'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Keys in DBMS A Key is an attribute or a set of attributes th (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 7dd90c5938be
source: WINSEM2025-26_CSE2007_ETH_AP2025264000241_2026-01-07_Reference-Material-I.docx
page: 0
title: Keys in DBMS A Key is an attribute or a set of attributes th (Chunk 0)
keywords: ['DBMS A', 'Key', 'Super Key', 'Candidate Key', 'Primary Key', 'Alternate Key', 'Composite Key', 'Foreign Key', 'Student Table', 'Course Table', 'Attribute']
created: 2026-05-08 02:05:48
tree_path: DBMS > Page 0 > Keys in DBMS A Key is an attribute or a set of att
---

Keys in DBMS A Key is an attribute or a set of attributes that uniquely identifies a record (tuple) in a relation (table) Types of Keys 1. Super Key A Super Key is a combination of one or more attributes that can uniquely identify a row in a table. Example: If a table has attributes: Rno, Sname, Email, AadhaarNo Then possible super keys are: {Rno}, {Email}, {AadhaarNo}, {Rno, Email}, etc. 2. Candidate Key A Candidate Key is a minimal super key (no unnecessary attribute is included). Example: From the above super keys, the minimal ones are: {Rno}, {Email}, {AadhaarNo} These are candidate keys. 3. Primary Key A Primary Key is one of the candidate keys chosen by the database designer. It is unique and cannot be NULL. Example: writ Rno → Primary Key 4. Alternate Key The remaining candidate keys (which are not selected as the primary key) are called Alternate Keys. Example: If Rno is primary key, then Email and AadhaarNo are alternate keys. 5. Composite Key A Composite Key is a key formed by two or more attributes together. Example: {Rno, Cid} → Composite Key 6. Foreign Key A Foreign Key is an attribute in one table that refers to the primary key of another table. It is used to link two tables together. Diagram Student Table Keys: Super Keys: {Rno}, {Email}, {AadhaarNo}, {Rno, Email} Candidate Keys: {Rno}, {Email}, {AadhaarNo} Primary Key: Rno Alternate Keys: Email, AadhaarNo Composite Key: {Rno, Cid} Course Table Foreign Key Relationship: Student.Cid → Course.Cid An attribute is a property or characteristic of something. In DBMS (Database): An attribute is a column in a table. Example: Table: Student RollNo → Attribute Name → Attribute Age → Attribute In general English: An attribute means a quality or feature. Example: Honesty is an attribute of a good person. 01. 02. 03 04 05. 06.

### Related Concepts
- [[Super Key]]
- [[Foreign Key]]
- [[DBMS A]]
- [[Key]]
- [[Candidate Key]]
- [[Alternate Key]]
- [[Composite Key]]
- [[Course Table]]
- [[Student Table]]
- [[Primary Key]]
- [[Attribute]]
