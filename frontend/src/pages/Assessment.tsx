import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

interface Question {
  title: string;
  description: string;
  category: string;
  difficulty: string;
  context?: string;
}

function Assessment() {
  const [question, setQuestion] = useState<Question | null>(null);
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchQuestion();
  }, []);

  const fetchQuestion = async () => {
    try {
      setLoading(true);
      const res = await axios.get(`${API_URL}/api/questions/random`, {
        params: { count: 1 }
      });
      if (res.data && res.data.length > 0) {
        setQuestion(res.data[0]);
      }
    } catch (err) {
      setError('Failed to load question. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!response.trim()) {
      setError('Please provide a response.');
      return;
    }

    try {
      // Store response and results
      const analysisRes = await axios.post(`${API_URL}/api/assessment/analyze`, {
        question_id: 1,
        response_text: response
      });

      // Navigate to results with data
      navigate('/results', {
        state: {
          question,
          response,
          analysis: analysisRes.data
        }
      });
    } catch (err) {
      setError('Failed to analyze response. Please try again.');
      console.error(err);
    }
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-12 text-center">
        <p className="text-xl text-gray-600">Loading question...</p>
      </div>
    );
  }

  if (!question) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-12 text-center">
        <p className="text-xl text-red-600">Failed to load question.</p>
        <button
          onClick={fetchQuestion}
          className="mt-4 bg-indigo-600 text-white px-6 py-2 rounded hover:bg-indigo-700"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-12">
      <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
        <div className="mb-6">
          <span className="inline-block bg-indigo-100 text-indigo-800 px-4 py-2 rounded-full text-sm font-semibold mb-4">
            {question.category.toUpperCase()} • {question.difficulty.toUpperCase()}
          </span>
          <h2 className="text-3xl font-bold text-gray-900 mb-4">{question.title}</h2>
          <p className="text-gray-700 text-lg mb-4">{question.description}</p>
          {question.context && (
            <p className="text-sm text-gray-500 italic">Context: {question.context}</p>
          )}
        </div>
      </div>

      <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8">
        <div className="mb-6">
          <label className="block text-lg font-semibold text-gray-900 mb-3">
            Your Response
          </label>
          <textarea
            value={response}
            onChange={(e) => setResponse(e.target.value)}
            placeholder="Share your thoughtful response here. Consider:
- Your perspective and experience
- Nuances and complexities
- Creative or unconventional approaches
- Real-world business implications"
            className="w-full h-64 p-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-indigo-600 resize-none"
          />
        </div>

        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
            {error}
          </div>
        )}

        <div className="flex gap-4">
          <button
            type="submit"
            className="flex-1 bg-indigo-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-indigo-700 transition"
          >
            Analyze Response →
          </button>
          <button
            type="button"
            onClick={fetchQuestion}
            className="px-6 py-3 border-2 border-gray-300 text-gray-700 rounded-lg font-semibold hover:border-gray-400 transition"
          >
            Skip Question
          </button>
        </div>
      </form>
    </div>
  );
}

export default Assessment;
