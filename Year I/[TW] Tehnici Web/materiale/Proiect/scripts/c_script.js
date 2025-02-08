let q_counter = 0;
let score = 0;
const questionNumber = document.getElementById("question_number");
const questionText = document.getElementById("question_text");
const buttonsQuestions = document.getElementsByClassName("btn");
const nextButton = document.getElementById("next");
const backBtn = document.getElementById("backBtn");

const htmlquiz = {
    question1: {
        question: "Which CSS property is used to set the background color of an element?",
        a1: ["bg-color", false],
        a2: ["background-color", true],
        a3: ["color-background", false],
        a4: ["background-style", false]
    },
    question2: {
        question: "Which property is used to change the color of text in CSS?",
        a1: ['text-color', false],
        a2: ['color', true],
        a3: ['font-color', false],
        a4: ['text-style', false]
    },
    question3: {
        question: "Which CSS property is used to set the font size of text?",
        a1: ['font-size', true],
        a2: ['text-size', false],
        a3: ['size-font', false],
        a4: ['font-style', false]
    },
    question4: {
        question: "Which property is used to align text to the center horizontally in CSS?",
        a1: ['text-align: center', true],
        a2: ['align: center', false],
        a3: ['center-text: horizontal', false],
        a4: ['text-align: middle', false]
    },
    question5: {
        question: "Which CSS property is used to add a border around an element?",
        a1: ['border-style', false],
        a2: ['border', true],
        a3: ['element-border', false],
        a4: ['style-border', false]
    },
    question6: {
        question: "What CSS property is used to make text bold?",
        a1: ['font-weight: bold', true],
        a2: ['bold-text: true', false],
        a3: ['text-style: bold', false],
        a4: ['font-bold: yes', false]
    }
}


function check(q){
    nextButton.style.display = "block";
    let correct;

    for(let i=1; i<=4; i++){
        if(htmlquiz["question"+(q_counter+1)]["a"+i][1] === true)
            correct = i;

        const correctBtn = document.getElementById("b"+i);
        correctBtn.disabled = true;
    }


    const correctBtn = document.getElementById("b" + correct);
    correctBtn.style.backgroundColor = "#32a85a";
    

    if(htmlquiz["question"+(q_counter+1)]["a"+q][1] === false){
        const currentBtn = document.getElementById("b" + q);
        currentBtn.style.backgroundColor = "#d62b2b";
    }
    else
        score += 1;
}

function start(){
    
    questionNumber.textContent = "#1"
    questionText.innerHTML = htmlquiz["question"+(q_counter+1)]["question"];
    for(let i = 0; i < buttonsQuestions.length; i++){
        buttonsQuestions[i].textContent = 
        htmlquiz["question"+(q_counter+1)]["a"+(i+1)][0];
        buttonsQuestions[i].style.backgroundColor = "white";
    }

}

function next(){
    q_counter += 1;
    if(q_counter == 6)
        final_screen();
    else
        resetNext();
}

function resetNext(){
    nextButton.style.display = "none";
    questionNumber.textContent = "#" + (q_counter+1);
    questionText.innerHTML = htmlquiz["question"+(q_counter+1)]["question"];
    for(let i = 0; i < buttonsQuestions.length; i++){
        buttonsQuestions[i].textContent = 
        htmlquiz["question"+(q_counter+1)]["a"+(i+1)][0];
        buttonsQuestions[i].style.backgroundColor = "white";
        buttonsQuestions[i].disabled = false;
    }
    

}

function final_screen(){
    for(let i = 0; i < buttonsQuestions.length; i++)
        buttonsQuestions[i].style.display = "none";

    nextButton.style.display = "none";
    questionNumber.textContent = "";
    questionText.textContent = `Your Score: ${score}/6`;
    backBtn.style.display = "block";

    localStorage.setItem("c_score", score);
    
}

var x = document.querySelector("#b1");
x.addEventListener('click', function(){check(1);});

var x = document.querySelector("#b2");
x.addEventListener('click', function(){check(2);});

var x = document.querySelector("#b3");
x.addEventListener('click', function(){check(3);});

var x = document.querySelector("#b4");
x.addEventListener('click', function(){check(4);});

var nxt = document.querySelector("#next");
nxt.addEventListener('click', next);

start();