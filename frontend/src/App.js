import React, { useState } from 'react';
import TextInput from './components/TextInput';
import Results from './components/Results';
import SeverityMeter from './components/SeverityMeter';
import GPTExplanation from './components/GPTExplanation';
import axios from 'axios';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [results, setResults] = useState(null);
  const [selectedPhrase, setSelectedPhrase] = useState(null);

  const analyzeText = async (text) => {
    setIsLoading(true);
    setError(null);
    setResults(null);
    setSelectedPhrase(null);
    
    try {
      const response = await axios.post('http://localhost:8000/analyze', { text });
      setResults(response.data);
      
      // If there are flagged phrases, select the first one by default
      if (response.data.flagged_phrases && response.data.flagged_phrases.length > 0) {
        setSelectedPhrase(response.data.flagged_phrases[0]);
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred while analyzing the text');
    } finally {
      setIsLoading(false);
    }
  };

  const handlePhraseClick = (phrase) => {
    setSelectedPhrase(phrase);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-gradient-to-r from-blue-600 to-blue-800 shadow-lg">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <h1 className="text-3xl font-bold text-white flex items-center">
                <span className="text-yellow-300 mr-3 text-4xl">🛡️</span>
                SAFESPELL
              </h1>
              <div className="ml-4 px-3 py-1 bg-blue-500 rounded-full">
                <span className="text-xs font-medium text-blue-100">Powered by LLaMA 3.2</span>
              </div>
            </div>
            <div className="text-right">
              <p className="text-blue-100 font-medium">AI-Powered Language Analysis</p>
              <p className="text-xs text-blue-200">Detect harmful and manipulative language patterns</p>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-8 sm:px-0">
          <div className="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-100">
            <div className="p-8">
              <div className="text-center mb-6">
                <h2 className="text-2xl font-bold text-gray-900 mb-2">Analyze Text for Harmful Language</h2>
                <p className="text-gray-600">Our AI analyzes text patterns to identify potentially abusive or manipulative language</p>
              </div>
              <TextInput onAnalyze={analyzeText} isLoading={isLoading} />
            </div>

            {error && (
              <div className="p-4 bg-red-50 border-t border-red-200">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <h3 className="text-sm font-medium text-red-800">Error</h3>
                    <div className="mt-2 text-sm text-red-700">
                      <p>{error}</p>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {results && (
              <div className="border-t border-gray-200 bg-gray-50">
                <div className="p-8">
                  <div className="flex items-center justify-between mb-6">
                    <h3 className="text-xl font-bold text-gray-900 flex items-center">
                      📊 Analysis Results
                    </h3>
                    <div className="text-sm text-gray-500">
                      Analysis completed in {new Date().toLocaleTimeString()}
                    </div>
                  </div>
                  
                  {results.flagged_phrases && results.flagged_phrases.length > 0 ? (
                    <>
                      <div className="mb-8 bg-white rounded-lg p-6 shadow-sm border border-gray-200">
                        <h4 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
                          ⚠️ Severity Assessment
                        </h4>
                        <SeverityMeter score={results.severity_score} />
                      </div>
                      
                      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        <div className="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
                          <h4 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
                            🔍 Text Analysis
                          </h4>
                          <Results 
                            originalText={results.original_text} 
                            flaggedPhrases={results.flagged_phrases}
                            onPhraseClick={handlePhraseClick}
                            selectedPhrase={selectedPhrase}
                          />
                        </div>
                        
                        <div className="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
                          <h4 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
                            💡 AI Explanation
                          </h4>
                          {selectedPhrase ? (
                            <GPTExplanation phrase={selectedPhrase} />
                          ) : (
                            <div className="bg-blue-50 rounded-lg p-6 text-blue-700 text-sm border border-blue-200">
                              <div className="flex items-center mb-2">
                                <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                                </svg>
                                <span className="font-medium">Select a highlighted phrase</span>
                              </div>
                              <p>Click on any red-highlighted text above to see a detailed explanation from our AI model.</p>
                            </div>
                          )}
                        </div>
                      </div>
                    </>
                  ) : (
                    <div className="bg-green-50 rounded-lg p-8 text-center border border-green-200">
                      <div className="text-6xl mb-4">✅</div>
                      <h4 className="text-xl font-bold text-green-800 mb-2">Great News!</h4>
                      <p className="text-green-700 mb-4">No potentially harmful language patterns were detected in your text.</p>
                      <div className="bg-white rounded-lg p-4 border border-green-200">
                        <p className="text-gray-700 text-sm">"{results.original_text}"</p>
                      </div>
                      <p className="text-xs text-green-600 mt-4">This text appears to use respectful and constructive language.</p>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </main>

      <footer className="bg-gray-800 border-t border-gray-700 mt-12">
        <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="flex items-center justify-center mb-4">
              <span className="text-2xl mr-2">🛡️</span>
              <span className="text-lg font-bold text-white">SAFESPELL</span>
            </div>
            <p className="text-sm text-gray-300 mb-2">
              AI-Powered Language Analysis Tool
            </p>
            <p className="text-xs text-gray-400">
              Powered by LLaMA 3.2 via Ollama • Built with React & Tailwind CSS
            </p>
            <div className="mt-4 flex items-center justify-center space-x-4 text-xs text-gray-500">
              <span>🔒 Privacy-focused</span>
              <span>•</span>
              <span>🚀 Real-time analysis</span>
              <span>•</span>
              <span>🧠 Advanced AI</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;