import React, {useState} from "react";
import './Resource.css'

function ResourceRequestForm(props) {
  const [formData, setFormData] = useState({
    requestAmount1: '',
    requestAmount2: ''
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
    //eventually add case handler for button type (check-in and check-out)

    <form onSubmit={handleSubmit}>
        <div>
        <table id = "table1">
            <tr>
            <th class = "custom-padding"></th>
            <th class = "custom-padding">Total Capacity</th>
            <th class = "custom-padding">Currently Available</th>
            <th class = "custom-padding">Request Amount</th>
            </tr>
            <tr>
            <td>Hardware #1</td>
            <td class = "text-outline-box">{props.capacity1}</td>
            <td class = "text-outline-box">{props.available1}</td>
            <td class = "text-outline-box">
                <input type="text" name="requestAmount1" value = {formData.requestAmount1} onChange =  {handleInputChange}/>
            </td>
            </tr>
            <tr>
            <td>Hardware #2</td>
            <td class = "text-outline-box">{props.capacity2}</td>
            <td class = "text-outline-box">{props.available2}</td>
            <td class = "text-outline-box">
                <input type="text" name="requestAmount2" value = {formData.requestAmount2} onChange =  {handleInputChange}/>
            </td>
            </tr>
        </table>
        <button onClick={() => alert('Checking In Hardware!')}type="submit" name="action" value="checkin">Check-In</button>
        <button onClick={() => alert('Checking Out Hardware!')} type="submit" name="action" value="checkout">Check-Out</button>
        
        </div>        
    </form>
    );
}
export default ResourceRequestForm; 