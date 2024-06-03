import React, { useState } from 'react';
import * as XLSX from 'xlsx';
import FileUpload from './components/FileUpload';
import SheetSelector from './components/SheetSelector';
import DataGrid from './components/DataGrid';
import './index.css'; // Ensure this points to the CSS file with Tailwind directives

function App() {
  const [sheets, setSheets] = useState([]);
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
      const binaryString = event.target.result;
      const workbook = XLSX.read(binaryString, { type: 'binary' });

      const sheetNames = workbook.SheetNames;
      setSheets(sheetNames);

      const firstSheet = sheetNames[0];
      loadSheetData(workbook, firstSheet);
    };

    reader.readAsBinaryString(file);
  };

  const handleSheetChange = (sheetName) => {
    const file = document.querySelector('input[type="file"]').files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
      const binaryString = event.target.result;
      const workbook = XLSX.read(binaryString, { type: 'binary' });

      loadSheetData(workbook, sheetName);
    };

    reader.readAsBinaryString(file);
  };

  const loadSheetData = (workbook, sheetName) => {
    const worksheet = workbook.Sheets[sheetName];
    const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

    const headers = json[0];
    const rows = json.slice(1);

    setColumns(headers);
    setData(rows);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-center text-2xl font-bold mb-4">Excel-like React App</h1>
      <FileUpload onFileChange={handleFileChange} />
      {sheets.length > 0 && (
        <SheetSelector sheets={sheets} onSheetChange={handleSheetChange} />
      )}
      {data.length > 0 && <DataGrid columns={columns} data={data} />}
    </div>
  );
}

export default App;
