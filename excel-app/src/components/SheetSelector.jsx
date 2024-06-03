import React from 'react';

function SheetSelector({ sheets, onSheetChange }) {
  return (
    <div className="flex justify-center mt-4">
      <select 
        onChange={(e) => onSheetChange(e.target.value)} 
        className="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
      >
        {sheets.map((sheet, index) => (
          <option key={index} value={sheet}>
            {sheet}
          </option>
        ))}
      </select>
    </div>
  );
}

export default SheetSelector;
