import streamlit as st
import tempfile

from services.result_saver import save_results
from services.zip_handler import extract_repo
from agent.workflow import run_agent
from services.download_helper import create_zip

st.set_page_config(
    page_title="AI Coding Agent",
    layout="wide"
)

st.title("🤖 AI Coding Agent")

uploaded_file = st.file_uploader(
    "Upload Repository ZIP",
    type=["zip"]
)

task = st.text_area(
    "Enter Coding Task",
    placeholder="Add input validation and write tests"
)

if st.button("Run Agent"):

    if uploaded_file is None:
        st.error("Please upload a repository ZIP.")
        st.stop()

    if not task:
        st.error("Please enter a task.")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp:
        tmp.write(uploaded_file.read())
        zip_path = tmp.name

    repo_path = extract_repo(zip_path)

    with st.spinner("Agent is working..."):
        
        try:
            result = run_agent(
                task=task,
                repo_path=repo_path
            )
            
        except ValueError as e:
            st.error(str(e))
            st.stop()
            
        except Exception as e:
            
            st.error(f"Unexpected Error: {str(e)}")
            st.stop()

        save_results(result)

    st.success("Completed")

    st.subheader("Selected Files")

    st.json(result["selected_files"])

    st.subheader("Plan")

    st.write(result["plan"])

    st.subheader("Explanation")
    
    st.write(result["explanation"])

    st.subheader("Diffs")

    for file_name, diff in result["diffs"].items():

        st.markdown(f"### {file_name}")

        st.code(
            diff,
            language="diff"
        )

    st.subheader("Modified Files")
    
    for file_name, code in result["modified_files"].items():
        
        st.markdown(f"### {file_name}")
        
        st.code(
            code,
            language="python"
        )
        
    if result["modified_files"]:
            
        zip_data = create_zip(
            result["modified_files"]
        )
            
        st.download_button(
            label="📥 Download Modified Repository",
            data=zip_data,
            file_name="modified_repo.zip",
            mime="application/zip"
        )