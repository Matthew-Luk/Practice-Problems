var email = document.getElementById("email-input")
var card = document.getElementById("card")
var success = document.getElementById("success")

function validateEmail(){
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)){
        console.log("worked")
        if (card.style.display !== "none"){
            card.style.display = "none";
            success.style.display = "flex";
        }else{
            card.style.display = "flex";
            success.style.display = "none";
        }
        return(true)
    }else{
        console.log("failed")
        document.getElementById("email-input").classList.add("error-input")
        document.getElementById("error-message").innerText = "Valid email required"
        return(false)
    }
}

function dismiss(){
    var temp = ""
    if (success.style.display !== "none"){
        card.style.display = "flex";
        success.style.display = "none";
        email.innerHTML = temp;
    }else{
        card.style.display = "none";
        success.style.display = "flex";
        email.innerHTML = temp;
    }
}