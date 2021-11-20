import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/ToDos.js'
import LoginForm from './components/Auth.js'
import axios from 'axios'
import {HashRouter, Route, Link} from 'react-router-dom'
import Cookies from 'universal-cookie';


const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': [],
           'token': ''
       }
   }
  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token})
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token})
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
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
       this.get_token_from_storage()

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
             <li>
                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
             </li>
           </ul>
          </nav>
          <Route exact path='/users' component={() => <UserList users={this.state.users} />}  />
          <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
          <Route exact path='/todos' component={() => <TodoList items={this.state.todos} />} />
          <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
          <Route component={NotFound404} />
        </HashRouter>
      </div>
    )
  }

}
export default App;