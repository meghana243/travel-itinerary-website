import streamlit as st

st.set_page_config(page_title="Travel Itinerary", page_icon="🗺️")

st.title("Welcome to the Travel Itinerary Website")

st.sidebar.header("Navigation")
st.sidebar.button("Home", on_click=lambda: st.experimental_set_query_params(page="home"))
st.sidebar.button("Travel", on_click=lambda: st.experimental_set_query_params(page="travel"))
st.sidebar.button("Blogs", on_click=lambda: st.experimental_set_query_params(page="blogs"))

query_params = st.experimental_get_query_params()

if "page" in query_params:
    if query_params["page"][0] == "home":
        st.write("Welcome to the home page of the Travel Itinerary Website!")
    elif query_params["page"][0] == "travel":
        st.write("This is the travel page where you can find travel itineraries.")
    elif query_params["page"][0] == "blogs":
        # Sample travel blog data with more entries
        import pandas as pd

        data = {
            "title": ["Exploring Paris", "Adventures in Bali", "Discovering Tokyo", "Journey through the Swiss Alps"],
            "author": ["John Doe", "Jane Smith", "Alice Johnson", "Michael Brown"],
            "date": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05"],
            "content": [
                "Paris is an amazing city with a rich history...",
                "Bali is a beautiful island in Indonesia...",
                "Tokyo is a bustling metropolis with a unique blend of tradition and modernity...",
                "The Swiss Alps offer breathtaking views and exhilarating outdoor activities..."
            ],
            "image_url": [
                "https://example.com/paris.jpg",  # Replace with actual image URLs
                "https://example.com/bali.jpg",
                "https://example.com/tokyo.jpg",
                "https://example.com/swiss_alps.jpg"
            ]
        }

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Set the title of the app
        st.title('Travel Blogs')

        # Display the blogs
        for index, row in df.iterrows():
            st.header(row['title'])
            st.subheader(f"by {row['author']} on {row['date']}")
            st.write(row['content'])
            st.image(row['image_url'], caption=row['title'], use_column_width=True)
            st.markdown("---")  # Add a horizontal line between blogs
else:
    st.write("Welcome to the home page of the Travel Itinerary Website!")
