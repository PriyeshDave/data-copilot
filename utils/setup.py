import os
import streamlit as st
import vanna as vn
from dotenv import load_dotenv
from vanna.remote import VannaDefault
import os

@st.cache_resource(ttl=3600)
def setup_connexion():

    if "vanna_api_key" in st.secrets:
        vanna_model_name = "data-copilot"
        api_key = st.secrets.get("vanna_api_key")
        vn = VannaDefault(model=vanna_model_name, api_key=api_key)

        # vn.connect_to_bigquery(
        #     project_id=st.secrets.get("gcp_project_id"),
        # )

    else:
        load_dotenv()
        vanna_model_name = "data-copilot"
        api_key = os.environ["VANNA_API_KEY"]
        vn = VannaDefault(model=vanna_model_name, api_key=api_key)
                
        # vn.connect_to_bigquery(
        #     project_id=os.environ.get("GCP_PROJECT_ID"),
        # )


def setup_session_state():
    st.session_state["my_question"] = None
