import React from 'react'


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.title}</td>
            <td>{item.text}</td>
            <td>{item.user}</td>
        </tr>
    )
}


const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>TITLE</th>
                <th>TEXT</th>
                <th>USER</th>
            </tr>
            {items.map((item) => <ToDoItem item={item} />)}
        </table>
    )
}


export default ToDoList