# Intelligent Image Classification and Analysis

A powerful web application that leverages the Google Gemini 2.5 Flash model to provide advanced image analysis capabilities. Built with Streamlit, this tool allows users to upload images and extract meaningful insights across various domains, ranging from general descriptions to structured data extraction and technical stock chart analysis.

## Features

- **Image Description**: Generates comprehensive, well-organized descriptions of uploaded images, detailing objects, people, colors, setting, mood, and visible text.
- **Structured Data Extraction**: Automatically identifies and extracts relevant structured data (e.g., from receipts or business cards) and outputs it in a clean JSON format.
- **Stock Chart Analysis**: Acts as a technical analyst to evaluate stock chart images, identifying overall trends, patterns, key support/resistance levels, and technical indicators.

## Technologies Used

- **Python 3**
- **Streamlit**: For the interactive web interface.
- **Google GenAI SDK**: For seamless integration with the Gemini 2.5 Flash model.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- A valid Google Gemini API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abhinand-PV/image-analyser.git
   cd image-analyser
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   Create a `.streamlit/secrets.toml` file in the project root and add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```
   Alternatively, you can configure your environment variables depending on your deployment setup.

## Usage

Run the Streamlit application using the following command:
```bash
streamlit run app.py
```

Once the server is running, navigate to the local URL provided in your terminal (typically `http://localhost:8501`). Use the sidebar to select your desired analysis mode, upload an image, and view the generated insights.

## Deep Dive: Stock Chart Analysis Feature

The Stock Chart Analysis feature transforms the application into an automated technical analyst. By simply uploading an image of any financial chart, the application utilizes the Gemini 2.5 Flash model to instantly evaluate and provide:
- **Trend Analysis**: Determines if the current trend is bullish, bearish, or sideways, backed by visible evidence.
- **Chart Patterns**: Recognizes classical formations such as double tops, head and shoulders, or flags.
- **Key Levels**: Identifies critical support and resistance zones.
- **Technical Indicators**: Interprets visible signals like volume spikes or moving averages.
- **Comprehensive Summary**: Synthesizes the findings into a clear overall outlook.

## Screenshots

**1. Application Interface**
![Application Interface](assets/interface-screenshot.png)

**2. Structured Data Extraction Example**
![Structured Data Extraction](assets/data-extraction-screenshot.png)

**3. Stock Chart Analysis in Action**

Below is a complete breakdown of the technical analysis produced by the application:

*Uploading the Chart & Trend Analysis*
![Stock Chart Trend Analysis](assets/stock-chart-1.png)

*Identifying Key Resistance & Support Levels*
![Stock Chart Key Levels](assets/stock-chart-2.png)

*Interpreting Indicators*
![Stock Chart Indicators](assets/stock-chart-3.png)

*Final Summary and Outlook*
![Stock Chart Summary](assets/stock-chart-4.png)
