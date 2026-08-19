import streamlit as st
import pandas as pd
from db_connection import mydb, mycursor

# Sidebar information box
st.sidebar.markdown("""
<div style="background-color: #294C6F; padding: 15px; border-radius: 8px; color: white;">
<b>SQL Analytics Page:</b>
<ul>
<li>20 practice SQL questions</li>
<li>Interactive query execution</li>
<li>Real cricket database</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.title("📊 Cricket SQL Queries")

st.subheader("🏏 Run SQL Queries on Player Records")

st.write("Select a question to analyze:")

# Create a query list to insert in the selectbox
query_list = [
    '1. Find all players who represent India',
    '2. Show all cricket matches that were played in the last few days',
    '3. List the top 10 highest run scorers in ODI cricket',
    '4. Display all cricket venues that have a seating capacity of more than 25,000 spectators',
    '5. Calculate how many matches each team has won',
    '6. Count how many players belong to each playing role (like Batsman, Bowler, All-rounder, Wicket-keeper).',
    '7. Find the highest individual batting score achieved in each cricket format (Test, ODI, T20I)',
    '8. Show all cricket series that started in the year 2024',
    '9. Find all-rounder players who have scored more than 1000 runs AND taken more than 50 wickets in their career.',
    '10. Get details of the last 20 completed matches',
    "11. Compare each player's performance across different cricket formats",
    "12. Analyze each international team's performance when playing at home versus playing away.",
    '13. Identify batting partnerships where two consecutive batsmen (batting positions next to each other) scored a combined total of 100 or more runs',
    '14. Examine bowling performance at different venues.',
    '15. Identify players who perform exceptionally well in close matches.',
    "16. Track how players' batting performance changes over different years.",
    '17. Investigate whether winning the toss gives teams an advantage in winning matches.',
    '18. Find the most economical bowlers in limited-overs cricket (ODI and T20 formats).',
    '19. Determine which batsmen are most consistent in their scoring',
    '20. Analyze how many matches each player has played in different cricket formats',
    '21. Create a comprehensive performance ranking system for players.',
    '22. Build a head-to-head match prediction analysis between teams.',
    '23. Analyze recent player form and momentum.',
    '24. Study successful batting partnerships to identify the best player combinations',
    '25. Perform a time-series analysis of player performance evolution.'
]


# Create dropdown for selecting a query
selected_query = st.selectbox(
    'Select a question',
    query_list
)


# -------------------------------------------------
# GET THE QUESTION NUMBER
# -------------------------------------------------

query_number = int(selected_query.split(".")[0])


# -------------------------------------------------
# SQL QUERIES
# -------------------------------------------------

sql_queries = {

    1: """
    SELECT player_name,role,bat,bowl FROM players4 WHERE intl_team = 'India';
    """,

    2: """
    SELECT
        m.Description AS match_description,
        t1.Team_name AS team1,
        t2.Team_name AS team2,
        CONCAT(m.Venue, ', ', m.City) AS venue,
        CASE
            WHEN m.start_date > 100000000000
                THEN FROM_UNIXTIME(m.start_date / 1000)
            ELSE FROM_UNIXTIME(m.start_date)
        END AS match_date
    FROM matches m
    JOIN teams t1
        ON m.Team1_id = t1.Team_id
    JOIN teams t2
        ON m.Team2_id = t2.Team_id
    WHERE
        CASE
            WHEN m.start_date > 100000000000
                THEN FROM_UNIXTIME(m.start_date / 1000)
            ELSE FROM_UNIXTIME(m.start_date)
        END >= NOW() - INTERVAL 7 DAY
    ORDER BY m.start_date DESC;
    """,

    3: """
    SELECT
        b.player_name,
        SUM(b.runs) AS total_runs,
        ROUND(AVG(b.runs), 2) AS batting_average,
        SUM(
            CASE
                WHEN b.runs >= 100 THEN 1
                ELSE 0
            END
        ) AS centuries
    FROM batting b
    JOIN matches m
        ON b.match_id = m.Match_id
    WHERE m.Format = 'ODI'
    GROUP BY b.player_id, b.player_name
    ORDER BY total_runs DESC
    LIMIT 10;
    """,

    6: """
    SELECT role, COUNT(*) AS player_count
    FROM players4
    GROUP BY role
    ORDER BY player_count DESC;
    """,

    7: """
    SELECT
        m.Format AS cricket_format,
        MAX(b.runs) AS highest_score
    FROM batting b
    JOIN matches m
        ON b.match_id = m.Match_id
    WHERE m.Format IN ('TEST', 'ODI', 'T20')
    GROUP BY m.Format
    ORDER BY
        CASE m.Format
            WHEN 'TEST' THEN 1
            WHEN 'ODI' THEN 2
            WHEN 'T20' THEN 3
        END;
    """
}


# -------------------------------------------------
# SHOW SELECTED QUERY
# -------------------------------------------------

# st.subheader("Selected Query")

st.subheader(selected_query)


# -------------------------------------------------
# VIEW SQL QUERY
# -------------------------------------------------

with st.expander("🔍 View SQL Query"):

    if query_number in sql_queries:
        st.code(sql_queries[query_number], language="sql")

    else:
        st.info("SQL query is not available because there is insufficient data for this analysis.")


# -------------------------------------------------
# EXECUTE QUERY
# -------------------------------------------------

if st.button("▶ Execute Query"):

    if query_number not in sql_queries:

        st.warning(
            "Insufficient data available for this analysis."
        )

    else:

        sql = sql_queries[query_number]

        try:

            mycursor.execute(sql)

            result = mycursor.fetchall()

            # Get column names
            columns = [column[0] for column in mycursor.description]

            df = pd.DataFrame(result, columns=columns)

            st.success("Query executed successfully!")

            st.dataframe(df)

        except Exception as e:

            st.error(f"Error executing query: {e}")


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
