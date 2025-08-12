import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Human Trafficking Data Analysis", page_icon="📊", layout="wide")

# --- TOP NAVIGATION BAR ---
selected = option_menu(
    menu_title=None,
    options=["🏠 Home", "📈 EDA", "🗺 Geo Analysis", "🔍 Hypothesis Testing", "📊 Power BI Dashboard", "📋 Summary & Feedback"],
    icons=["house", "bar-chart", "map", "search", "pie-chart", "clipboard"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"color": "white", "font-size": "16px", "text-align": "center", "margin": "0px"},
        "nav-link-selected": {
            "background-color": "#ff4b4b",
            "margin": "0px",         # remove margin to prevent gap
            "padding": "8px 15px",  # same padding as nav-link
            "border-radius": "4px", # optional rounding
            "height": "100%",       # make height full of container
            "display": "flex",      # flex to center content vertically
            "align-items": "center",
            "justify-content": "center"
      }  },
)



# Load dataset
df = pd.read_csv("data/cleaned/cleaned_missing_data.csv")

# --- HOME ---
if selected == "🏠 Home":
    st.title("Human Trafficking Data Analysis from Missing Person Data")
    st.markdown("""
    This project analyzes missing person records across India from 2017 to 2022 to uncover demographic and geographic patterns potentially associated with human trafficking.

    ### **Goals & Objectives**
    - Identify states and districts with the highest missing cases.
    - Understand age & gender patterns in missing persons.
    - Use spatial analysis to detect potential trafficking hotspots.
    - Perform hypothesis testing for actionable insights.
    - Create a Power BI dashboard for interactive exploration.
    """)

    # Show dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Download dataset button
    csv_file = df.to_csv(index=False).encode()
    st.download_button("📥 Download Dataset", data=csv_file, file_name="cleaned_missing_data.csv", mime="text/csv")

    st.markdown("**Dataset Source:** [Click Here](https://indiadataportal.com/p/crime-statistics/r/ncrb-cii_missing_persons-dt-yr-prv)")


# --- EDA ---


elif selected == "📈 EDA":
    st.title("Exploratory Data Analysis (EDA)")
    st.markdown("""
    In this section, we visualize patterns in missing person cases.
    Charts include **Top 10 States**, **Yearly Trends**, and **Age Distribution by Gender**.
    """)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_top_states = os.path.normpath(os.path.join(BASE_DIR, "..", "visual", "top_states.png"))
    img_year_trends = os.path.normpath(os.path.join(BASE_DIR, "..", "visual", "year_trends.png"))
    img_age_gender_bar = os.path.normpath(os.path.join(BASE_DIR, "..", "visual", "age_gender_bar.png"))

  
    import streamlit as st

    if os.path.exists(img_top_states):
        st.image(img_top_states, width=700)
    else:
        st.error(f"Image not found: {img_top_states}")

    if os.path.exists(img_year_trends):
        st.image(img_year_trends,width=700)
    else:
        st.error(f"Image not found: {img_year_trends}")

    if os.path.exists(img_age_gender_bar):
        st.image(img_age_gender_bar, width=700)
    else:
        st.error(f"Image not found: {img_age_gender_bar}")


# --- GEO ANALYSIS ---


elif selected == "🗺 Geo Analysis":
    st.title("Geospatial Analysis")
    st.markdown("""
    A **heatmap** showing intensity of missing person cases across states.  
    Areas with high density may indicate potential trafficking hotspots.
    """)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    heatmap_path = os.path.normpath(os.path.join(BASE_DIR, "..", "visual", "missing_heatmap.html"))

    if os.path.exists(heatmap_path):
        with open(heatmap_path, "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=600,width=900)
    else:
        st.error(f"Heatmap  file not found: {heatmap_path}")

# --- HYPOTHESIS TESTING ---
elif selected == "🔍 Hypothesis Testing":
    st.title("Hypothesis Testing Results")

    st.subheader("1️⃣ Are females more likely to be minors?")
    st.write("Chi-square test result: **p < 0.05**, indicating a significant association between being female and being a minor.")

    st.subheader("2️⃣ Do urban districts have more missing cases than rural?")
    st.write("T-test result: **p < 0.05**, suggesting a significant difference — urban areas tend to report more missing cases.")

# --- POWER BI DASHBOARD ---
elif selected == "📊 Power BI Dashboard":
    st.title("Power BI Dashboard")
    st.image("streamlit/page1.png", use_container_width=True)
    st.image("streamlit/pag2.png", use_container_width=True)   # fixed typo here!
    st.image("streamlit/page3.png", use_container_width=True)
    st.image("streamlit/page4.png", use_container_width=True)

    # Dashboard download
    try:
        with open("streamlit/powerbi.pbix", "rb") as f:
            st.download_button("📥 Download Power BI File (.pbix)", f, file_name="powerbi.pbix")
    except FileNotFoundError:
        st.warning("Power BI file not found.")
        # After your download button code

    st.markdown(" ")  # optional separator line

    st.markdown("### 📊 Interactive Power BI Report")
    st.markdown(
        "[Click here to view ](https://app.powerbi.com/view?r=eyJrIjoiNGViZWQwM2ItMjkxMC00ZGVhLTk2NWUtNGM0NTc5OWRmYzVlIiwidCI6ImY1OTJlZjFjLWI1OGQtNDY0Zi1iZDFkLWY3MGU2NWU3MDRiYSJ9)",
        unsafe_allow_html=True,
    )

## ------ summary and fedback ----

elif selected == "📋 Summary & Feedback":
    st.title("Executive Summary & Feedback")

    st.subheader("Executive Summary — Missing Persons in India (2017–2022)")
    import streamlit as st

    st.markdown("""
    **1️⃣ Approximately 1 million missing person cases reported.**  
    **2️⃣ Females account for 65.05% of cases.**  
    **3️⃣ Minors represent 5.75% of total cases.**  
    **4️⃣ Highest female missing cases in the 18–30 age group.**  
    **5️⃣ Highest male missing cases in the 30–45 age group.**  
    **6️⃣ Peak year: 2019, with 380,484 cases.**  
    **7️⃣ Maharashtra is the most affected state.**  
    **8️⃣ Cuttack is the district with the highest cases.**
    """)



    st.markdown(" ")  # separator line

    st.subheader("Feedback & Suggestions")
    feedback = st.text_area("Please provide your valuable feedback or suggestions here:")
    if st.button("Submit Feedback"):
        if feedback.strip() == "":
            st.warning("Please enter some feedback before submitting.")
        else:
            # Save or process feedback here
            st.success("Thank you for your feedback! 🙌")




