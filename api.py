import requests
import pandas as pd
#import json
#from pprint import pprint
url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
	"x-rapidapi-key": "777c1dc328mshaa6c85b7f3dd8cap1909e6jsnbb8cbc134664",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

data = (response.json())
#print(type(data))
#print(data.keys())


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



##LOOPING THROUGHT TYPEMATCHES TO PRINT ALL MATCHE'S VALUES :-

all_matches = []
for match_type in data['typeMatches']:
    for series in match_type['seriesMatches']:
        if 'seriesAdWrapper' not in series:
            continue #if there are no adwropper in any series e.g native-mtches
        info_match = series['seriesAdWrapper']['matches']
        for match in info_match:
            series_name = match['matchInfo']['seriesName']
            match_description = match['matchInfo']['matchDesc']
            match_format = match['matchInfo']['matchFormat']
            match_state = match['matchInfo']['state']
            match_status = match['matchInfo']['status']
            match_venue = match['matchInfo']['venueInfo']['ground']
            match_city = match['matchInfo']['venueInfo']['city']
            team1_name = match['matchInfo']['team1']['teamName']
            team2_name = match['matchInfo']['team2']['teamName']
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
            print(f"{team1_score},{team2_score}")

            match_data = {
                "Series_Name" : series_name,
                "city" : match_city,
                "venue" : match_venue,
                "team1" : team1_name,
                "team2" : team2_name,
                "Description" : match_description,
                "Format" : match_format,
                "score1" : team1_score,
                "state" : match_state,
                "score2" : team2_score,
            }
            all_matches.append(match_data)
            #print(all_matches)

#CREATE DATAFRAME FROM LIST FRO BETTER MANAGEMENT , EASY DISPLAY OF STREAMLIT ,SQL STORAGE ETC.

data_frame = pd.DataFrame(all_matches)
print(data_frame)


