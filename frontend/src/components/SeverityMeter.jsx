import React from 'react';

const SeverityMeter = ({ score }) => {
  // Determine color based on severity score
  const getColor = (score) => {
    switch (score) {
      case 1:
        return 'bg-green-500';
      case 2:
        return 'bg-yellow-400';
      case 3:
        return 'bg-orange-400';
      case 4:
        return 'bg-orange-600';
      case 5:
        return 'bg-red-600';
      default:
        return 'bg-gray-300';
    }
  };

  // Get label based on severity score
  const getLabel = (score) => {
    switch (score) {
      case 1:
        return 'Low';
      case 2:
        return 'Mild';
      case 3:
        return 'Moderate';
      case 4:
        return 'High';
      case 5:
        return 'Severe';
      default:
        return 'Unknown';
    }
  };

  return (
    <div className="w-full">
      <div className="flex justify-between items-center mb-2">
        <div className="flex items-center">
          <span className="text-sm font-medium text-gray-700 mr-2">Severity Level:</span>
          <span className={`font-bold text-lg ${score >= 4 ? 'text-red-600' : score >= 3 ? 'text-orange-600' : score >= 2 ? 'text-yellow-600' : 'text-green-600'}`}>
            {getLabel(score)}
          </span>
        </div>
        <span className="text-sm text-gray-500">({score}/5)</span>
      </div>
      
      <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden shadow-inner">
        <div 
          className={`h-full ${getColor(score)} transition-all duration-500 ease-out rounded-full`} 
          style={{ width: `${score * 20}%` }}
        ></div>
      </div>
      
      <div className="flex justify-between mt-1 text-xs text-gray-500">
        <span>🟢 Low</span>
        <span>🟡 Mild</span>
        <span>🟠 Moderate</span>
        <span>🔴 High</span>
        <span>🚨 Severe</span>
      </div>
    </div>
  );
};

export default SeverityMeter;