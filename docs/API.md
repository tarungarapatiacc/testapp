# API Documentation

## Base URL
`http://localhost:8000`

## Endpoints

### Questions

#### Get Random Questions
```http
GET /api/questions/random?category=business&difficulty=intermediate&count=1
```

**Query Parameters:**
- `category` (optional): business, technical, creative
- `difficulty` (optional): beginner, intermediate, advanced
- `count` (optional, default: 1): Number of questions (1-10)

**Response:**
```json
[
  {
    "title": "Customer Retention Crisis",
    "description": "A loyal customer of 10 years suddenly switches to a competitor...",
    "category": "business",
    "difficulty": "intermediate",
    "context": "You're a customer success manager"
  }
]
```

#### Get Categories
```http
GET /api/questions/categories
```

**Response:**
```json
["business", "technical", "creative"]
```

#### Get Questions by Category
```http
GET /api/questions/by-category/{category}
```

**Response:**
```json
[
  {
    "title": "...",
    "description": "...",
    "category": "business",
    "difficulty": "...",
    "context": "..."
  }
]
```

### Assessment

#### Analyze Response
```http
POST /api/assessment/analyze
Content-Type: application/json

{
  "question_id": 1,
  "response_text": "Your response here..."
}
```

**Response:**
```json
{
  "human_score": 75.5,
  "ai_comparison_score": 82.3,
  "creativity_index": 68.9,
  "nuance_score": 71.2,
  "out_of_box_thinking_score": 76.4,
  "feedback": "Excellent out-of-box thinking! Your response shows...",
  "timestamp": "2024-01-15T10:30:00",
  "question_id": 1
}
```

## Error Handling

### Common Error Responses

**400 Bad Request**
```json
{
  "detail": "Response cannot be empty"
}
```

**404 Not Found**
```json
{
  "detail": "Resource not found"
}
```

**500 Internal Server Error**
```json
{
  "detail": "An error occurred while processing your request"
}
```
