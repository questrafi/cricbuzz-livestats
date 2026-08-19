import streamlit as st
import pandas as pd
from db_connection import mydb,mycursor 


# Sidebar information box
st.sidebar.markdown("""
<div style="background-color: #294C6F; padding: 15px; border-radius: 8px; color: white;">
<b>CRUD Operations Page:</b>
<ul>
<li>Create new player records</li>
<li>Read and search existing players</li>
<li>Update player information</li>
<li>Delete player records</li>
</ul>
</div>
""", unsafe_allow_html=True)

#Setting the title for the page:-
st.title("🔧 CRUD Operations")

st.subheader("📝 Create, Read, Update, Delete Player Records")

#create the dropdown :-
operation = st.selectbox(
    "Choose an operation",
    ["Create", "Read", "Update", "Delete"]
)

#create a form to get the values:-

#====================
     #CREATE
#=====================

if operation == "Create":
    st.subheader("➕ Add New Player")
    with st.form("create_player"):
        player_id = st.number_input("Player ID",min_value=1, step=1)
        player_name = st.text_input("Player Name")
        matches = st.number_input("Matches",min_value=0, step=1)
        innings = st.number_input("Innings",min_value=0, step=1)  
        runs = st.number_input("Runs",min_value=0, step=1)        
        average = st.number_input("Average",min_value=0.0, step=0.01)
        submit = st.form_submit_button("Add Player")

        if submit:
            mydb.ping(reconnect=True,attempts=3,delay=2)
            mycursor.execute("""
            INSERT INTO player_records 
            (player_id, player_name, matches, innings, runs, average)	
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                player_id,
                player_name,
                matches,
                innings,
                runs,
                average
             ))
            mydb.commit()
            st.success("✅ Player Successfully")

#====================
     #READ
#=====================

if operation == "Read":
    st.subheader("📋 Player Records")
    mycursor.execute("SELECT * FROM player_records")
    data = mycursor.fetchall()
    cols = [
        "Player ID",
        "Player Name",
        "Matches",
        "Innings",
        "Runs",
        "Average"

    ]
    df = pd.DataFrame(data,columns=cols)
    #displaying the dataframe
    st.dataframe(df)

# ====================
# UPDATE
# ====================

if operation == "Update":

    st.subheader("✏️ Update Player")

    # Create session state only once
    if "player" not in st.session_state:
        st.session_state["player"] = None

    # Search Player
    player_id = st.number_input(
        "Enter Player ID",
        min_value=1,
        step=1
    )

    search_btn = st.button("Search")

    if search_btn:

        mydb.ping(reconnect=True, attempts=3, delay=2)

        mycursor.execute("""
            SELECT *
            FROM player_records
            WHERE player_id = %s
        """, (player_id,))

        player = mycursor.fetchone()

        if player:
            st.session_state["player"] = player
        else:
            st.session_state["player"] = None
            st.warning("❌ No player found with this ID.")

    # Show form only if player is found
    if st.session_state["player"] is not None:

        player = st.session_state["player"]

        st.info(f"""
Current Information

Player ID : {player[0]},
Player Name : {player[1]},
Matches : {player[2]},
Innings : {player[3]},
Runs : {player[4]},
Average : {player[5]}
""")

        with st.form("update_form"):

            new_name = st.text_input(
                "Player Name",
                value=player[1]
            )

            new_matches = st.number_input(
                "Matches",
                min_value=0,
                step=1,
                value=player[2]
            )

            new_innings = st.number_input(
                "Innings",
                min_value=0,
                step=1,
                value=player[3]
            )

            new_runs = st.number_input(
                "Runs",
                min_value=0,
                step=1,
                value=player[4]
            )

            new_average = st.number_input(
                "Average",
                min_value=0.0,
                step=0.01,
                value=float(player[5])
            )

            update_btn = st.form_submit_button("Update Player")

            if update_btn:

                mydb.ping(reconnect=True, attempts=3, delay=2)

                mycursor.execute("""
                    UPDATE player_records
                    SET
                        player_name = %s,
                        matches = %s,
                        innings = %s,
                        runs = %s,
                        average = %s
                    WHERE player_id = %s
                """,
                (
                    new_name,
                    new_matches,
                    new_innings,
                    new_runs,
                    new_average,
                    player[0]
                ))

                mydb.commit()

                st.success("✅ Player updated successfully!")

                # Refresh session state
                st.session_state["player"] = (
                    player[0],
                    new_name,
                    new_matches,
                    new_innings,
                    new_runs,
                    new_average
                )

# ====================
# DELETE
# ====================

if operation == "Delete":

    st.subheader("🗑️ Delete Player Record")

    st.warning("⚠️ Warning: This action cannot be undone!")

    search_name = st.text_input("🔍 Search player to delete")

    # Search only after the user types something
    if search_name:

        mydb.ping(reconnect=True, attempts=3, delay=2)

        mycursor.execute("""
            SELECT *
            FROM player_records
            WHERE player_name LIKE %s
        """, (f"%{search_name}%",))

        players = mycursor.fetchall()

        if players:

            player_options = []

            for player in players:
                player_options.append(
                    f"{player[1]} (ID: {player[0]}) - {player[4]} Runs"
                )

            selected_option = st.selectbox(
                "Select Player",
                player_options
            )

            # Find the selected player
            selected_player = None

            for player in players:
                option = f"{player[1]} (ID: {player[0]}) - {player[4]} Runs"

                if option == selected_option:
                    selected_player = player
                    break

            st.error(
                f"⚠️ You are about to delete '{selected_player[1]}'. This action cannot be undone!"
            )

            confirm = st.text_input(
                f"Type DELETE {selected_player[1]} to confirm"
            )

            if confirm == f"DELETE {selected_player[1]}":

                if st.button("🗑️ Delete Player"):

                    mydb.ping(reconnect=True, attempts=3, delay=2)

                    mycursor.execute("""
                        DELETE FROM player_records
                        WHERE player_id = %s
                    """, (selected_player[0],))

                    mydb.commit()

                    st.success("✅ Player deleted successfully!")

            elif confirm != "":
                st.error("❌ Confirmation text does not match.")

        else:
            st.warning("❌ No player found with that name.")

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

                            
                             