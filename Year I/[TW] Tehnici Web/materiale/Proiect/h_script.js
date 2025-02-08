let q_counter = 0;
let score = 0;
const questionNumber = document.getElementById("question_number");
const questionText = document.getElementById("question_text");
const buttonsQuestions = document.getElementsByClassName("btn");
const nextButton = document.getElementById("next");
const backBtn = document.getElementById("backBtn");

const htmlquiz = {
    question1: {
        question: "Which tag is used to create an unordered list in HTML?",
        a1: ["<list>", false],
        a2: ["<ul>", true],
        a3: ["<ol>", false],
        a4: ["<li>", false]
    },
    question2: {
        question: "How do you specify that an image should be displayed without resizing in HTML?",
        a1: ['size="original"', false],
        a2: ['resize="none"', false],
        a3: ['scale="none"', false],
        a4: ['width="auto"', true]
    },
    question3: {
        question: "Which tag is used to create a section division in HTML?",
        a1: ['<div>', true],
        a2: ['<section>', false],
        a3: ['<split>', false],
        a4: ['<part>', false]
    },
    question4: {
        question: "How do you specify the text color in HTML using the color attribute?",
        a1: ['color="text-color"', false],
        a2: ['text-color="color"', false],
        a3: ['style="color: text-color;"', false],
        a4: ['font-color="color"', true]
    },
    question5: {
        question: "What is the correct tag to create a hyperlink in HTML?",
        a1: ['<link>', false],
        a2: ['<href>', false],
        a3: ['<a>', true],
        a4: ['<hyperlink>', false]
    },
    question6: {
        question: "What is the correct HTML tag for creating a line break?",
        a1: ['<lb>', false],
        a2: ['<break>', false],
        a3: ['<br>', true],
        a4: ['<line>', false]
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
    localStorage.setItem("h_score", score);

}


start();