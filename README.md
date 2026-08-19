# 🏏 Cricbuzz LiveStats Dashboard

A Streamlit-based cricket analytics dashboard built using **Python, MySQL, Pandas, and Streamlit**. The project provides an interactive platform to explore cricket data, view player statistics, perform SQL-based analytics, and manage player records through CRUD operations.

## 📌 Project Overview

**Cricbuzz LiveStats** is a multi-page cricket analytics dashboard that combines data stored in a MySQL database with an interactive Streamlit interface.

The application includes four main sections:

* 🏏 **Live Scores** – View live cricket score information.
* 📊 **Player Statistics** – Explore player performance and statistical information.
* 🗄️ **SQL Analytics** – Perform predefined SQL-based cricket data analysis.
* ⚙️ **CRUD Operations** – Create, read, update, and delete player records.

The project demonstrates the integration of a Python application with a relational database and provides an interactive interface for cricket data analysis.

## ✨ Features

### 1. 🏏 Live Scores

The Live Scores page provides an interactive view of cricket match and score information.

Users can explore available match data through the Streamlit dashboard.

### 2. 📊 Player Statistics

The Player Statistics page retrieves cricket player information from MySQL and processes the data using Pandas.

Users can explore player-related statistics through an interactive interface.

### 3. 🗄️ SQL Analytics

The SQL Analytics page provides predefined analytical queries for exploring cricket data stored in the MySQL database.

The page demonstrates the use of SQL queries to answer different cricket-related analytical questions.

### 4. ⚙️ CRUD Operations

The CRUD Operations page demonstrates database record management using Python, Streamlit, and MySQL.

It supports:

* **Create** – Add new player records
* **Read** – View existing player records
* **Update** – Modify player records
* **Delete** – Remove player records

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* MySQL
* mysql-connector-python

## 🗄️ Database

MySQL is used as the backend database for storing and retrieving cricket-related information.

The Python application connects to MySQL using `mysql.connector`.

The project includes database tables for cricket data such as:

* Players
* Player Records
* Batting
* Bowling
* Matches
* Scorecards
* Series
* Teams
* Venues

## 📂 Project Structure

```text
cricbuzz_livestats/
│
├── 1_Live_Scores.py
├── requirements.txt
├── README.md
│
└── pages/
    ├── 2_Player_Statistics.py
    ├── 3_SQL_Analytics.py
    └── 4_CRUD_Operations.py
```

## 🚀 Application Pages

| Page                 | Description                                  |
| -------------------- | -------------------------------------------- |
| 🏏 Live Scores       | Displays cricket score and match information |
| 📊 Player Statistics | Explores cricket player statistics           |
| 🗄️ SQL Analytics    | Performs SQL-based cricket data analysis     |
| ⚙️ CRUD Operations   | Manages player records using CRUD operations |

## ✅ Current Status

**Project Completed**

All four dashboard pages have been implemented and integrated into the Streamlit application:

* ✅ Live Scores
* ✅ Player Statistics
* ✅ SQL Analytics
* ✅ CRUD Operations

The project is fully uploaded to GitHub and is ready to be used as a portfolio project.

## 🔮 Future Improvements

Possible future enhancements include:

* Add more cricket analytics and visualizations
* Add additional filtering options
* Improve dashboard UI/UX
* Add more advanced player comparison features
* Improve error handling and database connection management
* Add additional analytical SQL queries
* Deploy the Streamlit application online

## 🎯 Project Purpose

This project was developed as a practical data analytics and application development project to strengthen skills in:

* Python programming
* SQL and MySQL
* Data processing with Pandas
* Streamlit application development
* Database connectivity
* CRUD operations
* Data analysis and visualization

## 📌 Disclaimer

This project is a learning and portfolio project developed for demonstrating skills in Python, SQL, data analytics, database management, and Streamlit application development.
