import React, { useState } from 'react';
import { DndContext, closestCenter } from '@dnd-kit/core';
import { arrayMove, SortableContext, verticalListSortingStrategy, horizontalListSortingStrategy } from '@dnd-kit/sortable';
import DraggableColumn from './DraggableColumn';
import './Table.css'; // Import the CSS file

const Table = ({ columns, setColumns }) => {
  const [columnHover, setColumnHover] = useState(false);

  const handleDragEnd = (event) => {
    const { active, over } = event;

    if (active.id!== over.id) {
      setColumns((columns) => {
        const oldIndex = columns.findIndex((col) => col.id === active.id);
        const newIndex = columns.findIndex((col) => col.id === over.id);
        return arrayMove(columns, oldIndex, newIndex);
      });
    }
  };

  return (
    <DndContext
      collisionDetection={closestCenter}
      onDragEnd={handleDragEnd}
    >
      <SortableContext items={columns.map((col) => col.id)} strategy={columnHover? horizontalListSortingStrategy : verticalListSortingStrategy}>
        <table className="draggable-table">
          <thead>
            <tr>
              {columns.map((column) => (
                <DraggableColumn key={column.id} column={column} setColumnHover={setColumnHover} />
              ))}
            </tr>
          </thead>
          <tbody>
            {columns.length > 0? (
              columns[0].data.map((_, rowIndex) => (
                <tr key={rowIndex}>
                  {columns.map((column) => (
                    <td key={column.id} className={columnHover? 'dragging' : ''}>
                      <SortableContext
                        items={column.data.map((_, index) => `${column.id}-${index}`)}
                        strategy={columnHover? verticalListSortingStrategy : horizontalListSortingStrategy}
                      >
                        <div>
                          {column.data[rowIndex]}
                        </div>
                      </SortableContext>
                    </td>
                  ))}
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={columns.length} className="no-data">
                  No data available
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </SortableContext>
    </DndContext>
  );
};

export default Table;