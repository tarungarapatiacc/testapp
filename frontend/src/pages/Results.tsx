import React from 'react';
import { useLocation, Link } from 'react-router-dom';

interface Analysis {
  human_score: number;
  ai_comparison_score: number;
  creativity_index: number;
  nuance_score: number;
  out_of_box_thinking_score: number;
  feedback: string;
}

function ScoreBar({ label, score }: { label: string; score: number }) {
  const getColor = (score: number) => {
    if (score >= 80) return 'bg-green-500';
    if (score >= 60) return 'bg-blue-500';
    if (score >= 40) return 'bg-yellow-500';
    return 'bg-orange-500';
  };

  return (
    <div className="mb-4">
      <div className="flex justify-between mb-2">
        <span className="text-gray-700 font-semibold">{label}</span>
        <span className="text-gray-900 font-bold">{Math.round(score)}/100</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-3">
        <div
          className={`h-3 rounded-full transition-all ${getColor(score)}`}
          style={{ width: `${score}%` }}
        />
      </div>
    </div>
  );
}

function Results() {
  const location = useLocation();
  const { question, response, analysis } = location.state || {};

  if (!analysis) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-12 text-center">
        <p className="text-xl text-gray-600 mb-6">No results to display.</p>
        <Link
          to="/assessment"
          className="inline-block bg-indigo-600 text-white px-6 py-2 rounded hover:bg-indigo-700"
        >
          Back to Assessment
        </Link>
      </div>
    );
  }

  const avgScore = Math.round(
    (analysis.human_score +
      analysis.ai_comparison_score +
      analysis.creativity_index +
      analysis.nuance_score +
      analysis.out_of_box_thinking_score) /
      5
  );

  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">Assessment Results</h1>
        <p className="text-gray-600 mb-6">Here's how your thinking compares</p>

        {question && (
          <div className="mb-8 p-6 bg-gray-50 rounded-lg border-l-4 border-indigo-600">
            <h3 className="font-semibold text-gray-900 mb-2">{question.title}</h3>
            <p className="text-gray-700 mb-4">{question.description}</p>
          </div>
        )}
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        {/* Scores Card */}
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Your Scores</h2>
          <ScoreBar label="Human Thinking Index" score={analysis.human_score} />
          <ScoreBar
            label="AI Comparison Score"
            score={analysis.ai_comparison_score}
          />
          <ScoreBar label="Creativity Index" score={analysis.creativity_index} />
          <ScoreBar label="Nuance Score" score={analysis.nuance_score} />
          <ScoreBar
            label="Out-of-Box Thinking"
            score={analysis.out_of_box_thinking_score}
          />

          <div className="mt-8 pt-8 border-t-2 border-gray-200">
            <div className="text-center">
              <p className="text-gray-600 text-sm mb-2">Overall Score</p>
              <p className="text-5xl font-bold text-indigo-600">{avgScore}</p>
              <p className="text-gray-600 text-sm mt-2">/100</p>
            </div>
          </div>
        </div>

        {/* Feedback Card */}
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Insights</h2>
          <div className="space-y-4">
            <div className="p-4 bg-blue-50 border-l-4 border-blue-500 rounded">
              <p className="text-gray-800">{analysis.feedback}</p>
            </div>
          </div>

          <div className="mt-8">
            <h3 className="text-lg font-bold text-gray-900 mb-4">Key Findings</h3>
            <ul className="space-y-3">
              <li className="flex items-start">
                <span className="text-indigo-600 mr-3 text-lg">→</span>
                <span className="text-gray-700">
                  Your response shows{' '}
                  <strong>
                    {analysis.human_score > 70 ? 'strong' : 'moderate'} human reasoning
                  </strong>
                </span>
              </li>
              <li className="flex items-start">
                <span className="text-indigo-600 mr-3 text-lg">→</span>
                <span className="text-gray-700">
                  Creativity level:{' '}
                  <strong>
                    {analysis.creativity_index > 70 ? 'Excellent' : 'Good'}
                  </strong>
                </span>
              </li>
              <li className="flex items-start">
                <span className="text-indigo-600 mr-3 text-lg">→</span>
                <span className="text-gray-700">
                  Out-of-box thinking:{' '}
                  <strong>
                    {analysis.out_of_box_thinking_score > 70
                      ? 'Highly developed'
                      : 'Room to grow'}
                  </strong>
                </span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      {response && (
        <div className="bg-white rounded-lg shadow-lg p-8 mt-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Your Response</h2>
          <p className="text-gray-700 bg-gray-50 p-6 rounded-lg">{response}</p>
        </div>
      )}

      <div className="mt-8 text-center">
        <Link
          to="/assessment"
          className="inline-block bg-indigo-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-indigo-700 transition"
        >
          Try Another Question →
        </Link>
      </div>
    </div>
  );
}

export default Results;
