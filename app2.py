import streamlit as st
from src.inference2 import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Input')
    emp_length_options = ['1', '2', '3','4']                 
    emp_length = st.sidebar.selectbox("YearsExperience", emp_length_options)
    def get_input_features():
        input_features = {'YearsExperience': YearsExperience}                             
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None
    
def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to Salary Prediction</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'

    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()