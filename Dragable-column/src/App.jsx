// import React, { useState, useEffect } from 'react';
// import Table from './Table';
// import './Table.css';

// const App = () => {
//   const getInitialColumns = () => {
//     const savedColumns = localStorage.getItem('columns');

//     if (savedColumns) {
//       return JSON.parse(savedColumns);
//     }
//     return [
//       { id: 'col-1', title: 'Name', data: ['Devanshu', 'Mohsin'] },
//       { id: 'col-2', title: 'Age', data: ['28', '34'] },
//       { id: 'col-3', title: 'Email', data: ['john.doe@example.com', 'jane.smith@example.com'] },
//     ];
//   };

//   const defaultColumns = [
//     { id: 'col-1', title: 'Name', data: ['Devanshu', 'Mohsin'] },
//     { id: 'col-2', title: 'Age', data: ['28', '34'] },
//     { id: 'col-3', title: 'Email', data: ['john.doe@example.com', 'jane.smith@example.com'] },
//   ];

//   const [columns, setColumns] = useState(getInitialColumns);
//   const [saveToLocalStorage, setSaveToLocalStorage] = useState(false);

//   useEffect(() => {
//     if (saveToLocalStorage) {
//       localStorage.setItem('columns', JSON.stringify(columns));
//       setSaveToLocalStorage(false);
//     }
//   }, [columns, saveToLocalStorage]);

//   const savePreferences = () => {
//     setSaveToLocalStorage(true);
//   };

//   const resetPreferences = () => {
//     setColumns(defaultColumns);
//     localStorage.removeItem('columns');
//   };

//   return (
//     <div>
//       <h1>Draggable Table</h1>
//       <div>
//         <button onClick={savePreferences}>Save Preferences</button>
//         <button onClick={resetPreferences}>Reset Preferences</button>
//       </div>
//       <Table columns={columns} setColumns={setColumns} />
//     </div>
//   );
// };

// export default App;
