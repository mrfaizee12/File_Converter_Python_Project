import streamlit as st
import pandas as pd
from fpdf import FPDF
from docx import Document

# 🎨 Custom CSS for Styling
st.markdown("""
    <style>
        body { background-color: #f5f5f5; }
        .main-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 700px;
            margin: auto;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton>button:hover { background-color: #45a049; }
        .title { font-size: 32px; font-weight: bold; color: #333; text-align: center; }
        .subtext { font-size: 18px; color: #666; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 🎯 Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📄 Convert File", "📬 Contact"])

# 🏠 Home Page
if page == "🏠 Home":
    st.markdown("<h1 class='title'>Welcome to File Converter 🌍</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>Convert DOCX or CSV files into PDF easily!</p>", unsafe_allow_html=True)
    
    st.image("https://apitemplate.io/wp-content/uploads/2022/10/python-generate-pdf.jpg", use_container_width=True)

    st.write("### 🔥 Features:")
    st.write("- 🚀 Convert DOCX to PDF")
    st.write("- 📌 Convert CSV to PDF")
    st.write("- 📬 Contact Form")

    st.success("🎉 Upload your file and get it converted in seconds!")

# 📄 Convert File Page
elif page == "📄 Convert File":
    st.markdown("<h1 class='title'>📄 File Converter</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your DOCX or CSV file", type=["docx", "csv"])

    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]

        # Convert DOCX to PDF
        if file_extension == "docx":
            doc = Document(uploaded_file)
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for para in doc.paragraphs:
                pdf.cell(200, 10, txt=para.text, ln=True)

            pdf_output_path = "converted.pdf"
            pdf.output(pdf_output_path)
            st.success("✅ DOCX converted to PDF successfully!")

            with open(pdf_output_path, "rb") as pdf_file:
                st.download_button(label="📥 Download PDF", data=pdf_file, file_name="converted.pdf", mime="application/pdf")

        # Convert CSV to PDF
        elif file_extension == "csv":
            df = pd.read_csv(uploaded_file)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for col in df.columns:
                pdf.cell(40, 10, col, border=1)

            pdf.ln()

            for index, row in df.iterrows():
                for col in df.columns:
                    pdf.cell(40, 10, str(row[col]), border=1)
                pdf.ln()

            pdf_output_path = "converted.pdf"
            pdf.output(pdf_output_path)
            st.success("✅ CSV converted to PDF successfully!")

            with open(pdf_output_path, "rb") as pdf_file:
                st.download_button(label="📥 Download PDF", data=pdf_file, file_name="converted.pdf", mime="application/pdf")

# 📬 Contact Page
elif page == "📬 Contact":
    st.markdown("<h1 class='title'>📬 Contact Me</h1>", unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and message:
                st.success("✅ Message sent successfully!")
            else:
                st.error("⚠️ Please fill all fields.")
