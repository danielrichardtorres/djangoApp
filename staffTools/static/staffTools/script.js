// this is here


const draggables = document.querySelectorAll('#dragItem')//these are all the objects we can drag
const containers = document.querySelectorAll('#dragContainer')//these are all the places we can place!

// looks at all draggable items and knows when we're dragging it
draggables.forEach(draggable => {
    draggable.addEventListener('dragstart', ()=> {
        

        // adds it the given dragItem we started dragging to a subclass
        // dragItem.dragging
        // mainly so we can style it so the user knows its been 'picked up'
        draggable.classList.add('dragging')
    })

    draggable.addEventListener('dragend', ()=> {
        // once we stop dragging it 
        // removes it from the subclass #dragItem.dragging
        // lets the user know we're dropping it
        draggable.classList.remove('dragging')
    })
})


containers.forEach(container =>{
    container.addEventListener('dragover', e => {
        //prevent default makes the cursor look correct
        e.preventDefault()
        

        //uses our custom function to find the item below the hovered dragItem
        const afterElement = getDragAfterElement(container, e.clientY)
        // console.log(afterElement)

        const draggable = document.querySelector('.dragging')
        // we're not above anything
        if (afterElement == null ){
            container.appendChild(draggable)
        } else {
            container.insertBefore(draggable, afterElement)
        }

        
        
    })
} )

// this will get the dragItem directly below the one in the container we're hovering 
function getDragAfterElement(container, y){

    const draggableElements = [...container.querySelectorAll('#dragItem:not(.dragging)')]
    
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect()
        const offset = y - box.top - box.height / 2
        if (offset < 0 && offset > closest.offset) {
          return { offset: offset, element: child }
        } else {
          return closest
        }
      }, { offset: Number.NEGATIVE_INFINITY }).element
    }




