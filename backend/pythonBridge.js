// FinSight/backend/pythonBridge.js
const { spawn } = require('child_process');
const path = require('path');

/**
 * Execute Python script with arguments
 * @param {string} scriptPath - Relative path to Python script
 * @param {string[]} args - Array of arguments
 * @returns {Promise<Object>} - Parsed JSON output from Python
 */
function runPythonScript(scriptPath, args = []) {
  return new Promise((resolve, reject) => {
    // Resolve absolute path for reliability
    const absolutePath = path.resolve(__dirname, '..', scriptPath);
    
    console.log(`⚡ Launching Python: ${absolutePath} ${args.join(' ')}`);
    
    const pythonProcess = spawn('python', [absolutePath, ...args]);
    
    let output = '';
    let errorOutput = '';
    
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });
    
    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        const errorMsg = `❌ Python script exited with code ${code}\n${errorOutput}`;
        console.error(errorMsg);
        reject(new Error(errorMsg));
        return;
      }
      
      try {
        // Parse JSON output from Python
        const result = JSON.parse(output);
        console.log(`✅ Python output: ${Object.keys(result).join(', ')}`);
        resolve(result);
      } catch (parseError) {
        const errorMsg = `❌ Failed to parse Python output: ${parseError.message}\nOutput: ${output}`;
        console.error(errorMsg);
        reject(new Error(errorMsg));
      }
    });
    
    pythonProcess.on('error', (err) => {
      console.error(`❌ Failed to start Python process: ${err.message}`);
      reject(err);
    });
  });
}

module.exports = { runPythonScript };