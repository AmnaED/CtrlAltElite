import React, {useState} from "react";

function UserForm(props) {
  const [formData, setFormData] = useState({
    Name: '',
    userID: '',
    password: '',
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
return (

    <form onSubmit={handleSubmit}>
        <h2>{props.defaultMessage}</h2>
         {props.isNewUser && (
            <>
            <label>
                Name: 
                <input name = "Name" value = {formData.Name} onChange =  {handleInputChange}/>
            </label>
            <br />
            </>
        )}
        <label>
            Username:
            <input name = "userID" value = {formData.userID} onChange = {handleInputChange}/>
        </label>
        <br />
        <label>
            Password:
            <input name = "password" type = "text" value = {formData.password} onChange = {handleInputChange}/>
        </label>
            <br />
        <button type="submit">{props.buttonMessage}</button>
    </form>
    );
}

export default UserForm;