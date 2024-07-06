import streamlit as st
from datetime import date, timedelta
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Travel Itinerary", page_icon="🗺️")

# Sample points of interest data
poi_data = {
    "India": [
        {"name": "Taj Mahal", "location": [27.1751, 78.0421]},
        {"name": "Rajasthan", "location": [27.0238, 74.2179]},
        {"name": "Rishikesh", "location": [30.0869, 78.2676]},
        {"name": "Red Fort", "location": [28.6562, 77.2410]},
        {"name": "Qutub Minar", "location": [28.5245, 77.1855]},
        {"name": "Gateway of India", "location": [18.9220, 72.8347]},
        {"name": "Kerala Backwaters", "location": [9.6030, 76.1664]},
        {"name": "Hawa Mahal", "location": [26.9239, 75.8267]},
        {"name": "Goa Beaches", "location": [15.2993, 74.1240]},
        {"name": "Mysore Palace", "location": [12.3052, 76.6551]},
        {"name": "Ajanta and Ellora Caves", "location": [20.5537, 75.7033]},
        {"name": "Varanasi Ghats", "location": [25.2820, 83.0061]},
        {"name": "Hampi", "location": [15.3350, 76.4600]},
        {"name": "Leh Ladakh", "location": [34.1526, 77.5770]},
        {"name": "Amritsar Golden Temple", "location": [31.6200, 74.8765]},
        {"name": "Sundarbans", "location": [21.9497, 89.1833]},
        {"name": "Kaziranga National Park", "location": [26.5775, 93.1714]},
        {"name": "Ranthambore National Park", "location": [26.0173, 76.5026]},
        {"name": "Meenakshi Temple", "location": [9.9194, 78.1194]},
        {"name": "Sikkim", "location": [27.5330, 88.5122]}
    ],
    "New York": [
        {"name": "Statue of Liberty", "location": [40.6892, -74.0445]},
        {"name": "Central Park", "location": [40.7851, -73.9683]},
        {"name": "Broadway", "location": [40.7590, -73.9845]}
    ],
    "Paris": [
        {"name": "Eiffel Tower", "location": [48.8584, 2.2945]},
        {"name": "Louvre Museum", "location": [48.8606, 2.3376]},
        {"name": "Seine River", "location": [48.8566, 2.3522]}
    ],
    "Tokyo": [
        {"name": "Senso-ji Temple", "location": [35.7148, 139.7967]},
        {"name": "Akihabara", "location": [35.7023, 139.7745]},
        {"name": "Mount Fuji", "location": [35.3606, 138.7274]},
        {"name": "Shibuya Crossing", "location": [35.6595, 139.7005]},
        {"name": "Tokyo Tower", "location": [35.6586, 139.7454]}
    ],
    "Sydney": [
        {"name": "Sydney Opera House", "location": [33.8568, 151.2153]},
        {"name": "Bondi Beach", "location": [33.8908, 151.2743]},
        {"name": "Sydney Harbour Bridge", "location": [33.8523, 151.2108]},
        {"name": "Taronga Zoo", "location": [33.8436, 151.2411]},
        {"name": "The Rocks", "location": [33.8599, 151.2093]}
    ],
    "Cape Town": [
        {"name": "Table Mountain", "location": [33.9628, 18.4098]},
        {"name": "Robben Island", "location": [33.8060, 18.3684]},
        {"name": "V&A Waterfront", "location": [33.9072, 18.4208]},
        {"name": "Kirstenbosch National Botanical Garden", "location": [33.9881, 18.4325]},
        {"name": "Cape Point", "location": [34.3568, 18.4954]}
    ],
    "Rio de Janeiro": [
        {"name": "Christ the Redeemer", "location": [-22.9519, -43.2105]},
        {"name": "Sugarloaf Mountain", "location": [-22.9482, -43.1565]},
        {"name": "Copacabana Beach", "location": [-22.9711, -43.1822]},
        {"name": "Ipanema Beach", "location": [-22.9839, -43.2075]},
        {"name": "Tijuca National Park", "location": [-22.9651, -43.2293]}
    ],
    "Istanbul": [
        {"name": "Hagia Sophia", "location": [41.0086, 28.9802]},
        {"name": "Blue Mosque", "location": [41.0054, 28.9768]},
        {"name": "Topkapi Palace", "location": [41.0115, 28.9831]},
        {"name": "Grand Bazaar", "location": [41.0106, 28.9680]},
        {"name": "Basilica Cistern", "location": [41.0084, 28.9784]}
    ],
    "Rome": [
        {"name": "Colosseum", "location": [41.8902, 12.4922]},
        {"name": "Vatican City", "location": [41.9029, 12.4534]},
        {"name": "Pantheon", "location": [41.8986, 12.4769]},
        {"name": "Trevi Fountain", "location": [41.9009, 12.4833]},
        {"name": "Roman Forum", "location": [41.8925, 12.4853]}
    ],
    "Bangkok": [
        {"name": "Grand Palace", "location": [13.7500, 100.4913]},
        {"name": "Wat Arun", "location": [13.7437, 100.4880]},
        {"name": "Chatuchak Market", "location": [13.8150, 100.5562]},
        {"name": "Jim Thompson House", "location": [13.7461, 100.5296]},
        {"name": "Lumphini Park", "location": [13.7302, 100.5416]}
    ],
    "London": [
        {"name": "Tower of London", "location": [51.5081, -0.0759]},
        {"name": "British Museum", "location": [51.5194, -0.1270]},
        {"name": "Buckingham Palace", "location": [51.5014, -0.1419]},
        {"name": "London Eye", "location": [51.5033, -0.1196]},
        {"name": "Big Ben", "location": [51.5007, -0.1246]}
    ]
}

def create_map(destination, selected_poi=None):
    if destination not in poi_data:
        st.error(f"No data available for {destination}")
        return None, []

    first_poi = poi_data[destination][0]["location"]
    travel_map = folium.Map(location=first_poi, zoom_start=12)

    for poi in poi_data[destination]:
        folium.Marker(
            location=poi["location"],
            popup=poi["name"],
            tooltip=poi["name"],
            icon=folium.Icon(color="blue" if poi["name"] != selected_poi else "red")
        ).add_to(travel_map)

    if selected_poi:
        for poi in poi_data[destination]:
            if poi["name"] == selected_poi:
                folium.Marker(
                    location=poi["location"],
                    popup=poi["name"],
                    tooltip=poi["name"],
                    icon=folium.Icon(color="red")
                ).add_to(travel_map)
                travel_map.location = poi["location"]

    return travel_map, [poi["name"] for poi in poi_data[destination]]

def main():
    st.video('travelling.mp4')
    st.title("WanderPlan")

    st.sidebar.title("Input Trip Details")
    destinations = list(poi_data.keys())

    with st.sidebar.form("itinerary_form"):
        st.image('logo1.png')
        trip_name = st.text_input("Trip Name", "My Awesome Trip")
        start_date = st.date_input("Start Date", date.today())
        end_date = st.date_input("End Date", date.today())
        destination = st.selectbox("Destination", destinations)
        submit = st.form_submit_button("Save Itinerary")
        
    if submit:
        st.session_state.trip_name = trip_name
        st.session_state.start_date = start_date
        st.session_state.end_date = end_date
        st.session_state.destination = destination
        st.session_state.selected_poi = None

    if "trip_name" in st.session_state:
        st.subheader(f"Trip: {st.session_state.trip_name}")
        st.write(f"Destination: {st.session_state.destination}")
        st.write(f"Start Date: {st.session_state.start_date}")
        st.write(f"End Date: {st.session_state.end_date}")
        


        poi_names = [poi["name"] for poi in poi_data[st.session_state.destination]]
        selected_poi = st.sidebar.selectbox("Select Point of Interest", poi_names)

        if st.session_state.selected_poi != selected_poi:
            st.session_state.selected_poi = selected_poi

        travel_map, _ = create_map(st.session_state.destination, st.session_state.selected_poi)
        folium_static(travel_map)
        
        days = (st.session_state.end_date - st.session_state.start_date).days + 1
        itinerary = {}
        for i in range(days):
            day = st.session_state.start_date + timedelta(days=i)
            with st.expander(f"Day {i + 1} ({day.strftime('%Y-%m-%d')})"):
                activities = st.text_area(f"Activities for Day {i + 1}", key=f"day_{i}")
                itinerary[day.strftime('%Y-%m-%d')] = activities

        uploaded_file = st.file_uploader("We keep this love in a photograph🎶", type=['png', 'jpeg', 'jpg'])
        st.write("Upload your files")
        if uploaded_file is not None:
            st.image(uploaded_file)

        if st.button("Save All"):
            st.write("Itinerary Saved!")
            for day, activities in itinerary.items():
                st.write(f"**{day}**: {activities}")

    

if __name__ == "__main__":
    main()
