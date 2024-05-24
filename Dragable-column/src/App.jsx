import React, { useState, useEffect } from 'react';
import Table from './Table';
import './Table.css';

const App = () => {
  // Function to get columns from local storage or use default
  const getInitialColumns = () => {
    const savedColumns = localStorage.getItem('columns');

    if (savedColumns) {
      return JSON.parse(savedColumns);
    }
    return [
      { id: 'col-1', title: 'Name', data: ['Devanshu', 'Mohsin'] },
      { id: 'col-2', title: 'Age', data: ['28', '34'] },
      { id: 'col-3', title: 'Email', data: ['john.doe@example.com', 'jane.smith@example.com'] },
    ];
  };
  const [columns, setColumns] = useState(getInitialColumns);

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
