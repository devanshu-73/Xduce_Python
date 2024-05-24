import React, { useState } from 'react';
import { DndContext, closestCenter } from '@dnd-kit/core';
import { arrayMove, SortableContext, horizontalListSortingStrategy, verticalListSortingStrategy } from '@dnd-kit/sortable';
import DraggableColumn from './DraggableColumn';
import { restrictToHorizontalAxis, restrictToVerticalAxis } from '@dnd-kit/modifiers';

const Table = ({ columns, setColumns }) => {
  const [columnHover, setColumnHover] = useState(false);

  const handleDragEnd = (event) => {
    const { active, over } = event;

    if (active.id !== over.id) {
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
      modifiers={[columnHover ? restrictToHorizontalAxis : restrictToVerticalAxis]}
    >
      <SortableContext
        items={columns.map(col => col.id)}
        strategy={columnHover ? horizontalListSortingStrategy : verticalListSortingStrategy}
      >
        <table className="draggable-table">
          <thead>
            <tr>
              {columns.map((column) => (
                <DraggableColumn key={column.id} column={column} setColumnHover={setColumnHover} />
              ))}
            </tr>
          </thead>
          <tbody>
            {columns[0].data.map((_, rowIndex) => (
              <tr key={rowIndex}>
                {columns.map((column) => (
                  <td key={column.id}>{column.data[rowIndex]}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </SortableContext>
    </DndContext>
  );
};

export default Table;
