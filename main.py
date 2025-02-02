import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyAhmx3IROFIXarN5K8JR6A9LgJUDrncPkg")
from PIL import Image

st.set_page_config(page_title="Gemini Project")
st.header("GenAI Fitness Project")
input = st.text_input("Input Prompt", key="input")
uploaded_file = st.file_uploader("Upload your Image", type=['jpg','jpeg','png','webp'])

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_part=[
            {
                'mime_type':uploaded_file.type,
                'data':bytes_data
            }
        ]
        return image_part

def get_response(input,image,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,image[0],prompt])
    return response.text

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    
submit=st.button("Submit")
input_prompt="""You are an expert in nutritionist where you need to see the food items from the image
                                and calculate the total calories, also provide the details of every food items with calorie intake
                                in below format.

                                1. Item - 1: No. of calories
                                2. Item - 2: No. of calories
                                -----------
                                -----------
                                -----------  
    
        
"""
    
    
    
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_response(input_prompt,image_data,input)
    st.write(response)