import React, { useState } from 'react';
import Table from './Table';
import './Table.css'; // Ensure this CSS file is imported

const App = () => {
  const [columns, setColumns] = useState([
    { id: 'col-1', title: 'Name', data: ['John Doe', 'Jane Smith'] },
    { id: 'col-2', title: 'Age', data: ['28', '34'] },
    { id: 'col-3', title: 'Email', data: ['john.doe@example.com', 'jane.smith@example.com'] },
  ]);

  return (
    <div>
      <h1>Draggable Table</h1>
      <Table columns={columns} setColumns={setColumns} />
    </div>
  );
};

export default App;
