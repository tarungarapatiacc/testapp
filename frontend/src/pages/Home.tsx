import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <main className="max-w-7xl mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-5xl font-bold text-gray-900 mb-4">
          Human vs AI Thinking Assessment
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Discover how your thinking differs from algorithmic approaches.
          Assess your out-of-the-box thinking, nuance, and creative problem-solving.
        </p>
        <Link
          to="/assessment"
          className="inline-block bg-indigo-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-indigo-700 transition text-lg"
        >
          Start Assessment →
        </Link>
      </div>

      <div className="grid md:grid-cols-3 gap-8">
        <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
          <div className="text-4xl mb-4">🎯</div>
          <h3 className="text-xl font-bold mb-3">Out-of-Box Thinking</h3>
          <p className="text-gray-600">
            Evaluate your ability to think laterally and challenge conventional assumptions.
          </p>
        </div>

        <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
          <div className="text-4xl mb-4">✨</div>
          <h3 className="text-xl font-bold mb-3">Nuanced Reasoning</h3>
          <p className="text-gray-600">
            Assess how you balance complexity, context, and multiple perspectives.
          </p>
        </div>

        <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition">
          <div className="text-4xl mb-4">🧠</div>
          <h3 className="text-xl font-bold mb-3">Human Intelligence</h3>
          <p className="text-gray-600">
            Compare your human reasoning with AI/algorithmic thinking approaches.
          </p>
        </div>
      </div>

      <div className="mt-12 bg-white p-8 rounded-lg shadow-md">
        <h2 className="text-2xl font-bold mb-4">How It Works</h2>
        <ol className="space-y-4 text-gray-700">
          <li className="flex items-start">
            <span className="font-bold text-indigo-600 mr-4">1.</span>
            <span>Answer thought-provoking questions across different categories</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold text-indigo-600 mr-4">2.</span>
            <span>Our AI analyzes your responses for creativity, nuance, and depth</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold text-indigo-600 mr-4">3.</span>
            <span>Get detailed insights on how your thinking differs from algorithms</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold text-indigo-600 mr-4">4.</span>
            <span>Explore your strengths in out-of-box thinking and business acumen</span>
          </li>
        </ol>
      </div>
    </main>
  );
}

export default Home;
