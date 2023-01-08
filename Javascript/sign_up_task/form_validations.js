
var user_list=[]
var pass_list=[]

function validations(x,y){
    var name1 = document.getElementById("fname").value
    var name1ptr=/^[a-zA-Z ]+$/
    var name2 = document.getElementById("lname").value            

    // for first name text box

    if (name1=="" ){
        document.getElementById("fnamemsg").innerHTML="First Name field is empty*"
        document.getElementById("fnamemsg").style.fontSize="14px"
        document.getElementById("fnamemsg").style.color="red"
        
    }
    else if (name1.match(name1ptr)){
        document.getElementById("fnamemsg").innerHTML="Correct"
        document.getElementById("fnamemsg").style.fontSize="14px"
        document.getElementById("fnamemsg").style.color="green"
        
    }
    else {
        document.getElementById("fnamemsg").innerHTML="Special Characters and Numbers are not allowed *"
        document.getElementById("fnamemsg").style.fontSize="14px"
        document.getElementById("fnamemsg").style.color="red"
        
    }

    // for last name text box

    if (name2=="" ){
        document.getElementById("lnamemsg").innerHTML="Last Name field is empty*"
        document.getElementById("lnamemsg").style.fontSize="14px"
        document.getElementById("lnamemsg").style.color="red"
        
    }
    else if (name2.match(name1ptr)){
        document.getElementById("lnamemsg").innerHTML="Correct"
        document.getElementById("lnamemsg").style.fontSize="14px"
        document.getElementById("lnamemsg").style.color="green"
        
    }
    else {
        document.getElementById("lnamemsg").innerHTML="Special Characters and Numbers are not allowed *"
        document.getElementById("lnamemsg").style.fontSize="14px"
        document.getElementById("lnamemsg").style.color="red"
        
    }

    // for gender radio button

    var v1=document.getElementsByName("gender");

    // document.write(v1)
    if (v1[0].checked || v1[1].checked || v1[2].checked){
        document.getElementById("gen").innerHTML="Correct"
        document.getElementById("gen").style.fontSize="14px"
        document.getElementById("gen").style.color="green"
    }
    else{
        document.getElementById("gen").innerHTML="Select Proper Gender.*"
        document.getElementById("gen").style.fontSize="14px"
        document.getElementById("gen").style.color="red"
    }

    // for contact number
    var c_number=document.getElementById("number").value

    var c_ptr=/^[\d]+$/

    if (c_number==""){
        document.getElementById("c_no").innerHTML="Contact Field is empty.*"
        document.getElementById("c_no").style.fontSize="14px"
        document.getElementById("c_no").style.color="red"
        
    }
    else if(c_number.match(c_ptr) && c_number.length==10){
        document.getElementById("c_no").innerHTML="Correct"
        document.getElementById("c_no").style.fontSize="14px"
        document.getElementById("c_no").style.color="green"
    }
    else if(c_number.length  > 10 || c_number.length < 10){
        document.getElementById("c_no").innerHTML="Contact must be of 10 digitd only.*"
        document.getElementById("c_no").style.fontSize="14px"
        document.getElementById("c_no").style.color="red"
    }
    else{
        document.getElementById("c_no").innerHTML="Contact must contain numbers only."
        document.getElementById("c_no").style.fontSize="14px"
        document.getElementById("c_no").style.color="red"
    }

    // for email 
    var user_name=document.getElementById("email").value
    var user_name_ptr=/^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$/
    
    if (user_name==""){
        document.getElementById("user_name").innerHTML=" Email field is empty.*"
        document.getElementById("user_name").style.fontSize="14px"
        document.getElementById("user_name").style.color="red"
    }
    else if(user_name.match(user_name_ptr)){
        document.getElementById("user_name").innerHTML="Correct"
        document.getElementById("user_name").style.fontSize="14px"
        document.getElementById("user_name").style.color="green"
    }
    else{
        document.getElementById("user_name").innerHTML=" Invalid Email Id.*"
        document.getElementById("user_name").style.fontSize="14px"
        document.getElementById("user_name").style.color="red"
    }

    // for password
    var user_pass=document.getElementById("pass").value
    var user_pass_confirm=document.getElementById("pass1").value

    if (user_pass.length < 6) {
        
        document.getElementById("p_word").innerHTML=" Minimum 6 character password required.*"
        document.getElementById("p_word").style.fontSize="14px"
        document.getElementById("p_word").style.color="red"
    }
    else if (user_pass.length < 16 && user_pass==user_pass_confirm){
        document.getElementById("p_word").innerHTML="Correct"
        document.getElementById("p_word").style.fontSize="14px"
        document.getElementById("p_word").style.color="green"
        
        document.getElementById("p_word1").innerHTML="Correct"
        document.getElementById("p_word1").style.fontSize="14px"
        document.getElementById("p_word1").style.color="green"
    }

    else if(user_pass.length <= 16 && user_pass != user_pass_confirm){
        document.getElementById("p_word1").innerHTML=" Password does not match.*"
        document.getElementById("p_word1").style.fontSize="14px"
        document.getElementById("p_word1").style.color="red"
    }
    else{
        document.getElementById("p_word").innerHTML=" Maximum 15 character password allowed.*"
        document.getElementById("p_word").style.fontSize="14px"
        document.getElementById("p_word").style.color="red"
    }

    if ((((((document.getElementById("fnamemsg").textContent=="Correct" && document.getElementById("lnamemsg").textContent=="Correct") && document.getElementById("gen").textContent=="Correct") && document.getElementById("c_no").textContent=="Correct") && document.getElementById("user_name").textContent=="Correct") && document.getElementById("p_word").textContent=="Correct") && document.getElementById("p_word1").textContent=="Correct") {

        if (confirm("ALL INFORMATION PROVIDED IS TRUE AND CORRECT...?") == true) {
            user_list.push(x.value)
            pass_list.push(y.value)
            console.log(user_list)
            console.log(pass_list)
            alert("REGISTERED SUCCESFULLY !!!...\n\nYOU CAN LOG IN NOW !!")

            // reseting values of inputs

            document.getElementById("fname").value=""
            document.getElementById("lname").value=""
            document.getElementById("number").value=""
            document.getElementById("email").value=""
            document.getElementById("pass").value=""
            document.getElementById("pass1").value=""

            // deselect the radio button

            v1[0].checked=false;
            v1[1].checked=false;
            v1[2].checked=false;

            // document.getElementById("show").checked=false;

            // reseting values of spans 

            document.getElementById("fnamemsg").textContent=""
            document.getElementById("lnamemsg").textContent=""
            document.getElementById("gen").textContent=""
            document.getElementById("c_no").textContent=""
            document.getElementById("user_name").textContent=""
            document.getElementById("p_word").textContent=""
            document.getElementById("p_word1").textContent=""

            return false

        }

        else {
            return false
        }

    }
    
    return false
}


function showpass(){
    var p1=document.getElementById("pass");
    var p2=document.getElementById("pass1");
    

    if (p1.type=="password" && p1.type=="password"){
        p1.type="text"
        p2.type="text"
    }        
    else{
        p1.type="password"
        p2.type="password"
    }
}

function logging_in(user,password){

    if ((user_list.indexOf(user.value) >= 0) && (user_list.indexOf(user.value) == pass_list.indexOf(password.value))) {
        document.getElementById("log_email").value=""
        document.getElementById("log_pass").value=""
        return true

    }
    else{

        alert("INCORRECT USER ID OR PASSWORD !!!")
        document.getElementById("log_email").value=""
        document.getElementById("log_pass").value=""
        return false    

    }

}


