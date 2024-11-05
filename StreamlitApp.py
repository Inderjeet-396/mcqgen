import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Loading the jsom file 

with open('C:\\Users\\inder\\mcqgen\\Response.json','r') as file:
    
    RESPONSE_JSON = json.load(file)

# creating the title for app
st.title("MCQs Creator Application with langchain ")

# Create a form using st.form

with st.form("user_inputs"):
    #file upload
    uploaded_file = st.file_uploader("Upload a PDF or Txt file")

    # Input fileds 
    mcq_count = st.number_input("NO. of MCQs",min_value=3,max_value=50)
    # Subject
    subject = st.text_input("Insert Subject",max_chars=20)
    #Quiz Tone
    tone=st.text_input("Complexity level of questions",max_chars=20,placeholder='simple')
    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked  and all fields have input 
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                # Count tokens and cost of API call 
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                        "text" : text,
                        "number":mcq_count,
                        "subject":subject,
                        "tone":tone,
                        "response_json":json.dumps(RESPONSE_JSON)
                    }
                )
                #st,write(response)
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("error")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    # Extract the quiz data from response
                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index=df.index + 1
                            st.table(df)
                            # Display the review in a text box as well
                            if 'Review' in response:
                                # Display the review in a text area
                                st.text_area(label="Review", value=response['Review'])
                            else:
                                # Show a warning message if 'Review' key is not present
                                st.warning("Review data not found in the response.")
                            # st.text_area(label="Review",value=response["Review"])
                        else:
                            st.error("error in the table data")
                else:
                    st.write(response)




