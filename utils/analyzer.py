import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from groq import Groq
import os




load_dotenv()


llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=st.secrets["GOOGLE_API_KEY"]
)

prompt = ChatPromptTemplate.from_template("""
You are a professional social media content analyst.

Analyze the following social media content:

{content}

Provide the analysis in this format:

1. Content Type
2. Main Topic
3. Sentiment
4. Target Audience
5. Strengths
6. Weaknesses
7. Engagement Potential
8. Improvement Suggestions
9. Improved Version

Give practical and concise suggestions.
""")


chain = prompt | llm


def analyze_content(text):

    text=text[:8000]

    response = chain.invoke({
        "content": text
    })

    return response.text


GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

groq_client = Groq(
    api_key=GROQ_API_KEY
)


groq_prompt = """
You are a professional social media content analyst.

Analyze the following social media content:

{content}

Provide the analysis in this format:

1. Content Type
2. Main Topic
3. Sentiment
4. Target Audience
5. Strengths
6. Weaknesses
7. Engagement Potential
8. Improvement Suggestions
9. Improved Version

Give practical and concise suggestions.
"""


def analyze_with_groq(text):

    response = groq_client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": "You are a professional social media content analyst."
            },
            {
                "role": "user",
                "content": groq_prompt.format(content=text)
            }
        ],

        temperature=0.0
    )

    return response.choices[0].message.content
