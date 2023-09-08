
function validate() {
    var nameInput = document.getElementById("name");
    var name = nameInput.value; 

    var emailInput = document.getElementById("mail");
    var email = emailInput.value;

    var pasInput = document.getElementById("password");
    var password = pasInput.value;


    if (name == "" || name == null) {
        alert("Full Name is required");
        
    } else if(email == "" || email== null) {
        alert("Email is required");
        
    } else if(password == "" || password == null){
        alert("Enter Password");
    } else{
        alert("Welcome "+name+" Enjoy!");
    }
    
}