# 🏏 Cricbuzz LiveStats Dashboard

A Streamlit-based cricket analytics dashboard built using **Python, MySQL, Pandas, and Streamlit**. The project is designed to display and analyze cricket player statistics using data stored in a MySQL database.

## 📌 Project Overview

Cricbuzz LiveStats is a cricket statistics dashboard that provides an interactive interface for viewing player information and analyzing cricket performance data.

The project combines:

* **Python** for application logic
* **MySQL** for storing cricket/player data
* **Pandas** for data processing
* **Streamlit** for building the interactive dashboard

The project also includes a CRUD section for managing player records.

## ✨ Features

### 1. Cricket Statistics Dashboard

The dashboard provides an interactive view of cricket statistics and player-related information.

Users can explore the available data through a Streamlit interface.

### 2. Player Statistics / Analysis

The application retrieves data from MySQL and processes it using Pandas before displaying it through the Streamlit dashboard.

The project focuses on making cricket statistics easier to view and understand through an interactive interface.

### 3. Player Records CRUD

A separate section was created to demonstrate CRUD operations:

* **Create** – Add player records
* **Read** – View player records
* **Update** – Modify player records
* **Delete** – Remove player records

The CRUD functionality currently works with a dedicated player records table in the database.

> **Note:** The database design and integration of the CRUD section with the main player/statistics data are still being refined.

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* MySQL
* mysql-connector-python

## 🗄️ Database

MySQL is used as the backend database for storing and retrieving cricket/player information.

The Python application connects to MySQL using `mysql.connector`.

## 📂 Project Structure

```text
Cricbuzz-LiveStats/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── ...
│
└── assets/
    └── ...
```

*The actual file structure may vary depending on the current project implementation.*

## 🚧 Current Status

The project is **partially completed and under active development**.

The main dashboard pages and player CRUD functionality have been implemented.

The **third page of the application is currently under development** and will be completed after further refinement of the project requirements and database design.

## 🎯 Future Improvements

* Complete the third dashboard page
* Refine the database relationships
* Improve integration between player records and the main statistics data
* Add more cricket analytics and visualizations
* Improve UI/UX
* Add additional filtering and player-selection functionality
* Improve error handling and database connection management

## 👨‍💻 Project Purpose

This project was developed as a practical project to strengthen skills in:

* Python
* SQL/MySQL
* Data processing with Pandas
* Streamlit application development
* CRUD operations
* Connecting a Python application with a relational database

## 📌 Disclaimer

This project is a learning/portfolio project and is currently under development. Some features, particularly the third dashboard page and parts of the database integration, are still being refined.
