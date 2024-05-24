import React from 'react';
import { useSortable } from '@dnd-kit/sortable';

const DraggableColumn = ({ column }) => {
  const { attributes, listeners, setNodeRef, transform, isDragging } = useSortable({ id: column.id });

  return (
    <th
      ref={setNodeRef}
      style={{
        transform: transform ? `translate(${transform.x}px, ${transform.y}px)` : 'none',
        opacity: isDragging ? 0.5 : 1,
        cursor: 'grab',
      }}
      {...attributes}
      {...listeners}
    >
      {column.title}
    </th>
  );
};

export default DraggableColumn;
