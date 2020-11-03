alert("One of these things is not like the other. One of these things does not beWONG!");

var pics = [
    "imgs/Wong1.jpeg",
    "imgs/Wong2.jpeg",
    "imgs/Wong3.jpeg",
    "imgs/Wong4.jpeg",
    "imgs/Wong5.jpeg",
    "imgs/Wong6.jpeg",
    "imgs/Wong7.jpeg",
    "imgs/Wong8.jpeg",
    "imgs/POG.jpeg"
];

var button = document.querySelector("button");
var img = document.querySelector("img");
var counter = 0;
button.addEventListener("click", function(){
    if(counter === 9){
        counter = 0;
    }
    img.src = pics[counter];
    counter = counter + 1;
});
