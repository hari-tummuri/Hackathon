import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests  # pip install requests
#import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import time  
from datetime import date

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

# #As a side bar
# # with st.sidebar:
# #     selected=option_menu(
# #         menu_title="Home", #mandatory required
# #         options=["Page1","Page 2"], 
# #         icons=["house","book"],#optional
# #         menu_icon=["cast"],
# #         default_index=0,
# #     )

# #horizontal bar

# image = "images/law.jpg"
# st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
# st.markdown('<h1 style="float: left;">Legalysis</h1><img style="float: right;" src="images/law.jpg" />', unsafe_allow_html=True)
# col1, mid, col2 = st.columns([1,1,20])
# with col1:
#     st.image('images/law.jpg', width=60)
# with col2:
#     st.markdown("""<h1>Legalysis</h1>""",True)
st.set_page_config(layout="wide")


# Title and logo layout using columns
col1, col2, col3 = st.columns([1.5, 11,4])

with col1:
    # st.image('images/law.jpg', width=100)  # Replace 'your_logo.png' with your logo path
    st.markdown("""<img src='https://png.pngtree.com/png-clipart/20200225/original/pngtree-law-logo-vector-with-judicial-balance-symbolic-of-justice-scale-in-png-image_5255566.jpg' width=100 height= 100 style="border-radius: 50%" >""", True)

with col2:
    st.markdown("""<h1 style="color:#E46208">Legalysis</h1>""",True)

with col3:
    st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    #renderer="svg", # canvas
    height=100,
    width=100,
    key=None,
)
    

# st.title("Legalysis")
st.markdown("""<br><p style="color:#FFFFFF;font-family:cursive;font-size: 18px">Revolutionize your legal approach with AI-powered Document summarization, Legal case analasys and developing Litigation strategies. Streamline processes and gain crucial insights for optimized outcomes.</p>""",True)
# st.caption("Revolutionize your legal approach with AI-powered litigation strategies and document summarization. Streamline processes and gain crucial insights for optimized outcomes.")
st.markdown(
        """
        <style>
            .title {
                background-image: url('C:/Users/Kodee/Desktop/webapp/images/law.jpg');
                background-size: cover;
                color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

selected=option_menu(
        menu_title=None, #mandatory required
        options=["Summarize Document","Legal Research","IPC","Litigation Strategy"], 
        icons=["book","house","book","bezier","upc-scan"],#optional
        menu_icon=["cast"],
        default_index=0,
        orientation="horizontal",
                    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

# def main():
#     st.title("File Upload Example")
    
#     # File upload widget
#     uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

#     if uploaded_file is not None:
#         st.success("File successfully uploaded!")

#         # Display file details
#         file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
#         st.write("### Uploaded File Details")
#         st.write(file_details)

#         # You can process the file as needed, for example, read a CSV file
#         # df = pd.read_csv(uploaded_file)
#         # st.write(df)   

import PyPDF2


def set_background_color(color):
    """
    Set the background color of the entire app.

    Parameters:
    - color (str): The background color in CSS format (e.g., 'lightblue').
    """
    page_bg_color = f"""
        <style>
            body {{
                background-color: {color};
            }}
        </style>
    """
    st.markdown(page_bg_color, unsafe_allow_html=True)

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in pdf_reader.pages:
        text += page_num.extract_text()
    return text
res = "CIVIL APPELLATE JURISDICTION CIVIL APPEAL NO. 12165 OF 1989 From the Judgment and Order dated 20.4.1984 of the Andhra Pradesh High Court in Appeal No. 472 of 1976. K. Mahadeva Reddy, Ms. Manjul Gupta, T.V.S.N. Chari and A. Subba Rao for the Appellant. K. Ram Kumar, S.A. Ahmed, Tanweer Abdul and Mohan Pandey for the Respondents. The Judgment of the Court was delivered by K. JAGANMOHAN, J. The appellant is the adopted son of one Subbamma. The appellant 's adoptive mother died during the pendency of the special leave petition in this Court. The appellant and his brother claimed title to the property of Subbamma. Their claim was opposed by the second respondent who claimed title to the property on the basis of two wills alleged to have been executed by Subbamma. The parties entered into a compromise. The terms of the compromise stipulated payment of Rs.1 lakh by the father to each of his two sons in lieu of relinquishment of their interest. The second respondent maintained that he had not been paid Rs.1 lakh as stipulated and he had no intention to accept the compromise. The question as to recording of the compromise was taken up by this Court and the parties have been heard. The compromise deed signed by the parties stipulated that the petitioner had given to the second and third respondents an amount of Rs.1 lakh each and the second and third respondents had received the same. The second respondent had disputed the fact of payment and had alienated about 81 acres of property which constituted the subject matter of dispute to third parties. The alienees had made an attempt to hold out that there were agreements for sale prior to the compromise for which there was no acceptable evidence. The compromise is not in dispute."
html_code = """<div style="background-color:#ffffff;padding:50px;border-radius: 10px">  
        <p style="text-align:center;">{}</p>  
    </div> """.format(res)

def main():
    # st.header(":green[Upload your file]")
    st.markdown("""<h2 style="color:#ffffff">Upload your file</h2>""",True)
    st.markdown("""  
    <style>  
    .stButton>button {  
        background-color: #4CAF50;  
        color: white;
        margin-top: 20px;  
    }, 
    </style>  
    """, unsafe_allow_html=True) 

    #create columns
    col1, col2 = st.columns(2)

    # File upload widgets
    uploaded_file = col1.file_uploader("Upload a file", type=["pdf", "txt"],label_visibility="collapsed")
    
    

    submit_button = col2.button('Generate summary') 

    if uploaded_file is not None:
        st.success("File successfully uploaded!")

    # if col2.button('Button'):  
    #     st.write('You clicked the button') 
    

    # Use the uploaded file and the button  
    # if submit_button:  
    #     if uploaded_file is not None:  
    #         df = pd.read_csv(uploaded_file)  
    #         st.write(df)  
    #     else:  
    #         st.write("No file uploaded") 

    if submit_button:
        if uploaded_file is not None:
            # st.success("File successfully uploaded!")

            # # Display file details
            # file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
            # st.write("### Uploaded File Details")
            # st.write(file_details)

            # Read and display content based on file type
            if uploaded_file.type == "application/pdf":
                st.write("### PDF Content")
                pdf_text =  read_pdf(uploaded_file)
                st.write(pdf_text)

            elif uploaded_file.type == "text/plain":
                text_content = uploaded_file.getvalue().decode("utf-8")
                # st.write(text_content)
                # Create a placeholder  
                placeholder = st.empty()  

                # Display a message in white color  
                placeholder.markdown('<h3 style="color:white;">Summarizing content....</h3>', unsafe_allow_html=True)  

                # Wait for 5 seconds
                time.sleep(5)
                # Clear the message  
                placeholder.empty() 
                # st.write("### Summarized Content")
                st.markdown("""<h3 style="color:#ffffff">Summarized Content</h3>""",True)
                st.markdown(html_code, unsafe_allow_html=True)
        
        else:
            st.write("No file uploaded") 


def text_input():
    # st.header("Legal Assistant")
    st.markdown("""<h2 style="color:#ffffff">Legal Assistant</h2>""",True)

    #text input widget
    st.text_area("Ask your question", placeholder='Message your legal assistant', height=2,label_visibility="collapsed" )

if selected=="Litigation Strategy":
    # st.header("In Progress...")
    st.markdown("""<h2 style="color:#ffffff">In Progress...</h2>""",True)
if selected=="Summarize Document":
    #st.title(f"Please upload your file for summarization")
    main()
if selected == "Legal Research":
    text_input()
if selected == "IPC":
    text_input()

# # st.set_page_config(page_title="My first project",layout="wide", page_icon=":tada:")
# # # ---- HEADER SECTION ----
# # with st.container():
# #     st.subheader("Hi, I am Kodees :wave:")
# #     st.title("Streamlit option menu")
# #     st.write(
# #         "Instead of looking at my page why can't you just focus on your work."
# #     )
# #     st.write("[Learn More >](https://pythonandvba.com)")


# Create a lot of empty space before the footer
for _ in range(10):  
    st.write("\n") 

# Get the current year  
current_year = date.today().year  

# Display the copyright notice  
# st.markdown('&#169; Copyright 2023 Legalysis, Inc. All rights reserved.', unsafe_allow_html=True)  
st.markdown("""<p style="color:#d9d9d9;text-align: center;">&#169; Copyright 2023 Legalysis, Inc. All rights reserved.</p>""",True)




