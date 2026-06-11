# app.py
import streamlit as st
import joblib
import numpy as np
from utils import preprocess_text

st.set_page_config(
    page_title="AI News Verifier", 
    page_icon="📰", 
    layout="centered"
)

st.title("📰 Fake News Classification Dashboard")
st.write(
    "Enter the title and text body of a news article below. Our regularized "
    "machine learning pipeline will process the text and estimate the statistical "
    "probability of it being authentic or fabricated."
)

# 2. CACHE PIPELINE ASSETS TO PREVENT RELOADING SLOWDOWNS
@st.cache_resource
def load_saved_pipeline():
    """
    Safely rehydrates the saved vectorizer vocabulary and our regularized 
    Logistic Regression model from disk storage.
    """
    try:
        vec = joblib.load('models/vectorizer.pkl')
        # Using Logistic Regression here yields smooth, nuanced probabilities (e.g., 73% vs a flat 100%)
        model = joblib.load('models/logistic_regression.pkl') 
        return vec, model
    except FileNotFoundError:
        return None, None

# Run asset initialization
vectorizer, classification_model = load_saved_pipeline()

# 3. INTERACTIVE DASHBOARD VALIDATION LOGIC
if vectorizer is None or classification_model is None:
    st.error(
        "⚠️ Pre-trained model artifacts not found inside the 'models/' folder! "
        "Please execute 'python train.py' in your terminal window console first to compile the system."
    )
else:
    # Render UI Text Inputs for the End User
    article_title = st.text_input(
        "News Article Headline", 
        placeholder="e.g., Breaking: Major Political Policy Announcement Transpires..."
    )
    article_body = st.text_area(
        "Article Content Body", 
        placeholder="Paste the complete text content of the news post here...", 
        height=200
    )

    # Trigger Evaluation on Button Press
    if st.button("Analyze Content Consistency", type="primary"):
        # Validate that user actually input text in both fields
        if not article_title.strip() or not article_body.strip():
            st.warning("Please fill out both the headline and body text blocks before running the validation algorithm.")
        else:
            with st.spinner("Processing text mechanics and computing probability vectors..."):
                
                # Step A: Recreate the identical text concatenation used during training
                fused_raw_string = f"{article_title} {article_body}"
                
                # Step B: Clean the text string using the central engine rules inside utils.py
                # Note: utils expects an iterable array/list format
                cleaned_input = preprocess_text([fused_raw_string])
                
                # Step C: Map the cleaned text string to our exact TF-IDF numerical vector space
                vectorized_input = vectorizer.transform(cleaned_input)
                
                # Step D: Extract structural curve probability predictions
                # predict_proba returns an array layout of: [[Probability of Fake (0), Probability of Real (1)]]
                probabilities = classification_model.predict_proba(vectorized_input)[0]
                
                fake_probability = probabilities[0] * 100
                real_probability = probabilities[1] * 100
                
                # Determine final category label output based on majority percentage
                prediction_result = 1 if real_probability > fake_probability else 0
                
                # 4. RENDER GRAPHICAL APP ANALYSIS INTERFACE
                st.markdown("---")
                st.subheader("📊 System Diagnostic Probability Metrics")
                
                if prediction_result == 1:
                    st.success("### Prediction Outcome: **VERIFIED GENUINE ARTICLE**")
                    st.metric(label="Model Context Confidence Score", value=f"{real_probability:.2f}% REAL")
                    st.progress(int(real_probability))
                    st.info(
                        "ℹ️ **Linguistic Analysis Note:** The syntax structure, word densities, and contextual "
                        "layout patterns align primarily with baseline authoritative journalistic publications."
                    )
                else:
                    st.error("### Prediction Outcome: **FLAGGED AS UNVERIFIED / FAKE**")
                    st.metric(label="Model Context Confidence Score", value=f"{fake_probability:.2f}% FAKE")
                    st.progress(int(fake_probability))
                    st.warning(
                        "⚠️ **Linguistic Analysis Note:** This entry exhibits high density distributions of "
                        "sensationalist terminology, temporal bias match markers, or rigid historical word associations."
                    )
                    
                # Render a collapsible details element for your project presentation review
                with st.expander("See complete algorithm probability breakdown weights"):
                    st.write(f"🕵️‍♂️ Fabricated/Fake News Metric Space Weight: `{fake_probability:.2f}%`")
                    st.write(f"📰 Authoritative/Real News Metric Space Weight: `{real_probability:.2f}%`")