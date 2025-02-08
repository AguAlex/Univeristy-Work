let q_counter = 0;
let score = 0;
const questionNumber = document.getElementById("question_number");
const questionText = document.getElementById("question_text");
const buttonsQuestions = document.getElementsByClassName("btn");
const nextButton = document.getElementById("next");
const backBtn = document.getElementById("backBtn");

const htmlquiz = {
    question1: {
        question: "Which keyword is used to declare variables in JavaScript?",
        a1: ["var", true],
        a2: ["variable", false],
        a3: ["v", false],
        a4: ["int", false]
    },
    question2: {
        question: "How do you declare a constant variable in JavaScript?",
        a1: ['let', false],
        a2: ['var', false],
        a3: ['const', true],
        a4: ['constant', false]
    },
    question3: {
        question: "Which keyword is used to define a function in JavaScript?",
        a1: ['func', false],
        a2: ['function', true],
        a3: ['def', false],
        a4: ['fn', false]
    },
    question4: {
        question: "What method is used to find the length of an array in JavaScript?",
        a1: ['length()', true],
        a2: ['count()', false],
        a3: ['size()', false],
        a4: ['len()', false]
    },
    question5: {
        question: "Which operator is used to concatenate strings in JavaScript?",
        a1: ['+', true],
        a2: ['*', false],
        a3: ['/', false],
        a4: ['-', false]
    },
    question6: {
        question: "Which function is used to print content to the console in JavaScript?",
        a1: ['print()', false],
        a2: ['display()', false],
        a3: ['console.log()', true],
        a4: ['out()', false]
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

    localStorage.setItem("j_score", score);
    
}

function setScore(){
    const newScore = document.getElementById("currentScoreJS");
    newScore.textContent = sessionStorage.getItem("scorJS");
}


start();