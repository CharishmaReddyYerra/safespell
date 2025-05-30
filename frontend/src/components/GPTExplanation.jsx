import React from 'react';

const GPTExplanation = ({ phrase }) => {
  if (!phrase) {
    return (
      <div className="bg-gray-50 rounded-lg p-4 text-gray-500 text-sm">
        Select a highlighted phrase to see an explanation.
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-6 shadow-sm">
      <div className="mb-4 pb-4 border-b border-gray-100">
        <div className="flex items-center mb-2">
          <span className="text-lg mr-2">🤖</span>
          <h3 className="text-sm font-semibold text-gray-700">LLaMA Analysis</h3>
        </div>
        <span className="inline-block bg-red-100 text-red-800 px-3 py-1 rounded-full text-sm font-medium">
          "{phrase.phrase}"
        </span>
      </div>
      
      <div className="relative">
        <div className="absolute top-0 left-0 transform -translate-x-4 translate-y-1">
          <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
        </div>
        <div className="bg-gray-50 rounded-lg p-4 border-l-4 border-blue-500">
          <p className="text-gray-700 text-sm leading-relaxed">
            {phrase.explanation}
          </p>
        </div>
      </div>
      
      <div className="mt-4 flex items-center text-xs text-gray-500">
        <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
        </svg>
        <p>AI-generated explanation powered by LLaMA 3.2 via Ollama</p>
      </div>
    </div>
  );
};

export default GPTExplanation;