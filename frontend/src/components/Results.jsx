import React from 'react';

const Results = ({ originalText, flaggedPhrases, onPhraseClick, selectedPhrase }) => {
  // If no flagged phrases, just return the original text
  if (!flaggedPhrases || flaggedPhrases.length === 0) {
    return (
      <div className="bg-white rounded-lg border border-gray-200 p-4">
        <p className="text-gray-800">{originalText}</p>
        <p className="mt-4 text-sm text-green-600 font-medium">No potentially harmful language detected.</p>
      </div>
    );
  }

  // Sort flagged phrases by their position in the text (start_index)
  const sortedPhrases = [...flaggedPhrases].sort((a, b) => a.start_index - b.start_index);

  // Build the highlighted text
  const buildHighlightedText = () => {
    let result = [];
    let lastIndex = 0;

    sortedPhrases.forEach((phrase, index) => {
      // Add text before the phrase
      if (phrase.start_index > lastIndex) {
        result.push(
          <span key={`text-${index}`}>
            {originalText.substring(lastIndex, phrase.start_index)}
          </span>
        );
      }

      // Add the highlighted phrase
      const isSelected = selectedPhrase && selectedPhrase.start_index === phrase.start_index;
      result.push(
        <span 
          key={`phrase-${index}`}
          className={`highlighted-text cursor-pointer transition-all duration-200 hover:bg-red-300 ${isSelected ? 'bg-red-200 border-red-600 shadow-sm' : ''}`}
          onClick={() => onPhraseClick(phrase)}
          title="Click to see explanation"
        >
          {originalText.substring(phrase.start_index, phrase.end_index)}
        </span>
      );

      lastIndex = phrase.end_index;
    });

    // Add any remaining text after the last phrase
    if (lastIndex < originalText.length) {
      result.push(
        <span key="text-end">
          {originalText.substring(lastIndex)}
        </span>
      );
    }

    return result;
  };

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <p className="text-gray-800 whitespace-pre-line">{buildHighlightedText()}</p>
      
      <div className="mt-4 text-sm text-red-600">
        <p className="font-medium">Found {flaggedPhrases.length} potentially harmful phrase{flaggedPhrases.length !== 1 ? 's' : ''}</p>
        <p className="text-xs text-gray-500 mt-1">Click on any highlighted text to see an explanation</p>
      </div>
    </div>
  );
};

export default Results;