import streamlit as st
import pandas as pd
import requests
from db_connection import mydb,mycursor
import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# Sidebar information box
st.sidebar.markdown("""
<div style="background-color: #294C6F; padding: 15px; border-radius: 8px; color: white;">
<b>Player Stats Page:</b>
<ul>
<li>Search any cricket player</li>
<li>Career statistics across formats</li>
<li>Comprehensive player profiles</li>
</ul>
</div>
""", unsafe_allow_html=True)


#st.write("HELLO FROM PLAYER STATS PAGE")
st.title("👤Cricket Player Statistics")
st.header("🔍 Search a player")

player_name = st.text_input("Enter a player name")
if st.button("🔍 Search"):
    st.success(f"Player found : {player_name}")
    st.session_state.search_clicked = True
if st.session_state.get("search_clicked",False):
    
    

    
    #API extraction for searching the player's id and name :-
    
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"

    querystring = {"plrN":player_name}

    headers = {
	"x-rapidapi-key": RAPIDAPI_KEY,
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
    }
    #Use different names instead of "response" variable as many many API's are extracted and confusion can occur :-

    search_response = requests.get(url, headers=headers, params=querystring)
    #convert API to json :-
    data = (search_response.json())
    #st.write(data)
    #Display pyhton data nicely on the webpage :-
    #st.json(data['player'])
    
    if "player" not in data:
        st.error("No players found or API returned an unexpected response.")
        st.write(data)
        st.stop()
    players = data['player']
    st.header(f"Found {len(players)} players matching '{player_name}'")
    #Storing all the player names in a list that streamlit can show in a dropdown:-
    player_options = []
    for player in players:
        #Append the name and the team of all the players with similar name:-
        player_options.append(f"{player['name']} - {player['teamName']}")
         
    #Create the dropdown :-
    selected_player = st.selectbox(
        "Select a player:",
        player_options
    )
    selected_player_id = None
    for player in players:
        if (selected_player == f"{player['name']} - {player['teamName']}"):
            selected_player_id = player['id']
            break
    



    #storing the selected player 's id :-
    # selected_player_id = data['player'][0]['id']
    # st.json(data)
    #Creating another URL to prevent NameError (while giving in the url) :-
    

    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player_id}"

    headers = {
	"x-rapidapi-key": "b0102cb292msh23226301ff12009p19a043jsn677d85b2be33",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
    }

    player_response = requests.get(url, headers=headers)

    player_info_data = (player_response.json())
    #st.write(player_response.status_code)
    #st.write(player_info_data)
    #st.json(player_info_data.keys())
    #st
    #Diaplying name of the player :-
    st.header(f"📊 {player_name} - Player Profile")
    #st.write(f"{player_info_data['role']}")

    #Creating 3 tabs or sections for profile,batting,bowling :-
    tab1,tab2,tab3 = st.tabs(
        ["👤 Profie","🏏 Batsman Stats","⚡Bowling Stats"]
    )
    with tab1:
        st.header("🎯 Personel Information")
        cricket_details,personal_details,Teams_Played_For = st.columns(3)
        with cricket_details:
            #st.write(player_info_data)
            player_id = player_info_data.get("player_id","Not Available")
            player_name = player_info_data.get("player_name","Not Available")
            role = player_info_data.get("role","Not Available")
            bat = player_info_data.get("bat","Not Available")
            bowl = player_info_data.get("bowl","Not Available")
            intl_team = player_info_data.get("intl_team","Not Available")
            dob = player_info_data.get("dob","Not Available")
            birth_place = player_info_data.get("birth_place","Not Available")

             # =======================================
             # INSERTING VALUES IN THE PLAYERS4 TABLE:
             # =======================================
            mycursor.execute(
                "SELECT * FROM PLAYERS4 WHERE player_id = %s",
                (player_id,)

            )
            existing_player = mycursor.fetchone()

            if existing_player is None:
                mycursor.execute("""
                             INSERT INTO PLAYERS4 
                             (player_id,player_name,role,bat,bowl,intl_team,dob,birth_place)
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                             
                             """,
                             (
                                 player_id,
                                 player_name,
                                 role,
                                 bat,
                                 bowl,
                                 intl_team,
                                 dob,
                                 birth_place
                             )
                             
                             
                             
                             )
                mydb.commit()
            # else:
            #     st.info("Player already existed in the database")






            st.write("🏏 Cricket Details")
            st.write(f"Role: {player_info_data.get('role','Not available')}")
            st.write(f"Batting: {player_info_data.get('bat','Not available')}")
            st.write(f"Bowling: {player_info_data.get('bowl','Not available')}")
            st.write(f"International Team: {player_info_data.get('intlTeam','Not available')}")
        with personal_details:
            st.write("📍 Personal Details")
            st.write(f"Date of Birth: {player_info_data.get('DoB','Not available')}")
            st.write(f"Birth Place: {player_info_data.get('birthPlace','Not available')}")
        with Teams_Played_For:
            st.write("🏆 Teams Played For")
            teams = player_info_data['teamNameIds']
            #st.write(player_info_data['teamNameIds'])
             
            for teamname_id_s in teams[0:7]:
                #check if the key "teamName" exists in all the key-values (as error throwed when "Raina" is typed) :-
                teamname = teamname_id_s.get('teamName')
                # st.write(teamname)
                if teamname:
                    #teamname becomes none if there is no key,else it will be true and the below code will execute :- 
                    st.markdown(f"- {teamname}")

            
            with st.expander(f"Show remaining {max(0,len(teams) - 7)} teams "):
                for teamname_id_s in teams[7:]:
                  #check if the key "teamName" exists in all the key-values (as error throwed when "Raina" is typed) :-
                  teamname = teamname_id_s.get('teamName')
                   # st.write(teamname)
                  if teamname:
                    #teamname becomes none if there is no key,else it will be true and the below code will execute :- 
                    st.markdown(f"- {teamname}") 
        with tab2:
            st.header("🏏 Batting Career Statistics")
            st.subheader("📊 Career Overview")
            #importing the players/batting endpoint to extract and print the batting stats :-
            




            url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player_id}/batting"
            
            headers = {
	          "x-rapidapi-key": RAPIDAPI_KEY,
	          "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	          "Content-Type": "application/json"
            }
            batting_response = requests.get(url, headers=headers)

            # st.write("STATUS:", batting_response.status_code)
            # st.write("RESPONSE:", batting_response.text)
            
            if batting_response.status_code == 204:
                st.warning("No batting or bowling statistics available for this player.")
                st.stop()

            batting_data = batting_response.json()
            #st.json(batting_data)


            column_headers = batting_data['headers']
            batting_rows = []
            for item in batting_data['values']:
                batting_rows.append(item['values'])
            batting_table_df = pd.DataFrame(batting_rows)
            #st.write(batting_rows)
            #st.dataframe(table_df,hide_index=True)
            batting_overview_df = (batting_table_df.iloc[[0,2,5,6],[0,1,2,3,4]])
            batting_overview_df.columns=([
                "Format",
                "Test",
                "ODI",
                "T20",
                "IPL"
            ])
            st.dataframe(batting_overview_df,hide_index=True)
            #st.dataframe(table_df,hide_index=True)
            st.subheader("📈 Detailed Batting Statistics")
            batting_detailed_df = (batting_table_df.iloc[[0,1,2,3,4,5,11,12],[0,1,2,3,4]])
            batting_detailed_df.columns=([
                "Statistics",
                "Test",
                "ODI",
                "T20",
                "IPL"
            ])
            st.dataframe(batting_detailed_df,hide_index=True) 
        with tab3:
            st.header("⚡ Bowling Career Statistics")
            

            url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{selected_player_id}/bowling"

            headers = {
	           "x-rapidapi-key": RAPIDAPI_KEY,
	           "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	           "Content-Type": "application/json"
            }

            bowling_response = requests.get(url, headers=headers)
            if bowling_response.status_code == 204:
                st.warning("No bowling statistics available for this player.")
                st.stop()

            bowling_data = bowling_response.json()
            #st.json(bowling_data)
            bowling_rows = []
            for bowling_item in bowling_data['values']:
                bowling_rows.append(bowling_item['values'])
            bowling_table_df = pd.DataFrame(bowling_rows)
            #st.write(bowling_rows)
            #st.dataframe(bowling_table_df,hide_index=True)
            st.subheader("📊 Career Overview")
            bowling_overview_df = (bowling_table_df.iloc[[0,5,6,7],[0,1,2,3,4]])
            bowling_overview_df.columns=([
                "Format",
                "Test",
                "ODI",
                "T20",
                "IPL"
            ])
            st.dataframe(bowling_overview_df,hide_index=True)
            #st.dataframe(table_df,hide_index=True)
            st.subheader("📈 Detailed Bowling Statistics")
            bowling_detailed_df = (bowling_table_df.iloc[0:9,[0,1,2,3,4]])
            bowling_detailed_df.columns=([
                "Statistics",
                "Test",
                "ODI",
                "T20",
                "IPL"
            ])
            st.dataframe(bowling_detailed_df,hide_index=True)
   

            ###Three tabs or sections finished in the second page :-
             #creating the profile page link:-
        profile_url = batting_data['appIndex']['webURL']
        #st.json(batting_data)
        st.write(f"Full Profile: {profile_url}")
        #st.link_button("🌐 Full Profile:", profile_url)
    

    #"About the Dashboard" section" :-

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

            





    





    

