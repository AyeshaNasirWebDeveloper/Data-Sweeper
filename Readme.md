# Data Sweeper App

**Data Sweeper App** is a Python-based web application built using **Streamlit**, **Pandas**, and **Plotly**. This app allows you to upload files, clean data, visualize it, and download the processed data in various formats.

## Features

- **File Upload**: Upload CSV, Excel, Word, and PDF files.
- **Data Cleaning**:
  - Remove duplicate rows.
  - Fill missing values (with zero, mean, median, or mode).
- **Data Visualization**:
  - Line Chart
  - Bar Chart
  - Scatter Plot
  - Histogram
- **Convert and Download**:
  - Convert data to CSV, Excel, or JSON format.
  - Download the converted file.

## Requirements

- Python 3.7 or higher
- Libraries:
  - `streamlit`
  - `pandas`
  - `openpyxl`
  - `PyPDF2`
  - `python-docx`
  - `plotly`

## Installation

1. **Install Python**:
   If you don't have Python installed, download it from [Python.org](https://www.python.org/).

2. **Clone the Project**:
   ```bash
   git clone https://github.com/AyeshaNasirWebDeveloper/Data-Sweeper.git

3. **Run the App**:
    streamlit run app.py
