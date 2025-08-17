// FinSight/frontend/src/components/ForecastChart.jsx
import React from 'react';
import Plot from 'react-plotly.js';

const ForecastChart = ({ data }) => {
  // Check if data is available
  if (!data || !data.ds || !data.yhat) {
    return (
      <div className="chart-container">
        <p>Loading forecast data...</p>
      </div>
    );
  }

  return (
    <div className="chart-container">
      <h3>Price Forecast</h3>
      <Plot
        data={[
          {
            x: data.ds,
            y: data.yhat,
            type: 'scatter',
            mode: 'lines',
            name: 'Forecast',
            line: { color: '#3f51b5' }
          },
          {
            x: data.ds,
            y: data.yhat_upper,
            type: 'scatter',
            mode: 'lines',
            fill: 'tonexty',
            fillcolor: 'rgba(63, 81, 181, 0.2)',
            line: { width: 0 },
            name: 'Upper Bound'
          },
          {
            x: data.ds,
            y: data.yhat_lower,
            type: 'scatter',
            mode: 'lines',
            fill: 'tonexty',
            fillcolor: 'rgba(63, 81, 181, 0.2)',
            line: { width: 0 },
            name: 'Lower Bound'
          }
        ]}
        layout={{
          autosize: true,
          margin: { l: 40, r: 30, t: 30, b: 40 },
          hovermode: 'closest',
          xaxis: { title: 'Date' },
          yaxis: { title: 'Price ($)' }
        }}
        config={{ responsive: true }}
        style={{ width: '100%', height: '300px' }}
      />
    </div>
  );
};

export default ForecastChart;