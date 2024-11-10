import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyAB7IqPaUC3lNWFL5YfKpb2zlAVizz06ag")
model = genai.GenerativeModel("gemini-1.5-flash")

# Method 1: Inject CSS directly with markdown
st.markdown("""
<style>
@keyframes colorChange {
    0% { color: grey; }
    25% { color: #CCA4EC; }
    50% { color: #75DFAA; }
    75% { color: #F8AA7D; }
    100% { color: #FD8282; }
}

.stHeading {
    display: flex;
    animation: colorChange 3s infinite; 
}
.stHeading p {
    font-family: Georgia, serif;
}         
        
.stMarkdown p {
    text-align: center;
    font-size: 21px;
}    

[data-testid="stVerticalBlockBorderWrapper"]{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    width: 100%;
}      
            
.stPageLink {
    border-style: solid;
    border-radius: 5px;
    padding: 1em;
    max-width: 100%;
}
            
.stPageLink p {
    font-size: 17px;
    text-align: center;  
}
            
.stPageLink:hover {
    background-color: #89C7FA;
    color: black;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

</style>
""", unsafe_allow_html=True)


with st.container():
    st.title("👋 Welcome to [App Title]")

st.write("Navigating finances for the first time can feel overwhelming, especially as a first-generation or low-income student. Our goal is to provide clear, practical information on financial topics to help you make informed decisions. From understanding student aid to managing credit and planning for retirement, we're here to support you every step of the way.")
st.write("Just click on the widgets below to access information, quizzes, resources, and more about the topics you'd wish to get familiar with")
st.write("")
c1 = st.container()
with c1:
    c1.page_link("pages/federal_aid.py", label="Federal Student Aid", icon="🤝")
    c1.page_link("pages/credit.py", label="Building Credit", icon="💳")
    c1.page_link("pages/retirement.py", label="Investing for Retirement", icon="💰")

# response = model.generate_content("How many planets are in our solar system?")


with st.expander ("Need more resources?"):
    VIDEO_URL = "https://www.youtube.com/watch?v=swXHv0khiWY"
    st.video(VIDEO_URL)
    st.write ("This video will take you througth the basics of financial literacy")
    st.write ("We have added a repository with more resources")
    st.write ("Still didn't get it? This Lecture will help you nevigate through the FUNDAMENTALS of  ")
    VIDEO_URL1 = "https://www.youtube.com/watch?v=uTbVWfdgXUY"
    st.video(VIDEO_URL1)
    



