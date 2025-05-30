# SAFESPELL

## Description

SAFESPELL is an AI-powered tool designed to detect and explain emotionally manipulative or abusive language in text. It helps users identify potentially harmful communication patterns such as gaslighting, coercion, and other forms of verbal abuse.

## Features

-   **Text Analysis**: Users can paste a conversation or text snippet into a user-friendly interface.
-   **Keyword Detection**: The backend employs advanced NLP techniques to identify potentially toxic or manipulative phrases.
-   **AI-Powered Explanation**: Flagged phrases are analyzed using LLaMA 3.2 model via Ollama for in-depth analysis.
-   **Severity Scoring**: Each identified red flag is assigned a severity score from 1 to 5.
-   **Detailed Feedback**: The AI provides comprehensive explanations for each red flag, helping users understand the nature of the manipulative language.
-   **Frontend Visualization**: The frontend highlights flagged text, displays a severity meter, and presents the AI's explanations in a clear and accessible manner.
-   **Privacy-Focused**: All processing is done locally using Ollama, ensuring your data stays private.
-   **Real-time Analysis**: Instant feedback and analysis as you type.
-   **Modern UI/UX**: Beautiful, responsive design with smooth animations and interactions.

## Tech Stack

-   **Frontend**: React, Tailwind CSS
-   **Backend**: FastAPI (Python)
-   **AI Model**: LLaMA 3.2 via Ollama (local, privacy-focused AI processing)
-   **Styling**: Custom CSS with smooth animations and modern design patterns

## How to Run

### Prerequisites

-   **Python 3.8+**
-   **Node.js and npm**
-   **Ollama** - Download from [https://ollama.ai/download](https://ollama.ai/download)

### Setup Instructions

#### 1. Install and Setup Ollama

```bash
# Install Ollama (visit https://ollama.ai/download for your OS)
# After installation, pull the required model:
ollama pull llama3.2

# Start Ollama service (if not already running):
ollama serve
```

#### 2. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI application
python -m app.main
```

The backend will be available at `http://localhost:8000`

#### 3. Frontend Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

The frontend will be available at `http://localhost:3000`

### Quick Start

1. Ensure Ollama is running with LLaMA 3.2 model
2. Start the backend server
3. Start the frontend development server
4. Open `http://localhost:3000` in your browser
5. Start analyzing text for harmful language patterns!

## How to Push to GitHub using GitHub Desktop

1.  **Open GitHub Desktop.**
2.  If you haven't already, **add your local repository** to GitHub Desktop:
    -   Click on "File" > "Add Local Repository..."
    -   Choose the path to your `SAFESPELL` project folder.
3.  **Commit Changes:**
    -   GitHub Desktop will automatically detect any changes you've made to the files.
    -   In the "Changes" tab (usually on the left), you'll see a list of modified, added, or deleted files.
    -   Select the files you want to include in the commit. It's good practice to commit related changes together.
    -   Enter a concise and descriptive **commit summary** in the text box at the bottom left (e.g., "Create initial project structure" or "Add README.md").
    -   You can also add a more detailed **description** if needed.
    -   Click the "Commit to `main`" (or your current branch name) button.
4.  **Push to GitHub:**
    -   After committing, you'll see a "Push origin" button at the top of the GitHub Desktop window (or in the "Repository" menu).
    -   Click this button to upload your local commits to the remote repository on GitHub.

## Sample Input Examples to Test

You can test SAFESPELL with various text inputs. Here are a few examples that might contain manipulative language:

1.  **Gaslighting Example:**
    ```
    Person A: I felt really uncomfortable when you said that yesterday.
    Person B: I never said that. You're always imagining things and being too sensitive.
    ```

2.  **Coercion/Guilt-Tripping Example:**
    ```
    Person A: I'm not sure I want to go out tonight.
    Person B: If you really cared about me, you would come. I guess I'll just go alone then and be miserable.
    ```

3.  **Minimizing/Invalidating Example:**
    ```
    Person A: That comment you made about my project in front of everyone was really embarrassing.
    Person B: Oh, come on, I was just joking! You can't take a little teasing? It's not a big deal.
    ```

4.  **Blame-Shifting Example:**
    ```
    Person A: We need to talk about how the bills are piling up.
    Person B: Well, if you didn't spend so much on your hobbies, maybe we wouldn't have this problem. It's really your fault.
    ```

## API Endpoints

-   `POST /analyze` - Analyze text for harmful content
-   `GET /health` - Health check endpoint

## Project Structure

```
safespell/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py      # Main application entry point
│   │   ├── models/      # Data models
│   │   └── utils/       # Utility functions
│   ├── requirements.txt # Python dependencies
│   └── .env.example     # Environment variables template
├── frontend/            # React frontend
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   ├── components/  # React components
│   │   └── index.css    # Styling
│   ├── public/          # Static files
│   └── package.json     # Node.js dependencies
└── README.md           # This file
```

## Troubleshooting

**Ollama Issues:**
-   Ensure Ollama is installed and running: `ollama serve`
-   Verify LLaMA 3.2 model is available: `ollama list`
-   Check Ollama is accessible at `http://localhost:11434`

**Backend Issues:**
-   Verify virtual environment is activated
-   Check all dependencies are installed
-   Ensure port 8000 is available

**Frontend Issues:**
-   Clear npm cache: `npm cache clean --force`
-   Delete node_modules and reinstall: `rm -rf node_modules && npm install`
-   Ensure port 3000 is available

---

**Note**: This application processes all data locally using Ollama, ensuring your privacy and data security.
