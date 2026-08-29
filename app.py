import streamlit as st

from src.screen.home_screen import home_screen
from src.screen.teacher_screen import teacher_screen
from src.screen.student_screen import student_screen


def main():
    st.set_page_config(
        page_title='SnapClass - Making attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
        )

    

    if "login_type" not in st.session_state:
        st.session_state.login_type = None

    # Handle join code first
    join_code = st.query_params.get("join_code")

    if join_code:
        st.session_state.pending_join_code = join_code

        if st.session_state.login_type != "student":
            st.session_state.login_type = "student"
            st.rerun()

    # Route to the correct screen
    match st.session_state.login_type:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case _:
            home_screen()


main()