import React, { useState, useEffect } from 'react';
import Table from './Table';
import './Table.css';

const App = () => {
  // Function to load columns from local storage
  const loadColumns = () => {
    const savedColumns = localStorage.getItem('columns');
    return savedColumns ? JSON.parse(savedColumns) : [
      { id: 'col-1', title: 'Name', data: ['John Doe', 'Jane Smith'] },
      { id: 'col-2', title: 'Age', data: ['28', '34'] },
      { id: 'col-3', title: 'Email', data: ['john.doe@example.com', 'jane.smith@example.com'] },
    ];
  };

  const [columns, setColumns] = useState(loadColumns);

  // save columns to local storage whenever they change
  useEffect(() => {
    localStorage.setItem('columns', JSON.stringify(columns));
  }, [columns]);

  return (
    <div>
      <h1>Draggable Table</h1>
      <Table columns={columns} setColumns={setColumns} />
    </div>
  );
};

export default App;
