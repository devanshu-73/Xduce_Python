import React from 'react-dom'
import Draggable, {DraggableCore} from 'react-draggable';
function MyDraggableComponent() {
  const eventHandler = (e, data) => {
    console.log('Event Type', e.type);
    console.log({e, data});
  }
 
  return (
    <Draggable
        onDrag={eventHandler}>
        <div style={{border: "2px solid red", padding: "1rem", width: "5%"}}>
          {/* <div className="handle">Drag from here</div>
          <div>This readme is really dragging on the onDrag react event listener...</div> */}
        </div>
    </Draggable>
  )
}
 
export default MyDraggableComponent;