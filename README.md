# AI Chatbot

A simple ChatGPT-style chatbot built with a FastAPI backend and a clean HTML, CSS, and JavaScript frontend. The backend uses LangChain with Groq to generate AI responses, while the frontend provides a lightweight chat interface for sending messages and showing replies.

## Features

- Chat interface similar to a basic AI assistant
- FastAPI backend with clean API routes
- Groq LLM integration through LangChain
- CORS support for local frontend development
- Request and response validation with Pydantic
- Simple frontend built with plain HTML, CSS, and JavaScript
- API documentation available through FastAPI Swagger UI

## Project Structure

```text
chatbot/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py          # Environment settings and allowed origins
│   │   ├── llm_service.py     # Groq and LangChain response generation
│   │   ├── main.py            # FastAPI app setup
│   │   ├── routes.py          # API endpoints
│   │   └── schemas.py         # Request and response models
│   │
│   ├── .env                   # Local environment variables
│   └── requirements.txt       # Backend dependencies
│
└── frontend/
    ├── index.html             # Chat UI markup
    ├── style.css              # Frontend styling
    └── script.js              # Frontend API calls and chat behavior
```

## Requirements

Make sure you have the following installed:

- Python 3.10 or later
- pip
- A Groq API key
- A browser

## Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

For Windows:

```bash
venv\Scripts\activate
```

For macOS or Linux:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
GROQ_API_KEY="your_groq_api_key_here"
GROQ_MODEL=llama-3.1-8b-instant
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000
```

Do not upload your real `.env` file to GitHub. Keep API keys private.

Start the backend server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

Open a new terminal and go to the frontend folder:

```bash
cd frontend
```

Run a simple local server:

```bash
python -m http.server 5500
```

Open this URL in your browser:

```text
http://localhost:5500
```

Now type a message in the chat input and send it. The frontend will call the backend API and show the AI response in the chat box.

## API Endpoints

### Health Check

```http
GET /api/health
```

Response:

```json
{
  "status": "ok",
  "message": "Chatbot API is running"
}
```

### Chat

```http
POST /api/chat
```

Request body:

```json
{
  "message": "Hello, how are you?"
}
```

Response:

```json
{
  "response": "AI response will appear here"
}
```

## How It Works

The frontend collects the user's message from the input field and sends it to the backend using a POST request.

The backend receives the message, validates it with Pydantic, and passes it to the LLM service. The LLM service sends the message to Groq through LangChain and returns the generated response. The frontend then displays that response inside the chat window.

## Environment Variables

| Variable | Description |
| --- | --- |
| `GROQ_API_KEY` | Your Groq API key |
| `GROQ_MODEL` | Groq model used for chat responses |
| `ALLOWED_ORIGINS` | Comma-separated list of frontend URLs allowed by CORS |

## Changing the API URL

The frontend API URL is defined in `frontend/script.js`:

```javascript
const API_URL = "http://127.0.0.1:8000/api/chat";
```

If your backend runs on another port or domain, update this value before running the frontend.

## Recommended `.gitignore`

Add a `.gitignore` file to avoid pushing local files and secrets:

```gitignore
# Python
__pycache__/
*.pyc
venv/
.env

# Editor
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

You can also create a `.env.example` file for GitHub:

```env
GROQ_API_KEY="your_groq_api_key_here"
GROQ_MODEL=llama-3.1-8b-instant
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000
```

## Common Issues

### Backend is not starting

Check that you are inside the `backend` folder and the virtual environment is activated. Also make sure all dependencies are installed.

```bash
pip install -r requirements.txt
```

### Groq API error

Make sure your `GROQ_API_KEY` is correct and available in the `.env` file.

### Frontend shows "Sorry, something went wrong"

This usually means the frontend could not reach the backend. Confirm that the backend is running at:

```text
http://127.0.0.1:8000
```

Also check that `API_URL` in `frontend/script.js` matches your backend URL.

### CORS error in browser console

Make sure the frontend URL is included in `ALLOWED_ORIGINS` inside the backend `.env` file.

For example:

```env
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000
```

## Notes

- Keep your API key private.
- Run the backend and frontend in separate terminals.
- Use `/docs` to test the API directly from the browser.
- The current frontend is intentionally simple and can be extended with chat history, markdown rendering, authentication, or database storage later.
