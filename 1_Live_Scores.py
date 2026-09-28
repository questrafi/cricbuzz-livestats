# ##EXTRACTION OF SERIES NAME

# extract_basic_info = (data['typeMatches'][0]['seriesMatches'])
# seriesMatches_list = (extract_basic_info[0])
# seriesAdWrapper_dict = seriesMatches_list['seriesAdWrapper']
# series_name = seriesAdWrapper_dict['matches'][0]['matchInfo']['seriesName']
# #print("Series Name:",series_name)

# ##EXTRACTION OF Match Description

# matches = seriesAdWrapper_dict['matches']
# #print(matches)
# #matches1 = seriesAdWrapper_dict['matches'][1] #error came as only one index
# matches_list = seriesAdWrapper_dict['matches'][0]
# match_description = matches_list['matchInfo']['matchDesc']
# #print("Match Description: ",match_description)

# ##EXTRACTION OF Match format:
# match_format = matches_list['matchInfo']['matchFormat']
# #print("Match format: ",match_format)

# ##EXTRACTION OF STATE:
# match_state = matches_list['matchInfo']['state']
# #print("Match state: ",match_state)

# ##EXTRACTION OF STATUS:
# match_status = matches_list['matchInfo']['status']
# #print("Match status: ",match_status)

# ##EXTRACTION OF VENUE:
# match_venue = matches_list['matchInfo']['venueInfo']['ground']
# #print("Match venue: ",match_venue)

# ##EXTRACTION OF CITY:
# match_city = matches_list['matchInfo']['venueInfo']['city']
# #print("Match City: ",match_city)

# ##EXTRACTION OF FIRST INNS. TEAM 1 SCORES :-

# ##EXTRACTION OF team1 score:
# inningsid1 = matches_list['matchScore']['team1Score']['inngs1']['inningsId']
# #EXTRACTION OF team1 score:
# team1_first_innings_runs = matches_list['matchScore']['team1Score']['inngs1']['runs']
# ##EXTRACTION OF team1 score:
# team1_first_innings_wickets = matches_list['matchScore']['team1Score']['inngs1']['wickets']
# ##EXTRACTION OF team1 score:
# team1_first_innings_overs = matches_list['matchScore']['team1Score']['inngs1']['overs']

# #print(series_name)

# ##EXTRACTION OF SECOND INNS. TEAM 2 SCORES :-

# #print(matches_list)
# ##EXTRACTION OF team2 score:
# # inningsid2 = matches_list['matchScore']['team2Score']['inngs1']['inningsId']
# # # ##EXTRACTION OF team2 score:
# # team2_first_innings_runs = matches_list['matchScore']['team2Score']['inngs1']['runs']
# # # ##EXTRACTION OF team2 score:
# # team2_first_innings_wickets = matches_list['matchScore']['team2Score']['inngs1']['wickets']
# # # ##EXTRACTION OF team2 score:
# # team2_first_innings_overs = matches_list['matchScore']['team2Score']['inngs1']['overs']


# ##DISPLAY TEAM NAMES IN "VS" :-

# team1_name = matches_list['matchInfo']['team1']['teamName']
# team2_name = matches_list['matchInfo']['team2']['teamName']
# #print(f"{team1_name}{team2_name}")
# team_VS = f"{team1_name} Vs {team2_name}"
# #print(team)

# ##DISPLAY ONE CLEAN OUTPUT OF SCORE OF TEMA1:-

# score_f = f"{team1_first_innings_runs}/{team1_first_innings_wickets}" 
# overs_f = f"({team1_first_innings_overs})"
# team1_score = (f"{score_f} {overs_f}")


# # ##DISPLAY ONE CLEAN OUTPUT OF SCORE OF TEMA1:-

# # score_s = f"{team2_first_innings_runs}/{team2_first_innings_wickets}" 
# # overs_s = f"({team2_first_innings_overs})"
# # team2_score = (f"{score_s} {overs_s}")


# ##PRINTING COMPLETLE CLEAN O/P :-

# # print("Series Name:",series_name)
# # print(team)
# # print(f"Japan 's Score: {japan_score}")
# # print(f"Vanuatu 's Score: {vanuatu_score}")
# # print("Match venue: ",match_venue)

# ##ORGANIZING OR COMBINING ALL VARIABLES IN A SIGLE VARIABLE

# match_data = {
#     "Series_Name" : series_name,
#     "city" : match_city,
#     "venue" : match_venue,
#     "team1" : team1_name,
#     "team2" : team2_name,
#     "Description" : match_description,
#     "Format" : match_format,
#     "score1" : team1_score,
#     "state" : match_state
#     #"score2" : team2_score,
# }
#print(match_data)
#print(data)

import pandas as pd
import streamlit as st
import requests
from db_connection import mydb,mycursor
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

#import pandas as pd
#import json

# Sidebar information box
st.sidebar.markdown("""
<div style="background-color: #294C6F; padding: 15px; border-radius: 8px; color: white;">
<b>Live Scores Page:</b>
<ul>
<li>Real-time match data</li>
<li>Detailed scorecards</li>
<li>Series information</li>
<li>Interactive match selection</li>
</ul>
</div>
""", unsafe_allow_html=True)


#creating the title for the sidebar
# st.sidebar.title("🖌️ Cricket Dashboard")

#First Api extracted :-


url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
	"x-rapidapi-key": RAPIDAPI_KEY,
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}
#defining function to prevent rerunnig the whole script everytime :-

response = requests.get(url, headers=headers, timeout=10)
# st.write(url)

# print(response.json())
if response.status_code == 200:
    data = response.json()
    #st.write(data.keys())
else:
    st.error(f"Live Matches API Error: {response.status_code}")
    st.stop()

#print(type(data))
#print(data.keys())

#Scorecard API extraction :-
# url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{selected_id}/scard"

# headers = {
# 	"x-rapidapi-key": "777c1dc328mshaa6c85b7f3dd8cap1909e6jsnbb8cbc134664",
# 	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

#scorecard_data = response.json()
#st.write(data['typeMatches'][0])

##LOOPING THROUGHT TYPEMATCHES TO PRINT ALL MATCHE'S VALUES :-

all_matches = []
for match_type in data['typeMatches']:
    for series in match_type['seriesMatches']:
        if 'seriesAdWrapper' not in series:
            continue #if there are no adwropper in any series e.g native-mtches
        info_match = series['seriesAdWrapper']['matches']
        for match in info_match:
            #st.write(match)
            match_id = match['matchInfo']['matchId']
            series_id = match['matchInfo']['seriesId']
            series_name = match['matchInfo']['seriesName']
            match_description = match['matchInfo']['matchDesc']
            start_date = match['matchInfo']['startDate']
            #print("DEBUG MATCH:", match_id)
            #print("DEBUG START DATE:", start_date)
            end_date = match['matchInfo']['endDate']
            match_format = match['matchInfo']['matchFormat']
            match_state = match['matchInfo']['state']
            match_status = match['matchInfo']['status']
            venue_id = match['matchInfo']['venueInfo']['id']
            match_venue = match['matchInfo']['venueInfo']['ground']
            match_city = match['matchInfo']['venueInfo']['city']
            timezone = match['matchInfo']['venueInfo']['timezone']
            latitude = match['matchInfo']['venueInfo']['latitude']
            longitude = match['matchInfo']['venueInfo']['longitude']
            team1_name = match['matchInfo']['team1']['teamName']
            team2_name = match[F'matchInfo']['team2']['teamName']
            team1_id = match['matchInfo']['team1']['teamId']
            team2_id = match['matchInfo']['team2']['teamId']
            team1_short = match['matchInfo']['team1']['teamSName']
            team2_short = match['matchInfo']['team2']['teamSName']
            team_VS = f"{team1_name} Vs {team2_name}"
            #check matchscore key :-
            match_score = match.get('matchScore', {})
            #check team1 and 2 score key :-
            team1_data =  match_score.get('team1Score', {}).get('inngs1',{})
            team2_data =  match_score.get('team2Score', {}).get('inngs1',{})
            #extract runs,wickets,overs :-
            team1_runs = team1_data.get('runs','N/A')
            team1_wickets = team1_data.get('wickets','N/A')
            team1_overs = team1_data.get('overs','N/A')
            team2_runs = team2_data.get('runs','N/A')
            team2_wickets = team2_data.get('wickets','N/A')
            team2_overs = team2_data.get('overs','N/A')
            #Create clean scores :-
            team1_score = f"{team1_runs}/{team1_wickets} ({team1_overs})"
            team2_score = f"{team2_runs}/{team2_wickets} ({team2_overs})"
            #print(f"{team1_score},{team2_score}")
            
            # EXTRACTING VENUE/INFO API FOR QN.4 IN SQL:
            url = f"https://cricbuzz-cricket.p.rapidapi.com/venues/v1/{venue_id}"

            headers = {
	                "x-rapidapi-key": RAPIDAPI_KEY,
	                "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	                "Content-Type": "application/json"
            }  

            venue_additional_response = requests.get(url, headers=headers)

            venue_data_new = (venue_additional_response.json())
            country = venue_data_new['country']
            capacity = venue_data_new.get('capacity')

            #solving mysql connection issue:
            #print(team1_id)
            #st.write(match.values())
            #creating insert query for inserting values of players in the teams table:-
            if not mydb.is_connected():
                mydb.reconnect()
            
             # =======================================
             # INSERTING VALUES IN THE TEAMS TABLE:
             # =======================================
            mycursor.execute(
                "SELECT * FROM TEAMS WHERE Team_id = %s",
                (team1_id,)
            )           
                
                
            
            existing_teams = mycursor.fetchone()
            if existing_teams is None:
                mycursor.execute("""
                INSERT INTO TEAMS (Team_id,Team_name,short_name)
                VALUES (%s,%s,%s)
                """,
                (team1_id,team1_name,team1_short)
            )
            
            #Check Team 2
            mycursor.execute(
                "SELECT * FROM TEAMS WHERE Team_id = %s",
                (team2_id,)
            )           
            existing_teams = mycursor.fetchone()
            if existing_teams is None:
                mycursor.execute("""
                INSERT INTO TEAMS (Team_id,Team_name,short_name)
                VALUES (%s,%s,%s)
                """,
                (team2_id,team2_name,team2_short)
            )
            mydb.commit()
            
            # =======================================
            # INSERTING VALUES IN THE MACTHES TABLE:
            # =======================================
            mycursor.execute(
                "SELECT * FROM MATCHES WHERE match_id = %s",
                (match_id,)
            )
            existing_match = mycursor.fetchone()            

                 
            if existing_match:
               mycursor.execute("""
               UPDATE MATCHES
               SET start_date = %s
               WHERE match_id = %s
            """, (start_date, match_id))

               #print("UPDATED ROWS:", mycursor.rowcount)

               mydb.commit()
            
            else:
               mycursor.execute("""
                   INSERT INTO MATCHES
                   (Match_id, Series_name, Description, Format,
                   Team1_id, Team2_id, Venue, City, State, Status, start_date)

                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    match_id,
                    series_name,
                    match_description,
                    match_format,
                    team1_id,
                    team2_id,
                    match_venue,
                    match_city,
                    match_state,
                    match_status,
                    start_date
                   
                )
            )

            mydb.commit()

            mycursor.execute(
                   "SELECT start_date FROM MATCHES WHERE match_id = %s",
                    (match_id,)
            ) 
            result = mycursor.fetchone()
            # print("DB START DATE:", result)

           

            #=======================================
            #INSERTING VALUES IN THE VENUES TABLE:
            #=======================================
            # st.write("DEBUG venue_id:", venue_id)
            # st.write("DEBUG country:", country)
            # st.write("DEBUG capacity:", capacity)

            mycursor.execute(
                "SELECT * FROM VENUES WHERE venue_id = %s",
                (venue_id,)
            )           
            existing_venues = mycursor.fetchone()
            if existing_venues is None:
                mycursor.execute("""
                INSERT INTO VENUES (venue_id, ground, city, timezone, latitude, longitude, country, capacity)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                 (
                    venue_id,
                    match_venue,
                    match_city,
                    timezone,
                    latitude,
                    longitude,
                    country,
                    capacity
                )
                )
            else:

                # st.write("UPDATING VENUE:", venue_id)
                mycursor.execute("""
                    UPDATE VENUES 
                    SET country = %s,
                        capacity = %s
                    WHERE venue_id = %s
                """,
                (
                    country,
                    capacity,
                    venue_id
                ))
            mydb.commit()
                # =======================================
                # INSERTING VALUES IN THE SERIES TABLE:
                # =======================================
            mycursor.execute(
                "SELECT * FROM SERIES WHERE series_id = %s",
                (series_id,)
                )           
                
                
            
            existing_series = mycursor.fetchone()
            if existing_series is None:
                    mycursor.execute("""
                      INSERT INTO SERIES (series_id, series_name)
                      VALUES (%s, %s)
                      """,
                      (
                        series_id,
                        series_name
                      )
                    ) 

            mydb.commit()

                


           



            match_data = {
                "MatchId": match_id,
                "Series_Name" : series_name,
                "City" : match_city,
                "Venue" : match_venue,
                "Team1" : team1_name,
                "Team2" : team2_name,
                "Description" : match_description,
                "Format" : match_format,
                "State" : match_state,
                "Status" : match_status,
                "Score1" : team1_score,
                "Score2" : team2_score,
            }
            all_matches.append(match_data)
            #print(all_matches)

#CREATE DATAFRAME FROM LIST FOR BETTER MANAGEMENT , EASY DISPLAY OF STREAMLIT ,SQL STORAGE ETC.

df = pd.DataFrame(all_matches)
#print(data_frame)
 
#CREATE TITLE ,SUBHEADER :-

st.title("📡 Cricbuzz LiveStats Dashboard")
#st.subheader("All Matches")
#st.dataframe(df)

#SHOW TOTAL MATCHES :-

#st.write("Total matches: ",len(df))

#SEELCT SPECIFIC COLUMNS ONLY :-
# small_df = df[['Team1',"Team2",'Score1']]
# st.dataframe(small_df)

# CREATE DROPDOWN :-

match_options = df['Team1'] + " Vs " + df['Team2']

#DROPDOWN :-

selected_match = st.selectbox(
    "Select a match",
    match_options
)

#FILTER SELECTED MATCH :-
filtered_df = df[df['Team1'] + " Vs " + df['Team2'] == selected_match]
#st.write(filtered_df)

#Take First row :-

match1 = filtered_df.iloc[0]

# st.write(match1['Team1'])
# st.write(match1['Venue'])
##st.write(match1['MatchId'])

#Finding the selected matchId to print the batsmens o only those country or players :-
selected_id = match1['MatchId']
#st.write("selected atch id: ",selected_id)
#Scorecard API extraction :-
url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{selected_id}/scard"

headers = {
	"x-rapidapi-key": RAPIDAPI_KEY,
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)


# print(response.json())

if response.status_code == 200:
    scorecard_data = response.json()
    for innings in scorecard_data["scorecard"]:
      innings_id = (int(innings["inningsid"]))
      runs = int(innings["score"])
      wickets = int(innings["wickets"])
      overs = str(innings["overs"])
      batting_team = (innings["batteamname"])
      selected_id = int(selected_id)
    

       # ---------------- SCORECARD TABLE ----------------
      
      mycursor.execute(
                "SELECT Team_id FROM TEAMS WHERE Team_name = %s",
                (batting_team,)
                )  
      team = mycursor.fetchone()
      if team:
        batting_team_id = int(team[0])
        # st.write("Inside IF block")
        # st.write(batting_team)
        # st.write(batting_team_id)
        
        mycursor.execute("""
           INSERT INTO SCORECARD
           (match_id, innings_id, batting_team_id, runs, wickets, overs)
           VALUES (%s, %s, %s, %s, %s, %s)
           """,
        (
          selected_id,
          innings_id,
          batting_team_id,
          runs,
          wickets,
          overs
        ))
        mydb.commit()

        # ---------------- BATTING TABLE ----------------
        
        for bat_rec in innings["batsman"]:
            player_id = bat_rec["id"]
            player_name = bat_rec["name"]
            balls = bat_rec["balls"]
            fours = bat_rec["fours"]
            sixes = bat_rec["sixes"]
            runs = bat_rec["runs"]
            strike_rate = bat_rec["strkrate"]
            out_description = bat_rec["outdec"]
            
            mycursor.execute("""
              INSERT INTO Batting
              (match_id, innings_id, player_id, player_name, runs, balls, fours, sixes, strike_rate, out_description)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              """,
            (
               selected_id,
               innings_id,
               player_id,
               player_name,
               runs,
               balls,
               fours,
               sixes,
               strike_rate,
               out_description
           ))
            

            mydb.commit()
            
         # ---------------- BOWLING TABLE ----------------

        for bowl_rec in innings["bowler"]:
            player_id = bowl_rec["id"]
            player_name = bowl_rec["name"]
            runs = int(bowl_rec["runs"])
            overs = bowl_rec["overs"]
            maidens = int(bowl_rec["maidens"])
            wickets = int(bowl_rec["wickets"])
            economy = bowl_rec["economy"]

            mycursor.execute("""
            INSERT INTO Bowling
            (match_id, innings_id, player_id, player_name,
            runs, overs, maidens, wickets, economy)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                selected_id,
                innings_id,
                player_id,
                player_name,
                runs,
                overs,
                maidens,
                wickets,
                economy
            ))

        mydb.commit()

    
else:
    st.error(f"No scorecard available. Status Code: {response.status_code}")
    st.stop()
    
    





col1,col2 = st.columns(2)
with col1:
    st.subheader(f"🏏 {match1['Team1']} Vs {match1['Team2']}")
with col2:
    st.info(f"🏆 Series: {match1['Series_Name']}")

st.write(f"🏏 Match: {match1['Description']}")
st.write(f"🎯 Format: {match1['Format']}")
st.write(f"📍 City: {match1['City']}")
st.write(f"🏟️ Venue: {match1['Venue']}")
st.write(f"🔴 Status: {match1['Status']}")
st.write(f"📢 State: {match1['State']}")

#Displaying the innings score of both teams :-

st.header("📊 Current Score")

header_col1,header_col2 = st.columns(2)
with header_col1:
    st.write(f"{match1['Team1']}")
    st.info(f"Innings 1: {match1['Score1']} ")
with header_col2:
    st.write(f"{match1['Team2']}")
    st.success(f"Innings 2: {match1['Score2']} ")


#creating the "detailed scorecard button" :-
if st.button("📋 Click to View Detailed Scorecard"):
    st.header("📊 Innings 1")
    
    all_batsman_i1 = []

    if len(scorecard_data["scorecard"]) == 0:
      st.warning("Scorecard not available for this match yet.")
      st.stop()
    innings1 = scorecard_data["scorecard"][0]
    # st.write(innings1.keys())
    # # st.write(innings1['extras'])
    # # st.write(innings1['score'])
    # st.write(innings1['batsman'])
    
    
    for batsman in innings1['batsman']:
            Batsman = batsman['name']
            Runs = batsman['runs']
            Balls = batsman['balls']
            Fours = batsman['fours']
            Sixes = batsman['sixes']
            score_data = {
                "Batsman" : Batsman,
                "Runs" : Runs,
                "Balls" : Balls,
                "Fours" : Fours,
                "Sixes" : Sixes
            }
            all_batsman_i1.append(score_data)
    batsman1_df = pd.DataFrame(all_batsman_i1)
    #printing the dataframe (e.g df)
    st.dataframe(batsman1_df, hide_index=True)

    #EXTRAS AND TOTAL OF 1st INNINGS:-
    
    st.divider()
    st.header("📊 Extras & Total")
    extras_col1,extras_col2 = st.columns(2)
    with extras_col1:
        st.info(f"Extras: {innings1['extras']['byes']}")
        st.info(f"Legbyes: {innings1['extras']['legbyes']}")
        st.info(f"Wides: {innings1['extras']['wides']}")
        st.info(f"Noballs: {innings1['extras']['noballs']}")
        st.info(f"Penalty: {innings1['extras']['penalty']}")
    with extras_col2:
        st.success(f"Total Extras: {innings1['extras']['total']}")
        st.success(f"Total Score: {innings1['score']}")
    
    #BATSMEN SCORE OF INNINGS 2 :-
    
    st.divider()
    st.header("📊 Innings 2")

    #Checking wheather the second innigs exists in the scorecard list :-

    if (len(scorecard_data['scorecard']) > 1):
        innings2 = scorecard_data['scorecard'][1]
        all_batsman_i2 = []
        #Checking the keys in the 1st index position of scorecard list:-
        # #st.write(innings2['score'])
        # #st.write(innings2[''])
        for batsman_i2 in innings2['batsman']:
            Batsmani2 = batsman_i2['name']
            Runsi2 = batsman_i2['runs']
            Ballsi2 = batsman_i2['balls']
            Foursi2 = batsman_i2['fours']
            Sixesi2 = batsman_i2['sixes']
            score_data_innings_2 = {
                "Batsman" : Batsmani2,
                "Runs" : Runsi2,
                "Balls" : Ballsi2,
                "Fours" : Foursi2,
                "Sixes" : Sixesi2
            }
            all_batsman_i2.append(score_data_innings_2)
        batsman2_df = pd.DataFrame(all_batsman_i2)
        #printing the dataframe (e.g df)
        st.dataframe(batsman2_df, hide_index=True)

        #EXTRAS AND TOTAL OF 2nd INNINGS:-
    
        st.divider()
        st.header("📊 Extras & Total")
        extras_col1_i2,extras_col2_i2 = st.columns(2)
        with extras_col1_i2:
            st.info(f"Extras: {innings2['extras']['byes']}")
            st.info(f"Legbyes: {innings2['extras']['legbyes']}")
            st.info(f"Wides: {innings2['extras']['wides']}")
            st.info(f"Noballs: {innings2['extras']['noballs']}")
            st.info(f"Penalty: {innings2['extras']['penalty']}")
        with extras_col2_i2:
            st.success(f"Total Extras: {innings2['extras']['total']}")
            st.success(f"Total Score: {innings2['score']}")
    else:
        st.info("Second Innings has not started yet")   
    
    
st.divider()
st.subheader("📱 About This Dashboard")
st.write("This comprehensive Cricket Dashboard demonstrates:")
st.markdown("""
    - API Integration: Real-time data from Cricbuzz AP Database Operations.
    - MySQL with full CRUD functionality Data 
    - Analysis: 20 different SQL analytics queries.
    - Interactive Ut: Streamlit components with caching Player Statistics.
    - Detailed batting and bowling stats.
    """)





        
        


  

