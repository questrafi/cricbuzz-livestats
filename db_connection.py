import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    database = "cricbuzz_livestats"
)

# if mydb.is_connected():
#     print("Connected Successfully")

mydb.ping(reconnect=True)

mycursor = mydb.cursor(buffered=True)
# mycursor.execute("SHOW DATABASES")

# create_table = """
# CREATE TABLE players3(a
#     id INT PRIMARY KEY,
#     Name VARCHAR(100), 
#     Team VARCHAR(100)

# )
# """
# mycursor.execute(create_table)
# # print("Table created successfully")

# create_table = """
# CREATE TABLE TEAMS(
#     Team_id INT PRIMARY KEY,
#     Team_name VARCHAR(100), 
#     short_name VARCHAR(100)
    

# )
# """
# mycursor.execute(create_table)
# # print("Table created successfully")

# create_table = """
# CREATE TABLE MATCHES(
    # Match_id INT PRIMARY KEY,
    # Series_Name VARCHAR(100), 
    # Description VARCHAR(100),
    # Format  VARCHAR(100),
    # Team1_id INT,
    # Team2_id INT,
    # Venue VARCHAR(100),
    # City VARCHAR(100),
    # State VARCHAR(100),
    # Status VARCHAR(100)

# """
# mycursor.execute(create_table)
# # print("Table created successfully")


###VENUE TABLE

# create_table = """
# CREATE TABLE VENUES(
#     venue_id INT PRIMARY KEY,
#     ground VARCHAR(100), 
#     city VARCHAR(60),
#     timezone  VARCHAR(100),
#     latitude VARCHAR(100),
#     longitude VARCHAR(100)
   
# )
# """

# mycursor.execute(create_table)
# # print("Table created successfully")


# create_table = """
# CREATE TABLE SERIES(
#     series_id INT PRIMARY KEY,
#     series_name VARCHAR(100)
   
# )
# """
# mycursor.execute(create_table)
# # print("Table created successfully")


# create_table = """
# CREATE TABLE SCORECARD(
#     scorecard_id INT PRIMARY KEY AUTO_INCREMENT,
#     match_id INT ,
#     innings_id INT,
#     batting_team_id INT ,
#     runs INT,
#     wickets INT,
#     overs VARCHAR(20)
   
# )
# """
# mycursor.execute(create_table)
# print("Table created successfully")

#creating batting table :-
# create_table = """
# CREATE TABLE Batting(
#     batting_id INT PRIMARY KEY AUTO_INCREMENT,
#     match_id INT ,
#     innings_id INT,
#     player_id INT,
#     player_name VARCHAR(100) ,
#     runs INT,
#     balls INT,
#     fours INT,
#     sixes INT,
#     strike_rate VARCHAR(20),
#     Out_description VARCHAR(255) 
   
# )
# """
# mycursor.execute(create_table)
# print("Table created successfully")


#creating bowling table :-
# create_table = """
# CREATE TABLE Bowling(
#     bowling_id INT PRIMARY KEY AUTO_INCREMENT,
#     match_id INT ,
#     innings_id INT,
#     player_id INT,
#     player_name VARCHAR(100) ,
#     runs INT,
#     overs VARCHAR(20),
#     maidens INT,
#     wickets INT,
#     economy VARCHAR(20)
     
   
# )
# """
# mycursor.execute(create_table)
# print("Table created successfully")




