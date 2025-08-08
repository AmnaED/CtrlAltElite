import React, {useState} from "react";
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import API_BASE_URL from './config';



function ProjectForm(props) {
  const navigate = useNavigate();
  const { user_id } = useParams();
  const [formData, setFormData] = useState({
    project_id: '',
    project_name: '',
    project_description: '',
  });

  function handleInputChange(event) {
    const { name, value } = event.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  }

  async function addUser(project_id) {

    try {
      const response = await fetch (`${API_BASE_URL}/projects/${Number(project_id)}/users`, {
      //const response = await fetch (`http://127.0.0.1:5000/projects/${Number(project_id)}/users`, {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({user_id: user_id,}),
      });
      const data = await response.json();
      console.log("Data recieved", data.message);

      if (response.ok) {
        console("User added to project");
        return response;
      } else {
        alert(data.error || "Error in adding user to project");
        return response;
      }
    } catch (error) {
      console.error("Error adding user to project:", error);
      alert("Error adding user to project.");
    }
  }


  async function addProject(user_id, project_id) {

    try {
      const response = await fetch (`${API_BASE_URL}/users/${user_id}/projects`, {
      //const response = await fetch (`http://127.0.0.1:5000/users/${user_id}/projects`, {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({project_id: Number(project_id)}),
      });
      const data = await response.json();
      console.log("Data recieved", data.message);

      if (response.ok) {
        console.log("Project added to User");
        return response;
      } else {
        alert(data.error || "Error in adding project to user");
        return response;
      }
    } catch (error) {
      console.error("Error adding project to user:", error);
      alert("Error adding project to user.");
    }
  }

  async function handleSubmit(event) {
        
    event.preventDefault();
    console.log("Form Submitted", formData);

    if (props.isNewProject) {
      try {
        const response = await fetch(`${API_BASE_URL}/projects`,{
       // const response = await fetch("http://127.0.0.1:5000/projects",{
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify(formData),
        });
        const data = await response.json();
        console.log("Data recieved from Flask", data);
        alert(data.message);
        if (!response.ok) {
          alert(data.error);
          return;
        }
          const projectId = data.project_id;
          const addUserResponse = await addUser(projectId);
          const addProjectResponse = await addProject(user_id, projectId);
          if (addUserResponse?.ok && addProjectResponse?.ok) {
            setFormData({ project_id: '', project_name: '', project_description: '' });
            alert("Both user and project linked successfully!");
            navigate(`/users/${user_id}/projects/${projectId}/resources`);
          } else if (addUserResponse?.ok && !addProjectResponse?.ok) {
            console.log("User added to project, error adding project to user.");
          } else if (!addUserResponse?.ok && addProjectResponse?.ok) {
            console.log("Project added to user, user already in project.");
          } else {
            alert("Failed to link user and project.");
          }
        } catch (error) {
          console.error("Error submitting form:", error);
          alert("An error occurred. Please try again.");
        }
    } else {
      try {
        const response = await fetch (`${API_BASE_URL}/projects/${Number(formData.project_id)}`);
     //  const response = await fetch (`http://127.0.0.1:5000/projects/${Number(formData.project_id)}`);
        const data = await response.json();
        if (!response.ok) {
        alert(data.error || "Could not find project");
        return;
       }
       console.log("Project found");
       const projectId = data.project_id;
          const addUserResponse = await addUser(projectId);
          const addProjectResponse = await addProject(user_id, projectId)
          if (addUserResponse?.ok && addProjectResponse?.ok) {
            setFormData({ project_id: '', project_name: '', project_description: '' });
            alert("Both user and project linked successfully!");
          } else if (addUserResponse?.ok && !addProjectResponse?.ok) {
            console.log("User added to project, error adding project to user.");
          } else if (!addUserResponse?.ok && addProjectResponse?.ok) {
            console.log("Project added to user, user already in project.");
          } else {
            alert("Failed to link user and project.");
          }
        } catch (error) {
          console.error("Error submitting form:", error);
          alert("An error occurred. Please try again.");
        }
    }
  }
return(

    <form onSubmit={handleSubmit}>
        <h2>{props.defaultMessage}</h2>
        {props.isNewProject && (
            <>
            <label>
                Project Name: 
                <input name = "project_name" value = {formData.project_name} onChange =  {handleInputChange}/>
            </label>
            <br />
            <label>
                Project Description:
                <input name = "project_description" value = {formData.project_description} onChange = {handleInputChange}/>
            </label>
            <br />
            </>
        )}
        <label>
            Project ID:
            <input name = "project_id" type = "number" value = {formData.project_id} onChange = {handleInputChange}/>
        </label>
            <br />
        <button type="submit">{props.buttonMessage}</button>
    </form>
    );
}
export default ProjectForm;