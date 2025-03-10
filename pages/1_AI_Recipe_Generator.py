import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AI Halal Recipe Generator", layout="wide")
st.title("🍽️ AI-Powered Halal Recipe Generator")
st.markdown("Enter ingredients and get AI-suggested halal recipes instantly.")

# Disclaimer 
st.warning("Disclaimer: While we strive to provide only halal recipes, we strongly recommend that you personally verify the halal status of all ingredients before preparing or consuming any dish. We do not take responsibility for the halal compliance of every ingredient. Your discretion is advised.")

# Sidebar
st.sidebar.title("🍽 Halal Recipes")
cuisine_type = st.sidebar.selectbox("🌍 Choose Cuisine Type:", ["Pakistani", "Pakistani Chinese", "Indian", "Western"])
ingredients = st.text_area("📝 Enter Ingredients (comma-separated):", placeholder="chicken, rice, tomato, ginger, garlic")

# Halal items filtering list
HALAL_ITEMS = {
    "potato", "tomato", "onion", "garlic", "ginger", "bell pepper", "green chili", "cucumber",
    "bottle gourd", "apple gourd", "bitter gourd", "eggplant", "radish", "carrot", "green peas",
    "spinach", "fenugreek leaves", "mustard greens", "colocasia", "zucchini", "okra", "cauliflower",
    "cabbage", "corn", "mushrooms", "apple", "banana", "pomegranate", "watermelon", "melon",
    "grapes", "mango", "orange", "papaya", "pineapple", "coconut", "guava", "berries", "strawberry",
    "blueberry", "cherry", "lemon", "dates", "pear", "peach", "plum", "kiwi", "lychee", "black currant",
    "almond", "walnut", "pistachio", "cashew nut", "pine nut", "raisins", "dry coconut", "dried dates",
    "fig", "dried apricot", "wheat", "rice", "millet", "sorghum", "refined flour", "cracked wheat",
    "oats", "red lentils", "green gram", "split bengal gram", "pigeon pea", "black chickpeas",
    "white chickpeas", "kidney beans", "black-eyed peas", "soybeans", "beef", "mutton", "lamb",
    "camel", "chicken", "turkey", "duck", "quail", "rabbit", "fish", "prawns", "crabs", "lobsters",
    "milk", "yogurt", "buttermilk", "butter", "cream", "cheese", "ghee", "water", "fruit juices",
    "vegetable juices", "milkshakes", "green tea", "black tea", "herbal tea", "coffee",
    "sugarcane juice", "lemonade", "rose syrup", "sharbat", "olive oil", "sunflower oil", "mustard oil",
    "coconut oil", "corn oil", "soybean oil", "cumin", "coriander", "turmeric", "black pepper",
    "clove", "cinnamon", "cardamom", "bay leaf", "carom seeds", "dried fenugreek", "asafoetida"
}

# Halal filtering function
def is_recipe_halal(recipe_ingredients):
    for item in recipe_ingredients:
        item = item.lower().strip()
        if item not in HALAL_ITEMS:
            return False
    return True

def filter_halal_recipes(recipes):
    halal_recipes = []
    for recipe in recipes:
        if is_recipe_halal(recipe.get('ingredients', [])):
            halal_recipes.append(recipe)
    return halal_recipes

# Recipe generation section
if st.button("Generate Recipes"):
    with st.spinner("Cooking up some AI magic... 🍳"):
        api_url = "https://api.spoonacular.com/recipes/complexSearch"
        params = {
            "query": ingredients,
            "cuisine": cuisine_type,
            "number": 5,
            "apiKey": os.environ.get("SPOONACULAR_API_KEY")
        }

        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                recipes = data.get("results", [])
                if recipes:
                    st.markdown("## 🍛 AI-Generated Recipes")
                    for recipe in recipes:
                        title = recipe.get("title", "Recipe")
                        image = recipe.get("image", "")
                        recipe_id = recipe.get("id")
                        source_url = f"https://spoonacular.com/recipes/{title.replace(' ', '-').lower()}-{recipe_id}"

                        st.subheader(f"🥘 {title}")
                        if image:
                            st.image(image, caption=title, use_container_width=True)
                        st.markdown(f"[🔗 View Full Recipe Instructions]({source_url})")
                        st.markdown("---")
                else:
                    st.warning("No suitable halal recipes found. Try different ingredients.")
            else:
                st.error("⚠️ API error or limit reached.")
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")

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




# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()

# st.set_page_config(page_title="AI Halal Recipe Generator", layout="wide")
# st.title("🍽️ AI-Powered Halal Recipe Generator")
# st.markdown("Enter ingredients and get AI-suggested halal recipes instantly.")

# # Sidebar
# st.sidebar.title("🍽 Halal Recipes")
# cuisine_type = st.sidebar.selectbox("🌍 Choose Cuisine Type:", ["Pakistani", "Pakistani Chinese", "Indian", "Western"])

# ingredients = st.text_area("📝 Enter Ingredients (comma-separated):", placeholder="chicken, rice, tomato, ginger, garlic")

# HALAL_ITEMS = {
#     "potato", "tomato", "onion", "garlic", "ginger", "bell pepper", "green chili", "cucumber",
#     "bottle gourd", "apple gourd", "bitter gourd", "eggplant", "radish", "carrot", "green peas",
#     "spinach", "fenugreek leaves", "mustard greens", "colocasia", "zucchini", "okra", "cauliflower",
#     "cabbage", "corn", "mushrooms", "apple", "banana", "pomegranate", "watermelon", "melon",
#     "grapes", "mango", "orange", "papaya", "pineapple", "coconut", "guava", "berries", "strawberry",
#     "blueberry", "cherry", "lemon", "dates", "pear", "peach", "plum", "kiwi", "lychee", "black currant",
#     "almond", "walnut", "pistachio", "cashew nut", "pine nut", "raisins", "dry coconut", "dried dates",
#     "fig", "dried apricot", "wheat", "rice", "millet", "sorghum", "refined flour", "cracked wheat",
#     "oats", "red lentils", "green gram", "split bengal gram", "pigeon pea", "black chickpeas",
#     "white chickpeas", "kidney beans", "black-eyed peas", "soybeans", "beef", "mutton", "lamb",
#     "camel", "chicken", "turkey", "duck", "quail", "rabbit", "fish", "prawns", "crabs", "lobsters",
#     "milk", "yogurt", "buttermilk", "butter", "cream", "cheese", "ghee", "water", "fruit juices",
#     "vegetable juices", "milkshakes", "green tea", "black tea", "herbal tea", "coffee",
#     "sugarcane juice", "lemonade", "rose syrup", "sharbat", "olive oil", "sunflower oil", "mustard oil",
#     "coconut oil", "corn oil", "soybean oil", "cumin", "coriander", "turmeric", "black pepper",
#     "clove", "cinnamon", "cardamom", "bay leaf", "carom seeds", "dried fenugreek", "asafoetida"
# }


# if st.button("Generate Recipes"):
#     with st.spinner("Cooking up some AI magic... 🍳"):
#         api_url = "https://api.spoonacular.com/recipes/complexSearch"
#         params = {
#             params = {
#                 "query": ingredients,
#                 "cuisine": cuisine_type,
#                 "number": 5,
#                 "apiKey": os.environ.get("SPOONACULAR_API_KEY")  #getting api key from .env
#             }
#         }

#         try:
#             response = requests.get(api_url, params=params)
#             if response.status_code == 200:
#                 data = response.json()
#                 hits = data.get("hits", [])
#                 if hits:
#                     st.markdown("## 🍛 AI-Generated Recipes")
#                     for hit in hits:
#                         recipe = hit["recipe"]
#                         st.subheader(f"🥘 {recipe['label']}")
#                         st.markdown(f"**Ingredients:**")
#                         st.markdown("\n".join([f"- {item}" for item in recipe['ingredientLines']]))
#                         st.markdown(f"[🔗 View Full Recipe Instructions]({recipe['url']})")
#                         st.markdown("---")
#                 else:
#                     st.warning("No suitable halal recipes found. Try different ingredients.")
#             else:
#                 st.error("⚠️ API error or limit reached.")
#         except Exception as e:
#             st.error(f"⚠️ Something went wrong: {e}")

# #checking, agr ek b haram item hui to return false
# def is_recipe_halal(recipe_ingredients):
#     for item in recipe_ingredients:
#         item = item.lower().strip()
#         if item not in HALAL_ITEMS:
#             return False  # agar koi aik bhi haram item mil jaye
#     return True  # sab halal hain

# # Get recipes from API
# def filter_halal_recipes(recipes):
#     halal_recipes = []
#     for recipe in recipes:
#         if is_recipe_halal(recipe['ingredients']):
#             halal_recipes.append(recipe)
#     return halal_recipes


# # Footer
# st.sidebar.markdown("<div style='flex:1;'></div>", unsafe_allow_html=True)
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
#     """, unsafe_allow_html=True
# )
