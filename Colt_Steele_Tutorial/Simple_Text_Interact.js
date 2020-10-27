document.querySelector("button").addEventListener("click", function(){
    document.body.style.background = randColor();
})

function randColor(){
    return '#' + (function co(lor){
return (lor +=
    [0,,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'][Math.floor(Math.randon()*16)]) && (lor.length == 6) ?  lor : co(lor);
    })('');
}