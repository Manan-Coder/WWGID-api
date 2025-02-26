async function getData(){
    try{
        const response = await fetch('http://37.27.51.34:46155//api/get-all');
        const data = await response.json();
        console.log(data);
        const tableBody = document.getElementById('table-body');
        tableBody.innerHTML = '';
        data.forEach(element => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${element.id}</td>
                             <td>${element.entry}</td>
                             <td>${element.date}</td>`;
            tableBody.appendChild(row);
        }); }
        catch(error){
            console.log(error);}
   

}
async function getRandData(){
    try{
        const response = await fetch("http://37.27.51.34:46155//api/get-random");
        const data = await response.json();
        console.log(data);
        const tableBody = document.getElementById('table-body-rnd');
        tableBody.innerHTML = '';
        const row = document.createElement('tr');
        row.innerHTML = `<td>${data.id}</td>
                            <td>${data.entry}</td>
                            <td>${data.date}</td>`;
        tableBody.appendChild(row);
         }
    
    catch(error){
        console.log(error);
    }}
async function getMtd(){
    try{
        const response = await fetch("http://37.27.51.34:46155//api/get-motivation");
        const data = await response.json();
        console.log(data);
        const para = document.getElementById('motivation');
        para.innerHTML = '';
        para.innerHTML = data;
            }
    
    catch(error){
        console.log(error);
    }}

    async function sendData() {
        const inputValue = document.getElementById('event').value.trim();
    
        if (!inputValue) {
            console.error("Error: Input is empty.");
            alert("Please enter an event before sending!");
            return;
        }
    
        const data = { entry: inputValue };
    
        try {
            const response = await fetch("http://37.27.51.34:46155//api/add", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });
    
            const resText = await response.text();  
            console.log("Raw Response:", resText);
    
            if (!response.ok) {
                throw new Error(resText); 
            }
    
            const res = JSON.parse(resText);  
            console.log("Response:", res);
            alert("Data sent successfully!");
    
        } catch (error) {
            console.error("Error sending data:", error);
            alert("Failed to send data: " + error.message);
        }
    }
    
    
    
getData();
getRandData();