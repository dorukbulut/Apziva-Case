let i = 0 ;
let placeholder = "";
const txt = "Search for a job role.(ex : mobile developer, full stack developer...)"

const speed = 50;

let type = () => {
    placeholder += txt.charAt(i);

    document.getElementById("two").setAttribute("placeholder", placeholder);
    i++;

    setTimeout(type, speed);
}


type();