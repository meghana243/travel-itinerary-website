import streamlit as st
import pandas as pd

# Sample travel blog data with more entries
data = {
    "title": ["Exploring Paris", "Adventures in Bali", "Discovering Tokyo"],
    "author": ["John Doe", "Jane Smith", "Alice Johnson"],
    "date": ["2024-01-01", "2024-02-15", "2024-03-10"],
    "content": [
        "Paris, the City of Light, is an enchanting destination that captivates visitors with its timeless beauty, rich history, and vibrant culture. From its iconic landmarks to its charming streets, every corner of Paris offers something unique and magical.No visit to Paris is complete without a trip to the Eiffel Tower. This iconic structure, standing tall over the city, offers breathtaking views from its observation decks. Whether you visit during the day or night, the Eiffel Tower never fails to impress.",
        "Bali, Indonesia’s renowned island paradise, beckons travelers with its diverse landscapes, rich culture, and warm hospitality. Nestled in the heart of the Indonesian archipelago, Bali offers a blend of serene beaches, lush jungles, and vibrant cultural experiences that leave an indelible mark on every visitor.",
        "Tokyo, Japan’s bustling capital, is a dynamic metropolis that seamlessly blends ancient traditions with cutting-edge technology. Renowned for its skyscrapers, historic temples, and vibrant neighborhoods, Tokyo offers a captivating journey through Japanese culture, cuisine, and creativity.",
       
    ],
    "image_url": [
        "paris.jpg",  # Replace with actual image URLs
        "bali.jpg",
        "tokyo.jpg",
       
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
