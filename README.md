# Intelligent Image Classification and Analysis

Welcome to the Intelligent Image Classification and Analysis tool! This project is a Streamlit web application that uses the Google Gemini 2.5 Flash model to help you understand and extract insights from your images. Whether you want a quick description, need to pull structured data from a receipt, or want a technical breakdown of a stock chart, this tool has you covered.

## What It Does

- **Image Description**: Upload any picture, and the app will give you a detailed breakdown of what's in it—from the people and objects to the overall mood and setting.
- **Structured Data Extraction**: Tired of manually typing out receipts or business cards? This feature automatically grabs the important details and neatly formats them into JSON for you.
- **Stock Chart Analysis**: If you're looking at a financial chart and want a second opinion, this feature acts like your personal technical analyst. It spots trends, recognizes chart patterns, identifies key support and resistance levels, and reads technical indicators for you.

## How I Built It

- **Python 3**: The core language powering the logic.
- **Streamlit**: Used to create a clean, interactive web interface so you don't have to use the command line.
- **Google GenAI SDK**: The bridge that connects my app to the Gemini 2.5 Flash model.

## Getting Started

To get this running on your own machine, you'll need Python 3.8 or higher and a Google Gemini API key.

1. **Clone the project:**
   ```bash
   git clone https://github.com/Abhinand-PV/image-analyser.git
   cd image-analyser
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # If you're on Windows, use: .venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API Key:**
   Create a `.streamlit/secrets.toml` file in the main folder and add your Gemini API key like this:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```

## Running the App

Just run this command in your terminal:
```bash
streamlit run app.py
```

Your browser should automatically open to `http://localhost:8501`. From there, use the sidebar to pick what you want to do, upload your image, and let the app handle the rest!

## See It in Action

*(Note: The images below use standard Markdown formatting to render as actual pictures on GitHub!)*

### 1. The Main Interface
![Application Interface](assets/interface-screenshot.png)

### 2. Image Description in Action
See how the model breaks down the visual elements of a document into a comprehensive textual description:

![Image Description 1](assets/image-description-1.png)
![Image Description 2](assets/image-description-2.png)
![Image Description 3](assets/image-description-3.png)
![Image Description 4](assets/image-description-4.png)

### 3. Extracting Data from Documents
Watch as the tool pulls structured JSON data directly from a scanned fee receipt:

![Structured Data Extraction 1](assets/data-extraction-1.png)
![Structured Data Extraction 2](assets/data-extraction-2.png)
![Structured Data Extraction 3](assets/data-extraction-3.png)

### 4. Deep Dive: Stock Chart Analysis

Here is a step-by-step look at how the app breaks down a financial chart. It identifies the overall bearish trend, points out the key resistance levels, and provides a final outlook based on the indicators it sees.

*Uploading the Chart & Trend Analysis*
![Stock Chart Trend Analysis](assets/stock-chart-1.png)

*Identifying Key Resistance & Support Levels*
![Stock Chart Key Levels](assets/stock-chart-2.png)

*Interpreting Indicators and Final Summary*
![Stock Chart Indicators and Summary](assets/stock-chart-3.png)
