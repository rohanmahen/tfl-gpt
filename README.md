# TFL GPT

This chatbot, built with Langchain and OpenAI's GPT models, provides real-time journey planning for Transport for London (TFL). It integrates OpenStreetMap's Nominatim API for location services and TfL's API for journey details.

## Features

- **Location Conversion**: Translates location names to coordinates using Nominatim API.
- **Journey Planning**: Determines the fastest journey routes in London via TfL's API.
- **AI Conversational Interface**: Engages users with natural language processing powered by OpenAI and Langchain.

## Files Description

- `journey.py`: Handles interactions with the TfL API for journey details.
- `location.py`: Converts location names to coordinates.
- `main.py`: Initializes and runs the conversational agent.
- `requirements.txt`: Lists dependencies.

## Setup

### Prerequisites

- Python 3.6+
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rohanmahen/tfl-gpt.git
   cd tfl-gpt
   ```

2. **Set Up a Virtual Environment (Optional)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Unix or MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**

   Create a `.env` file with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_key_here
   ```

## Usage

Run `main.py` to start the bot:

```bash
python3 src/main.py
```

Input journey queries in natural language. Type `exit` to stop.
