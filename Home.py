# import streamlit as st
# import pandas as pd

# # Load halal recipes CSV
# data = pd.read_csv("halal_recipes.csv")

# st.set_page_config(page_title="Halal Recipe Explorer", layout="wide")
# st.title("🍽️ Halal Recipe Explorer")
# st.markdown("Explore popular, halal, and delicious recipes from Pakistani, Chinese, and Western cuisines.")


# # Sidebar Start
# st.sidebar.title("🍽 Halal Recipes")
# # Sidebar filter
# category = st.sidebar.selectbox("🌍 Choose Cuisine Type:", sorted(data['Category'].unique()))
# filtered_data = data[data['Category'] == category]

# # Search box
# search_query = st.sidebar.text_input("Search Recipe by Name:")
# if search_query:
#     filtered_data = filtered_data[filtered_data['Recipe Name'].str.contains(search_query, case=False)]

# if st.sidebar.button("👉 Generate AI Recipes"):
#     st.markdown("[Click here to switch to AI Generated Recipes Page](http://localhost:8502)", unsafe_allow_html=True)


# # Show filtered recipes
# for index, row in filtered_data.iterrows():
#     with st.container():
#         st.subheader(f"🥘 {row['Recipe Name']}")
#         col1, col2 = st.columns([1, 2])
#         with col1:
#             st.markdown(f"**Category:** {row['Category']}")
#             st.markdown(f"**Ingredients:**\n{row['Ingredients']}")
#         with col2:
#             with st.expander("🔪 View Cooking Steps"):
#                 st.write(row['Steps'])
#         st.markdown("---")

# # --- Dynamic Spacer ---
# # Creates max vertical space between content and footer
# st.sidebar.markdown("<div style='flex:1;'></div>", unsafe_allow_html=True)

# # --- Sticky Footer ---
# st.sidebar.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"] > div:first-child {
#         display: flex;
#         flex-direction: column;
#         height: 100vh;
#     }
#     .footer {
#         margin-top: auto;
#         text-align: center;
#         color: gray;
#         font-size: 13px;
#         padding: 20px 10px;
#     }
#     </style>
#     <div class="footer">
#         Made with ❤️ by <b>Syed Akber Shah</b> for Beloved Muslims
#     </div>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Halal Recipe Explorer", layout="wide")
st.title("🍽️ Halal Recipe Explorer")
st.markdown("Explore popular, halal, and delicious recipes from Pakistani, Chinese, Indian, and Western cuisines.")

# Disclaimer
st.warning("Disclaimer: While we strive to provide only halal recipes, we strongly recommend that you personally verify the halal status of all ingredients before preparing or consuming any dish. We do not take responsibility for the halal compliance of every ingredient. Your discretion is advised.")

# Load halal recipes
data = pd.read_csv("halal_recipes.csv")

# Sidebar
st.sidebar.title("🍽 Halal Recipes")
category = st.sidebar.selectbox("🌍 Choose Cuisine Type:", sorted(data['Category'].unique()))
filtered_data = data[data['Category'] == category]

search_query = st.sidebar.text_input("🔍 Search Recipe by Name:")
if search_query:
    filtered_data = filtered_data[filtered_data['Recipe Name'].str.contains(search_query, case=False)]

# Show filtered recipes
for index, row in filtered_data.iterrows():
    with st.container():
        st.subheader(f"🥘 {row['Recipe Name']}")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"**Category:** {row['Category']}")
            st.markdown(f"**Ingredients:**\n{row['Ingredients']}")
        with col2:
            with st.expander("🔪 View Cooking Steps"):
                st.write(row['Steps'])
        st.markdown("---")

# Footer
st.sidebar.markdown("<div style='flex:1;'></div>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .footer {
        margin-top: auto;
        text-align: center;
        color: gray;
        font-size: 13px;
        padding: 20px 10px;
    }
    </style>
    <div class="footer">
        Made with ❤️ by <b>Syed Akber Shah</b> for Beloved Muslims
    </div>
    """, unsafe_allow_html=True
)
