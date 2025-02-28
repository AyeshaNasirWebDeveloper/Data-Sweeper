import streamlit as st
import pandas as pd
import PyPDF2
from docx import Document
import io
import plotly.express as px

st.set_page_config(
    page_title="Data Sweeper",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read CSV
def read_csv(file):
    return pd.read_csv(file)

# Read Excel
def read_excel(file):
    return pd.read_excel(file, engine='openpyxl')

# Read Word
def read_word(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

# Read PDF
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

# File type and Read Accordingly
def read_file(file):
    if file.type == "text/csv":
        return read_csv(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return read_excel(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return read_word(file)
    elif file.type == "application/pdf":
        return read_pdf(file)
    else:
        st.error("Unsupported file type")
        return None

# Clean Data
def clean_data(df):
    st.subheader("Data Cleaning")
    
    if st.checkbox("Remove duplicates"):
        df = df.drop_duplicates()
    
    if st.checkbox("Fill missing values"):
            df = df.fillna(0)
    return df

# Visualize Data
def visualize_data(df):
    st.subheader("Data Visualization")
    
    chart_type = st.selectbox(
        "Choose chart type",
        ["Pie Chart", "Line Chart", "Bar Chart", "Scatter Plot", "Histogram"]
    )
    
    if chart_type == "Pie Chart":
        column = st.selectbox("Select column for pie chart", df.columns)
        fig = px.pie(df, names=column, title=f"Pie Chart of {column}")
        st.plotly_chart(fig)

    elif chart_type == "Line Chart":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart: {x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    
    elif chart_type == "Bar Chart":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart: {x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    
    elif chart_type == "Scatter Plot":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot: {x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    
    elif chart_type == "Histogram":
        column = st.selectbox("Select column for histogram", df.columns)
        fig = px.histogram(df, x=column, title=f"Histogram of {column}")
        st.plotly_chart(fig)

# Convert & Download
def convert_and_download(df):
    st.subheader("Convert and Download Data")
    file_format = st.selectbox("Choose file format", ["CSV", "Excel", "JSON"])
    
    if file_format == "CSV":
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "data.csv", "text/csv")
    elif file_format == "Excel":
        excel = io.BytesIO()
        df.to_excel(excel, index=False, engine='openpyxl')
        excel.seek(0)
        st.download_button("Download Excel", excel, "data.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    elif file_format == "JSON":
        json = df.to_json(orient='records')
        st.download_button("Download JSON", json, "data.json", "application/json")

# Streamlit
st.title(":blue[Data Sweeper 🧹]")
st.write(":blue[Clean, transform, and analyze your data with ease.]")

uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "docx", "pdf"])

if uploaded_file is not None:
    st.write(":green[File uploaded successfully!]")
    
    data = read_file(uploaded_file)
    
    if isinstance(data, pd.DataFrame):
        st.write("Data Preview:")
        st.dataframe(data.head())
        
        # Data Cleaning
        data = clean_data(data)
        st.write("Cleaned Data Preview:")
        st.dataframe(data.head())
        
        # Data Visualization
        visualize_data(data)
        
        # Convert and Download
        convert_and_download(data)
    elif isinstance(data, str):
        st.write("File Content:")
        st.text(data)
    else:
        st.error("Could not read the file.")