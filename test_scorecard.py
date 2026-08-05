# import requests

# url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/40381/scard"

# headers = {
# 	"x-rapidapi-key": "777c1dc328mshaa6c85b7f3dd8cap1909e6jsnbb8cbc134664",
# 	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# scorecard_data = response.json()

# #scorecard_list = data['scorecard']
# # print(len(scorecard_list[0].keys()))

# #Looping through the API and getting the batsman :-
# all_batsman = []
# for innings in scorecard_data['scorecard']:
#     for batsman in innings['batsman']:
#        Batsman = batsman['name']
#        Runs = batsman['runs']
#        Balls = batsman['balls']
#        Fours = batsman['fours']
#        Sixes = batsman['sixes']
#        score_data = {
           
# 	   }
#! pip install mysql-connector-python 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    database = "cricbuzz_livestats"
)

# if mydb.is_connected():
#     print("Connected Successfully")

mycursor = mydb.cursor(buffered=True)
# mycursor.execute("SHOW DATABASES")

# create_table = """
# CREATE TABLE players3(
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








