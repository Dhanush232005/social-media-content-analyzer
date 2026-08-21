import streamlit as st

from utils.pdf_extractor import extract_pdf_text
from utils.ocr import extract_text_from_image
from utils.analyzer import analyze_content, analyze_with_groq


st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e1b4b 50%,
        #312e81 100%
    );
    color: white;
}

h1 {
    color: #ffffff;
    font-weight: 700;
}

h2, h3 {
    color: #e0e7ff;
}

p {
    color: #dbeafe;
}

[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.20);
    border-radius: 15px;
    padding: 10px;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6
    );

    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: 600;
}
.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #8b5cf6,
        #6366f1
    );

    color: white;
}

textarea {
    background-color: rgba(255, 255, 255, 0.08) !important;
    color: white !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)


st.title("📱 Social Media Content Analyzer")

st.write(
    "Upload a PDF or image containing social media content "
    "to extract and analyze the text."
)

uploaded_file = st.file_uploader(
    "Upload your file",
    type=["pdf", "png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    file_type = uploaded_file.type

    if file_type == "application/pdf":

        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_pdf_text(uploaded_file)

    elif file_type.startswith("image/"):

        with st.spinner("Extracting text from image using OCR..."):
            extracted_text = extract_text_from_image(uploaded_file)

    else:

        st.error("Unsupported file type.")
        extracted_text = ""

    if extracted_text and extracted_text.strip():

        st.success("Text extracted successfully!")

        st.subheader("📄 Extracted Content")

        st.text_area(
            "Extracted text",
            extracted_text,
            height=300
        )


        st.subheader("🤖 Choose AI Preference")

        ai_choice = st.radio(
            "Select how you want to analyze the content:",
            [
                "AI Model 1",
                "AI Model 2",
                "Compare Both"
            ],
            horizontal=True
        )


        if st.button("🔍 Analyze Content"):

            if ai_choice == "AI Model 1":

                with st.spinner("Analyzing with AI Model 1..."):

                    analysis = analyze_content(
                        extracted_text
                    )

                st.subheader("🤖 AI Model 1 Analysis")

                st.write(analysis)

            elif ai_choice == "AI Model 2":

                with st.spinner("Analyzing with AI Model 2..."):

                    analysis = analyze_with_groq(
                        extracted_text
                    )

                st.subheader("🧠 AI Model 2 Analysis")

                st.write(analysis)

            else:

                with st.spinner(
                    "Analyzing with both AI models..."
                ):

                    analysis1 = analyze_content(
                        extracted_text
                    )

                    analysis2 = analyze_with_groq(
                        extracted_text
                    )


                st.subheader("📊 AI Comparison")


                col1, col2 = st.columns(2)


                with col1:

                    st.markdown(
                        "### 🤖 AI Model 1"
                    )

                    st.write(analysis1)


                with col2:

                    st.markdown(
                        "### 🧠 AI Model 2"
                    )

                    st.write(analysis2)


    else:

        st.warning(
            "No readable text could be extracted from this file."
        )
