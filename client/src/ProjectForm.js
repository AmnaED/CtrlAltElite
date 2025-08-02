import React, {useState} from "react";

function ProjectForm(props) {
  const [formData, setFormData] = useState({
    Name: '',
    projectID: '',
    projectDescription: '',
  });

  function handleInputChange(event) {
    const { name, value } = event.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  }

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
                <input name = "Name" value = {formData.Name} onChange =  {handleInputChange}/>
            </label>
            <br />
            <label>
                Project Description:
                <input name = "projectDescription" value = {formData.projectDescription} onChange = {handleInputChange}/>
            </label>
            <br />
            </>
        )}
        <label>
            Project ID:
            <input name = "projectID" type = "number" value = {formData.projectID} onChange = {handleInputChange}/>
        </label>
            <br />
        <button type="submit">{props.buttonMessage}</button>
    </form>
    );
}
export default ProjectForm;