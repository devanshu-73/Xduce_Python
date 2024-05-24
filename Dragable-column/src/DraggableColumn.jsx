import React from 'react';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';

const DraggableColumn = ({ column, setColumnHover }) => {
  const { attributes, listeners, setNodeRef, transform, transition, isDragging } = useSortable({ id: column.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
  };

  return (
    <th
      ref={setNodeRef}
      style={style}
      className={`draggable-column ${isDragging ? 'dragging' : ''}`}
      {...attributes}
      {...listeners}
      onMouseEnter={() => setColumnHover(true)}
      onMouseLeave={() => setColumnHover(false)}
    >
      {column.title}
    </th>
  );
};

export default DraggableColumn;
