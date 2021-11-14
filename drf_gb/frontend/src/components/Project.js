import React from 'react'


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.repository}</td>
            <td>{item.name}</td>
        </tr>
    )
}


const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>REPO</th>
                <th>NAME</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}


export default ProjectList