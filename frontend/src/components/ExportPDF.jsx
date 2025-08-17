import React from 'react';
import axios from 'axios';
import { Button } from '@mui/material';
import PictureAsPdfIcon from '@mui/icons-material/PictureAsPdf';

const ExportPDF = ({ report, symbol }) => {
  const handleExport = async () => {
    try {
      const response = await axios.post(
        'http://localhost:5000/api/export-pdf',
        {
          title: `${symbol} Financial Analysis Report`,
          content: report,
          author: "FinSight AI Analyst"
        },
        { responseType: 'blob' } // Important for binary data
      );
      
      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${symbol}_financial_report.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      
    } catch (error) {
      console.error('Export failed:', error);
      alert('Export failed. Please try again.');
    }
  };

  return (
    <Button 
      variant="contained" 
      color="primary" 
      startIcon={<PictureAsPdfIcon />}
      onClick={handleExport}
      disabled={!report}
      style={{ marginLeft: '10px' }}
    >
      Export PDF
    </Button>
  );
};

export default ExportPDF;