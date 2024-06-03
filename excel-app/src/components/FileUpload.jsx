import React from 'react';

function FileUpload({ onFileChange }) {
  return (
    <div className="flex justify-center mt-6">
      <label className="cursor-pointer inline-block px-6 py-3 bg-blue-600 text-white font-semibold rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
        Upload Excel File
        <input 
          type="file" 
          accept=".xlsx, .xls" 
          onChange={onFileChange} 
          className="hidden"
        />
      </label>
    </div>
  );
}

export default FileUpload;
