window.addEventListener("load", function ()
{
    // Get click element referances.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // Counter value.
    let counter = 0;

    //Click button function.
    let clickButtonFunction = function ()
    {
        //increment counter.
        counter++;
        //update counter value 
        clickCounterElement.innerHTML = counter;
    };


    // Attach button function.
    clickButtonElement.addEventListener("click",clickButtonFunction);
});