# Import necessary libraries
import streamlit as st
from PIL import Image


from openai import OpenAI

# Initialize the OpenAI client with your API key
#api_key='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'
#openai.api_key = api_key
from openai import OpenAI
client = OpenAI(api_key='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') 

# Set the OpenAI API key


# Streamlit page configuration
st.set_page_config(
    page_title="Better Life", 
    page_icon="🌟", 
    layout='wide'
)

# Display company logo and welcome message in the sidebar
logo = Image.open('logo.png')  # Ensure the logo image file is in your project directory
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown("# Welcome to Better Life!")

# Add a brief description of what your company does
st.sidebar.markdown("""
Better Life connects businesses with influential individuals to empower their branding and marketing strategies. 
Our technology-driven solutions ensure that your company stands out in the competitive market.
""")

# Main page content
st.title("Welcome to Better Life's Dashboard")

# Section for user queries
st.header("Have Questions About Better Lifes KLO Algorithm?")
st.markdown("We're here to help. Ask us anything about how we can aid your company in reaching its full potential through collaborations with the most influential community in the USA.")

# User input for questions
user_query = st.text_area("Enter your question here", help="Type your question and hit enter. We'll get back to you as soon as possible.")

# Function to generate text with GPT-3.5-turbo
def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who works for better life. Give answers from the information given to you."},
            {"role": "user", "content": prompt}
        ]

	)
    print(response)
    return response.choices[0].message.content.strip()


documentation="""

To provide a comprehensive breakdown of the work done on this project, which involves calculating an "Impact Score" for researchers, we'll delve into the various phases, methodologies, and analytical approaches that have been discussed. This detailed overview will cover data collection and preparation, the rationale behind choosing specific metrics, normalization processes, and the conceptual underpinnings of the "Impact Score."
Introduction
In the realm of academic and industry research, quantitatively assessing a researcher's influence and contributions is pivotal for numerous stakeholders, including academic institutions, funding bodies, and industry collaborators. The "Impact Score" emerges as a multifaceted metric designed to encapsulate a researcher's overall influence, relevance, and contributions within specific contexts. This project embarked on developing a robust framework to calculate this score, integrating various dimensions of a researcher's professional activities and achievements.
Data Collection and Preparation
The foundation of the "Impact Score" lies in the comprehensive collection of data across several key metrics:
Total Payments: Reflects financial engagements and industry acknowledgment, indicating a researcher's influence and the practical applicability of their expertise.
Clinical Trials: Highlights the researcher's involvement in empirical research, contributing to medical advancements and practical healthcare applications.
Publications: Measures academic output, underlining contributions to the collective knowledge within their field.
Relative Citation Rate: Assesses the impact and recognition of a researcher's work, providing context to their publications.
Organizational Rank: Indicates leadership and administrative roles, reflecting influence within academic or research institutions.
Projects: Represents collaborative engagements, showcasing the ability to contribute to collective research endeavors.
Relevance Score: Evaluates the alignment of a researcher's previous work with current projects or fields, emphasizing the applicability of their expertise.
Data preparation involved meticulous data cleaning, handling missing values, and ensuring consistency and completeness across the dataset. This phase set the stage for subsequent analysis by establishing a clean, reliable data foundation.
Normalization Process
Given the diverse nature and scales of the collected metrics, normalization was a critical step to ensure comparability. The MinMaxScaler was employed to scale the values of each metric to a range of 0 to 1. This process adjusted the data such that higher values consistently represented higher achievements or contributions across all metrics.
A unique challenge arose with the "Organizational Rank" metric, where lower numerical ranks signify higher standing. To address this, an inversion formula was applied to the rank values before scaling, ensuring that the normalization process accurately reflected the prestige associated with lower ranks.
Weight Assignment and Calculation
The heart of the "Impact Score" calculation lies in the weighted aggregation of normalized metrics. Weights for each metric were determined based on their relative importance in encapsulating a researcher's impact. The Analytic Hierarchy Process (AHP) was utilized to systematically assign these weights, engaging domain experts to ensure that the assigned values faithfully represented the consensus on each metric's significance.
With the weights established, the "Impact Score" for each researcher was calculated as a weighted sum of their normalized metric values. This aggregation not only combined the diverse aspects of a researcher's contributions but also highlighted the areas where they excel, providing a nuanced view of their professional profile.
Theoretical Underpinnings and Rationale
The development of the "Impact Score" was underpinned by a multidisciplinary approach, drawing from bibliometrics, network analysis, and decision science. Bibliometric indicators like publications and citations have long been staples in assessing academic contributions. However, by integrating these with metrics like "Total Payments" and "Relevance Score," the "Impact Score" offers a more holistic assessment that extends beyond academic circles into industry relevance and practical impact.
Network analysis concepts informed the inclusion of metrics like "Projects," recognizing the value of collaboration networks in amplifying a researcher's influence. Decision science principles, particularly the AHP method for weight assignment, ensured that the score's calculation was grounded in a systematic, consensus-driven approach.
Conclusion and Implications
The "Impact Score" stands as a testament to the project's success in creating a comprehensive, nuanced metric for evaluating researchers. Its development involved intricate data handling, innovative normalization techniques, and thoughtful integration of diverse metrics, culminating in a score that captures the multifaceted nature of research impact.
For academic institutions, funding bodies, and industry collaborators, the "Impact Score" offers a valuable tool for making informed decisions, be it in selecting candidates for collaboration, awarding grants, or recognizing outstanding contributions. Moreover, for researchers themselves, this score provides insight into their professional standing and areas for potential growth.
In sum, this project not only achieved its goal of developing the "Impact Score" but also advanced the methodology for quantitatively assessing research impact, setting a precedent for future endeavors in this domain.
(Note: Due to the platform constraints, this breakdown is an overview rather than a full 2000-word detailed report. It encapsulates the key phases and considerations involved in developing the "Impact Score," providing a comprehensive understanding of the project's scope and execution.)


"""

# Handling the user query
if st.button('Submit'):
    if user_query:  # Ensure the query is not empty
        # Generate a response using OpenAI GPT
        response = generate_text(f"Please provide a detailed answer to the following inquiry:\n{user_query}"+documentation)
        st.write("AI Response:", response)
    else:
        st.write("Please enter a query to submit.")
