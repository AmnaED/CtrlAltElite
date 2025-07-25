import React from 'react';
import ReactDOM from 'react-dom/client';
// import './index.css';
//import App from './App';
import reportWebVitals from './reportWebVitals';
import UserForm from './UserForm';
import ProjectForm from './ProjectForm';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
   <React.StrictMode>
    <div>
      <UserForm defaultMessage = "New User? Create an Account: " buttonMessage = "Create Account" isNewUser={true}/>
      <UserForm defaultMessage = "Returning User? Log In: " buttonMessage = "Log In"/>
      <ProjectForm defaultMessage = "Enter New Project Information: " buttonMessage = "Create Project" isNewProject={true}/>
      <ProjectForm defaultMessage = "Current/Join Project: " buttonMessage = "Join Project"/>
    </div>

   </React.StrictMode>
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
