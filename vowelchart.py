import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Tab 1
data = {
    "Vowel": ["i", "ɪ", "ɛ", "æ", "ɑ", "ɔ", "ʊ", "u", "ʌ", "ɝ"],
    "Men_F1": [270, 400, 530, 660, 730, 570, 440, 300, 640, 490],
    "Men_F2": [2300, 2000, 1850, 1700, 1100, 850, 1000, 850, 1200, 1350],
    "Women_F1": [300, 430, 600, 860, 850, 590, 470, 370, 760, 500],
    "Women_F2": [2800, 2500, 2350, 2050, 1200, 850, 1150, 950, 1400, 1650],
    "Children_F1": [370, 530, 700, 1000, 1030, 680, 560, 430, 850, 560],
    "Children_F2": [3200, 2750, 2600, 2300, 1350, 950, 1400, 1150, 1600, 1650]
}
df = pd.DataFrame(data)

# Initialize session state for tracking which data to plot in Tab 1
if 'show_men' not in st.session_state:
    st.session_state['show_men'] = False
if 'show_women' not in st.session_state:
    st.session_state['show_women'] = False
if 'show_children' not in st.session_state:
    st.session_state['show_children'] = False

# Function to plot vowel chart for Tab 1 with overlays for selected groups
def plot_vowel_chart(df):
    plt.figure(figsize=(8, 6))

    # Plot for Men if selected
    if st.session_state['show_men']:
        plt.scatter(df["Men_F2"], df["Men_F1"], color='blue', s=100, label='Men')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Men_F2"][i] + 30, df["Men_F1"][i] + 30, vowel, color='blue', fontsize=10, ha='center')

    # Plot for Women if selected
    if st.session_state['show_women']:
        plt.scatter(df["Women_F2"], df["Women_F1"], color='green', s=100, label='Women')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Women_F2"][i] + 30, df["Women_F1"][i] + 30, vowel, color='green', fontsize=10, ha='center')

    # Plot for Children if selected
    if st.session_state['show_children']:
        plt.scatter(df["Children_F2"], df["Children_F1"], color='red', s=100, label='Children')
        for i, vowel in enumerate(df["Vowel"]):
            plt.text(df["Children_F2"][i] + 30, df["Children_F1"][i] + 30, vowel, color='red', fontsize=10, ha='center')

    # Set consistent axes limits for all plots
    plt.xlim(800, 3300)
    plt.ylim(200, 1100)

    # Reverse axes as per common vowel chart convention
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.xlabel("F2")
    plt.ylabel("F1")
    plt.title("Overlay Vowel Chart")
    plt.legend()
    st.pyplot(plt)

# Tabs for different sections of the app
tab1, tab2, tab3 = st.tabs(["Overlay Vowel Chart", "Upload CSV", "Plot Uploaded Data"])

# Tab 1: Overlay Vowel Chart
with tab1:
    st.title("Overlay Vowel Chart Comparison")
    st.write("Click the buttons below to add each group's vowel data to the plot.")

    # Buttons to add each group's vowel data to the plot
    if st.button("Add Men's Data"):
        st.session_state['show_men'] = True

    if st.button("Add Women's Data"):
        st.session_state['show_women'] = True

    if st.button("Add Children's Data"):
        st.session_state['show_children'] = True

    # Display the vowel chart with the selected overlays
    plot_vowel_chart(df)

# Tab 2: Upload CSV file
uploaded_data = None
with tab2:
    st.title("Upload CSV File")
    st.write("Please upload a CSV file with columns: 'F1', 'F2', and 'word'.")
    st.markdown("[sample csv](https://raw.githubusercontent.com/MK316/MK-316/refs/heads/main/data/evowelcsv.csv)")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        uploaded_data = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.write(uploaded_data)

# Tab 3: Plot Uploaded Data
with tab3:
    st.title("Plot Uploaded Data")
    if uploaded_data is not None:
        plt.figure(figsize=(8, 6))
        plt.scatter(uploaded_data["F2"], uploaded_data["F1"], color='blue', s=100)

        # Display word labels
        for i, word in enumerate(uploaded_data["word"]):
            plt.text(uploaded_data["F2"][i] + 30, uploaded_data["F1"][i] + 30, word, fontsize=10, ha='center')

        # Set consistent axes limits
        plt.xlim(800, 3300)
        plt.ylim(200, 1100)

        # Reverse axes for vowel chart convention
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()

        plt.xlabel("F2")
        plt.ylabel("F1")
        plt.title("Dot Plot of F1 vs F2 with Word Labels")
        st.pyplot(plt)
    else:
        st.write("Please upload a CSV file in Tab 2 to display the plot here.")
