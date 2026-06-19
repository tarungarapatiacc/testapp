# Architecture Overview

## System Design

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **State Management**: React hooks (Context API for complex state)
- **Styling**: TailwindCSS for responsive design
- **HTTP Client**: Axios for API communication
- **Routing**: React Router v6

### Backend Architecture
- **Framework**: FastAPI (Python async framework)
- **Database**: SQLAlchemy ORM with SQLite/PostgreSQL
- **API**: RESTful endpoints with automatic OpenAPI documentation
- **NLP**: spaCy, NLTK for text analysis
- **Authentication**: JWT-based (future)

## Data Flow

1. **Question Generation**
   ```
   Frontend Request → Backend QuestionGenerator → Question Bank → Response
   ```

2. **Response Analysis**
   ```
   User Response → ResponseAnalyzer → NLP Processing → Scoring → Feedback
   ```

3. **Result Display**
   ```
   Analysis Results → Frontend Results Component → Visualization
   ```

## Key Components

### Backend Services

#### QuestionGenerator Service
- Manages question bank
- Generates random questions with filters
- Supports multiple difficulty levels and categories

#### ResponseAnalyzer Service
- Analyzes text for human-like traits
- Calculates creative thinking scores
- Measures out-of-box thinking indicators
- Detects nuance and sophistication
- Compares with AI thinking patterns

### Frontend Pages

1. **Home**: Landing page with feature overview
2. **Assessment**: Question display and response capture
3. **Results**: Score visualization and insights

## Scoring Algorithms

### Human Score (0-100)
- Personal references and emotional language
- Response length and thoughtfulness
- Presence of nuanced language
- Curiosity indicators (questions)

### AI Comparison Score (0-100)
- Emotional expression
- Uncertainty and hedging language
- Response complexity and detail

### Creativity Index (0-100)
- Vocabulary diversity
- Novel approach indicators
- Response length and depth

### Nuance Score (0-100)
- Balance and contradiction indicators
- Conditional thinking patterns
- Context and qualification language

### Out-of-Box Thinking Score (0-100)
- Lateral thinking indicators
- Problem reframing ability
- Creative solution synthesis

## Future Enhancements

- Machine learning model for improved analysis
- User authentication and progress tracking
- Advanced analytics dashboard
- Social comparison features
- Customizable question sets
- Multi-language support
- Real-time collaborative assessments
