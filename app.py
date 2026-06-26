import streamlit as st
import pandas as pd
import random


# Load the data
@st.cache_data
def load_data():
    # Replace with your actual CSV filename
    return pd.read_csv("recipes.csv")


df = load_data()

# App Header
st.title("🍽️ Meal Prep Picker")
st.write("Can't decide what to cook? Let fate take care of it.")

st.divider()

# --- Filters ---
st.subheader("Filters")

# Multi-select for Cookbooks
cookbooks = df["Cookbook"].unique().tolist()
selected_books = st.multiselect(
    "Select Cookbook(s):", options=cookbooks, default=cookbooks
)

# Multi-select for Proteins (Your lightweight ingredient filter)
proteins = df["Protein"].unique().tolist()
selected_proteins = st.multiselect(
    "Select Primary Protein(s):", options=proteins, default=proteins
)

st.divider()

# --- Logic ---
# Filter the dataframe based on selections
filtered_df = df[
    (df["Cookbook"].isin(selected_books)) & (df["Protein"].isin(selected_proteins))
]

# --- UI Button & Result ---
if st.button("🎲 Pick a Meal", use_container_width=True):
    if not filtered_df.empty:
        # Pick a random row
        choice = filtered_df.sample(1).iloc[0]

        st.success(f"### 🎉 {choice['Recipe']}")
        st.write(f"**📖 Cookbook:** {choice['Cookbook']} (Page {choice['Page']})")
        st.write(f"**🥩 Protein:** {choice['Protein']}")

    else:
        st.error("No recipes match your current filters. Try adjusting them!")
