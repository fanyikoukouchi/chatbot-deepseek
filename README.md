# DeepSeek ChatRobot

[中文文档](README.zh-CN.md)

A modern chat application powered by DeepSeek's large language model, featuring a Vue.js frontend and Python backend.

## System Architecture

### Overview
The system follows a three-tier architecture:
1. Frontend (Vue.js)
2. Backend (Python FastAPI)
3. DeepSeek API Integration
4. Database (PostgreSQL)

### Database
The application uses PostgreSQL as its primary database, with the following features:
- Relational database for structured data storage
- SQLAlchemy ORM for database operations
- Connection pooling for better performance
- Automatic migrations support
- Backup and recovery capabilities

### Directory Structure
```
deepseek-chatbot/
├── frontend/                 # Vue.js frontend application
│   ├── src/
│   │   ├── components/      # Vue components
│   │   ├── views/          # Page components
│   │   ├── store/          # Vuex state management
│   │   ├── router/         # Vue Router configuration
│   │   └── api/            # API service layer
│   └── package.json
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Core business logic
│   │   ├── models/         # Data models
│   │   └── services/       # Service layer
│   ├── requirements.txt
│   └── main.py
└── docs/                   # Documentation
```

### Technology Stack

#### Frontend
- Vue.js 3.x
- Vuex for state management
- Vue Router for navigation
- Axios for HTTP requests
- WebSocket for real-time communication
- TailwindCSS for styling

#### Backend
- Python 3.9+
- FastAPI framework
- SQLAlchemy ORM
- WebSocket support
- JWT authentication
- DeepSeek API integration

### Key Features
1. Real-time chat interface
2. Context-aware conversations
3. Tool integration support
4. User authentication
5. Conversation history
6. Plugin system

### API Design
The backend exposes RESTful APIs and WebSocket endpoints:
- `/api/auth/*` - Authentication endpoints
- `/api/chat/*` - Chat-related endpoints
- `/ws/chat` - WebSocket endpoint for real-time chat
- `/api/tools/*` - Tool integration endpoints

### Security
- JWT-based authentication
- HTTPS encryption
- Input validation
- Rate limiting
- CORS protection

## Development Setup

### Prerequisites
- Node.js 16+
- Python 3.9+
- DeepSeek API credentials

### Installation
1. Clone the repository
2. Set up frontend:
   ```bash
   cd frontend
   npm install
   ```
3. Set up backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Configuration
1. Create `.env` files in both frontend and backend directories
2. Configure DeepSeek API credentials
3. Set up database connection

### Running the Application
1. Start backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
2. Start frontend:
   ```bash
   cd frontend
   npm run serve
   ```

## Performance Considerations
- API response time < 500ms
- WebSocket connection stability
- Frontend bundle optimization
- Database query optimization
- Caching strategy

## Testing
- Frontend: Jest + Vue Test Utils
- Backend: pytest
- Integration tests
- Performance testing

## Deployment
- Docker containerization
- CI/CD pipeline
- Monitoring and logging
- Backup strategy 