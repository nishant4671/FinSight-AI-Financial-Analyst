// FinSight/frontend/src/components/SentimentIndicator.jsx
import React from 'react';

const SentimentIndicator = ({ sentiment }) => {
  // Determine color based on sentiment
  const getColor = () => {
    if (sentiment.includes('Bullish')) return '#4CAF50'; // Green
    if (sentiment.includes('Bearish')) return '#F44336'; // Red
    return '#FFC107'; // Yellow for neutral
  };

  return (
    <div className="sentiment-container">
      <h3>Market Sentiment</h3>
      <div 
        className="sentiment-indicator"
        style={{ backgroundColor: getColor() }}
      >
        {sentiment}
      </div>
    </div>
  );
};

export default SentimentIndicator;