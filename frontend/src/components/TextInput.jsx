import React, { useState } from 'react';

const TextInput = ({ onAnalyze, isLoading }) => {
  const [text, setText] = useState('');
  
  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAnalyze(text);
    }
  };

  const handleSampleText = () => {
    const sampleText = "You're overreacting as usual. No one will believe you if you tell them what happened. You're remembering it wrong anyway. If you really loved me, you wouldn't question me like this. You're lucky to have me after all I've done for you.";
    setText(sampleText);
  };

  const handleClear = () => {
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-4">
        <label htmlFor="text-input" className="block text-sm font-medium text-gray-700 mb-2">
          📝 Enter text to analyze for abusive or manipulative language
        </label>
        <div className="relative">
          <textarea
            id="text-input"
            rows="6"
            className="shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-lg p-4 border transition-all duration-200 resize-none"
            placeholder="Paste a conversation, message, or any text you want to analyze...\n\nExample: 'You're overreacting as usual. No one will believe you.'"
            value={text}
            onChange={(e) => setText(e.target.value)}
            disabled={isLoading}
          ></textarea>
          {text && (
            <button
              type="button"
              className="absolute top-2 right-2 text-gray-400 hover:text-gray-600 transition-colors"
              onClick={handleClear}
              disabled={isLoading}
              title="Clear text"
            >
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
              </svg>
            </button>
          )}
        </div>
        <div className="mt-1 text-xs text-gray-500">
          Character count: {text.length}
        </div>
      </div>
      
      <div className="flex items-center justify-between gap-3">
        <div className="flex gap-2">
          <button
            type="button"
            className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-lg text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-200"
            onClick={handleSampleText}
            disabled={isLoading}
          >
            📄 Load Sample Text
          </button>
          
          {text && (
            <button
              type="button"
              className="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-lg text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-200"
              onClick={handleClear}
              disabled={isLoading}
            >
              🗑️ Clear
            </button>
          )}
        </div>
        
        <button
          type="submit"
          className="inline-flex items-center px-6 py-2 border border-transparent text-sm font-medium rounded-lg shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
          disabled={isLoading || !text.trim()}
        >
          {isLoading ? (
            <>
              <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Analyzing with LLaMA...
            </>
          ) : (
            <>
              🔍 Analyze Text
            </>
          )}
        </button>
      </div>
    </form>
  );
};

export default TextInput;