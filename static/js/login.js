function validate() {
    var nameInput = document.getElementById("name or mail");
    var name = nameInput.value; 

    var pasInput = document.getElementById("password");
    var password = pasInput.value;

    if (name == "" || name == null) {
        alert("Name or Email is required");
        
    } else if(password == "" || password == null){
        alert("Enter Password");
    } else{
        alert("Welcome Back "+name+" Enjoy!");
    }
    
}