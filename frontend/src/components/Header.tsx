import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="bg-white shadow-md">
      <nav className="max-w-7xl mx-auto px-4 py-6 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-indigo-600">
          🧠 Human vs AI
        </Link>
        <div className="space-x-6">
          <Link to="/" className="text-gray-700 hover:text-indigo-600 transition">
            Home
          </Link>
          <Link to="/assessment" className="text-gray-700 hover:text-indigo-600 transition">
            Assessment
          </Link>
        </div>
      </nav>
    </header>
  );
}

export default Header;
