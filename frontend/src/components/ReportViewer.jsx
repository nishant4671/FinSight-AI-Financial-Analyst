// FinSight/frontend/src/components/ReportViewer.jsx
import React, { useState } from 'react';

const ReportViewer = ({ report }) => {
  const [expanded, setExpanded] = useState(false);

  // Format the report text
  const formatReport = (text) => {
    return text.split('\n').map((paragraph, index) => (
      <p key={index} className="report-paragraph">
        {paragraph}
      </p>
    ));
  };

  return (
    <div className={`report-container ${expanded ? 'expanded' : ''}`}>
      <div className="report-header">
        <h3>Financial Analysis Report</h3>
        <button 
          onClick={() => setExpanded(!expanded)}
          className="toggle-button"
        >
          {expanded ? 'Collapse' : 'Expand'}
        </button>
      </div>
      <div className="report-content">
        {report ? formatReport(report) : <p>No report generated yet</p>}
      </div>
    </div>
  );
};

export default ReportViewer;
// Add to imports
import ExportPDF from './ExportPDF';

// Add to component return
<div className="report-header">
  <h3>Financial Analysis Report</h3>
  <div>
    <button 
      onClick={() => setExpanded(!expanded)}
      className="toggle-button"
    >
      {expanded ? 'Collapse' : 'Expand'}
    </button>
    <ExportPDF report={report} symbol={symbol} />
  </div>
</div>