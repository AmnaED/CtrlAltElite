import ResourceQuantityForm from './ResourceQuantityForm';
import ResourceRequestForm from './ResourceRequestForm';
import './Resource.css'

function ResouceManagmementPage() {
  return (
    <div>
      <h1>Resource Management Page</h1>
      <h2 >Quantity Checked Out</h2>
       <ResourceQuantityForm quantity1 = "NULL #1"  quantity2 = "NULL #2"/>
      <h2 >Hardware Requests</h2>
      <ResourceRequestForm capacity1 = "NULL #1" available1 = "NULL #1" requestAmount1 = "NULL #1" capacity2 = "NULL #2" available2 = "NULL #2" requestAmount2 = "NULL #2"/>

    </div>
  );
}

export default ResouceManagmementPage;