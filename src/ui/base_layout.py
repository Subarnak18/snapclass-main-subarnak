import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>

                """,
                unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>

                """,
                unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit header */

        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top:1.5rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height:1.1 !important;
            margin-bottom:0rem !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
            color: black !important;
        }

        h3 {
            font-family: 'Outfit', sans-serif !important;
            color: black !important;
        }

        h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        /* ---------- Text Input Label ---------- */

        .stTextInput label {
            color: black !important;
        }

        .stTextInput p {
            color: black !important;
        }

        /* ---------- Select Box Label ---------- */

        .stSelectbox label {
            color: black !important;
        }

        .stSelectbox p {
            color: black !important;
        }

        /* Fallback for newer Streamlit versions */

        div[data-testid="stWidgetLabel"] p {
            color: black !important;
        }

        button{
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]{
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"]{
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
            transform: scale(1.05);
        }


        /* =====================================================
           SHARE CLASS LINK DIALOG
           ===================================================== */

        div[data-testid="stDialog"] > div {
            background-color: #F5F6FF !important;
        }

        div[data-testid="stDialog"] h1 {
            color: black !important;
        }

        div[data-testid="stDialog"] h2 {
            color: #5865F2 !important;
        }

        div[data-testid="stDialog"] h3 {
            color: black !important;
        }

        div[data-testid="stDialog"] p {
            color: black !important;
        }

        div[data-testid="stDialog"] pre {
            background-color: #E8EAFF !important;
        }

        div[data-testid="stDialog"] code {
            color: black !important;
        }

        div[data-testid="stDialog"] div[data-testid="stAlert"] {
            background-color: #E1E7FF !important;
        }

        div[data-testid="stDialog"] div[data-testid="stAlert"] p {
            color: #3652B3 !important;
        }

        </style>
    """, unsafe_allow_html=True)