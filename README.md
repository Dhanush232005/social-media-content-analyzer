 Social Media Content Analyzer

A Streamlit-based application that extracts and analyzes social media content from PDFs and images using OCR and AI.

#Features

  *Extract text from PDF files
  * Extract text from images using OCR
  * Analyze content using Google Gemini
  * Analyze content using Groq
  * Compare Gemini and Groq responces
  *Target audience identification
  * Engagement potential analysis
  * Content improvement suggestions
  * Interactive Streamlit UI

#Technologies Used

- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Google G
- Groq
- LangChain
- Python-dotenv

#How It Works

1. User uploads a PDF or image.
2. Text is extracted from the uploaded file.
3. OCR is used for image-based content.
4. The extracted text is sent to the selected AI model.
5. User can choose:
  - Gemini
  - Groq
  - Compare Both
6. The application displays the AI analysis.

#Analysis Provided

 The application analyzes:

   1. Content Type
   2. Main Topic
   3. Sentiment
   4. Target Audience
   5. Strengths
   6. Weaknesses
   7. Engagement Potential
   8. Improvement Suggestions
   9. Improved Version

#Approach

  Social Media Content Analyzer is a Streamlit-based application that analyzes social media content extracted from PDFs and images. PDFs are processed using PyMuPDF, while images are processed using Tesseract OCR.
  The extracted text is analyzed using two AI models: Google Goq. Users can select either model or compare both models simultaneously. The analysis identifies the content type, main topic, sentiment, target audience, strengths, weaknesses, engagement potential, improvement suggestions, and an improved version of the content.
  The project follows a modular architecture, separating PDF extraction, OCR processing, and AI analysis into different utility modules. API keys are stored in environment variables and excluded from the GitHub repository using `.gitignore`.

   #Project Structure

   ```text
         social-media-content-analyzer/
         │
         ├── app.py
         ├── requirements.txt
         ├── README.md
         ├── .gitignore
         │
         ├── utils/
         │   ├── analyzer.py
         │   ├── ocr.py
         │   └── pdf_extractor.py
         │
         └── sample_data/
             ├── sample.pdf
                 └── sample.png
