

const statusH = document.getElementById("clickToStartH");
const statusC = document.getElementById("clickToStartC");
const statusJS = document.getElementById("clickToStartJ");

const svgJ = document.getElementById("svgJ");
const perTxtJ = document.getElementById("perTxtJ");
const svgC = document.getElementById("svgC");
const perTxtC = document.getElementById("perTxtC");
const svgH = document.getElementById("svgH");
const perTxtH = document.getElementById("perTxtH");

function checkScore(){
    let aux = localStorage.getItem("j_score");
    let calcul=0;
    
    if(aux != -1){
        statusJS.textContent = `Your Score: ${aux}/6`;
        calcul = Math.floor(100*aux/6);
        svgJ.style.strokeDasharray = calcul+", 100";
        perTxtJ.textContent = calcul+"%";
    }

    aux = localStorage.getItem("h_score");
    if(aux != -1){
        statusH.textContent = `Your Score: ${aux}/6`;
        calcul = Math.floor(100*aux/6);
        svgH.style.strokeDasharray = calcul+", 100";
        perTxtH.textContent = calcul+"%";
    }

    aux = localStorage.getItem("c_score");
    if(aux != -1){
        statusC.textContent = `Your Score: ${aux}/6`;
        calcul = Math.floor(100*aux/6);
        svgC.style.strokeDasharray = calcul+", 100";
        perTxtC.textContent = calcul+"%";
    }
        
}
function resetScore(){
    localStorage.setItem("j_score", -1);
    localStorage.setItem("c_score", -1);
    localStorage.setItem("h_score", -1);

    statusJS.textContent = "Click to START";
    statusC.textContent = "Click to START";
    statusH.textContent = "Click to START";
    svgJ.style.strokeDasharray = "0,100";
    perTxtJ.textContent = "0%";
    svgC.style.strokeDasharray = "0,100";
    perTxtC.textContent = "0%";
    svgH.style.strokeDasharray = "0,100";
    perTxtH.textContent = "0%";
}

const submit_input = document.getElementById("submit_input");
function submitScore(){
    
}

checkScore();

