// FinSight/frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import SentimentIndicator from './components/SentimentIndicator';
import ForecastChart from './components/ForecastChart';
import ReportViewer from './components/ReportViewer';
import './App.css';

function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (symbol) => {
    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post(
        'http://localhost:5000/api/analyze',
        { symbol }
      );
      
      setAnalysisResult(response.data);
    } catch (err) {
      setError('Analysis failed. Please try again later.');
      console.error('Analysis error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>FinSight AI Financial Analyst</h1>
        <p>AI-powered stock analysis and forecasting</p>
      </header>
      
      <SearchBar onSearch={handleSearch} />
      
      {loading && <div className="loading-indicator">Analyzing...</div>}
      {error && <div className="error-message">{error}</div>}
      
      {analysisResult && !loading && (
        <div className="dashboard">
          <div className="dashboard-row">
            <div className="dashboard-col">
              <SentimentIndicator sentiment={analysisResult.sentiment} />
            </div>
            <div className="dashboard-col">
              <ForecastChart data={analysisResult.forecastData} />
            </div>
          </div>
          
          <div className="dashboard-row">
            <div className="dashboard-col full-width">
              <ReportViewer report={analysisResult.report} />
            </div>
          </div>
        </div>
      )}
      
      <footer className="app-footer">
        <p>FinSight AI - Professional Financial Analysis Platform</p>
      </footer>
    </div>
  );
}

export default App;