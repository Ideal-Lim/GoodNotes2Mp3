import streamlit as st
from utils.streamlitHelper import folder_picker, open_folder
from utils.goodnoteHelper import convert_goodnotes_to_mp3
import os


st.title('GoodNotes To MP3')

# if 'save_path' not in st.session_state:
#     # For Folder picker button
#     st.session_state.save_path = None

goodnote_file = st.file_uploader("Upload a .goodnotes file", type=["goodnotes"])


# clicked = st.button('Change save path')
# if clicked:
#     try: 
#         st.session_state.save_path = folder_picker()
#         if st.session_state.save_path is not None:
#             st.text_input('Selected folder to save:', st.session_state.save_path)
#     except:
#         st.error("Please upload a .goodnotes file first.")
if st.button("Run"):
    if goodnote_file:
        output_dir = convert_goodnotes_to_mp3(goodnote_file)
        # st.button("Check MP3 file")
        with open(output_dir+".zip", "rb") as file:
            btn = st.download_button(
                label="Download mp3 files",
                data=file,
                file_name=goodnote_file.name.replace(".goodnotes", ".zip"),
                mime="application/zip"
            )
            os.remove(output_dir+".zip")

    else:
        st.error("Please upload a .goodnotes file")

# if st.session_state.save_path is not None:  
#     if st.button("Open Output Folder"):
#         open_folder(st.session_state.save_path)

