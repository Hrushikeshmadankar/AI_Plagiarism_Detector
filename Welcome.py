import streamlit as st    

# Set page title and favicon
st.set_page_config(page_title="AI Plagiarism Detector", page_icon="🔍")


# Header
st.title("AI Plagiarism Detector")
st.subheader("Ensure the Integrity of Your Content with Advanced AI Detection")

# Main Content
st.write("""
Welcome to AI Plagiarism Detector, your go-to solution for accurate and efficient plagiarism detection. 
Whether you're a student, researcher, or content creator, our state-of-the-art AI technology is here to ensure 
the authenticity of your work.
""")

# Features
st.header("Key Features")
st.markdown("- **Advanced AI Detection:** Leverage cutting-edge AI models for precise plagiarism analysis.")
st.markdown("- **User-Friendly Interface:** Easily submit your text and receive instant results.")
st.markdown("- **Privacy Assurance:** Your data is treated with the utmost confidentiality.")


# Footer
st.markdown(
    """
    --- 
    *AI Plagiarism Detector | Your Trusted Partner in Content Integrity*
    """
)