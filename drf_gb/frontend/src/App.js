import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/ToDos.js'
import axios from 'axios'
import {HashRouter, Route, Link} from 'react-router-dom'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': []
       }
   }

    componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users/')
           .then(response => {
               const users = response.data.results
               console.log('Users: ', users)
                   this.setState(
                   {
                       'users': users
                   }
               )
           }).catch(error => console.log(error))
       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
               const projects = response.data.results
               console.log('Projects: ', projects)
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error))
       axios.get('http://127.0.0.1:8000/api/todos/')
           .then(response => {
               const todos = response.data.results
               console.log('Todos: ', todos)
                   this.setState(
                   {
                       'todos': todos
                   }
               )
           }).catch(error => console.log(error))
    }

   render() {
   return (
    <div className="App">
        <HashRouter>
        <nav>
           <ul>
             <li>
               <Link to='/users'>Users</Link>
             </li>
             <li>
               <Link to='/projects'>Projects</Link>
             </li>
             <li>
               <Link to='/todos'>ToDos</Link>
             </li>
           </ul>
          </nav>
          <Route exact path='/users' component={() => <UserList users={this.state.users} />}  />
          <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
          <Route exact path='/todos' component={() => <TodoList items={this.state.todos} />} />
        </HashRouter>
      </div>
    )
  }

}
export default App;