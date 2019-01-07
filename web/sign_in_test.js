function check_id_pw() {

    var uid = get_id("uid"),
        upw = get_id("upw") ;
    
    var okmsg = document.getElementById("signinok")
        ,failmsg = document.getElementById("singinfail")
        ,signinform = document.getElementById("form")
        ,okmsgadd = document.getElementById("addmsg")
        ,wmpic = document.getElementById("watermelon") ;

    var msg = uid + "님 반갑습니다!";
    
    document.getElementById("addmsg").innerHTML = msg;
    
    if (uid === 'a' && upw === '1') {
        okmsg.style.display = 'block';
        signinform.style.display = 'none';
        okmsgadd.style.display = 'block' ;
        wmpic.style.display = 'block' ;
    } 
    else { 
        failmsg.style.display = 'block';
    }

    return false;
}

function get_id(id) {
    return document.getElementById(id).value;
}