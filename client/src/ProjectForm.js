import React, {useState} from "react";

function ProjectForm(props) {
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
/*
  async function addUser(used_id, project_id) {
    try {
      const response = await fetch (`http://localhost:5000/users/${formData.user_id}/projects` {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
      }
    }
  }
*/


  function handleSubmit(event) {
    event.preventDefault();
    console.log("Form Submitted", formData);
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