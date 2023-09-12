const search_guests = document.getElementById("number-guests");
function stepper(btn){
    let id = btn.getAttribute("id");
    let min = search_guests.getAttribute("min");
    let max = search_guests.getAttribute("max");
    let step = search_guests.getAttribute("step");
    let val = search_guests.getAttribute("value");
    let calcStep = (id == "increment") ? (step*1) : (step * -1);
    let newValue = parseInt(val) + calcStep;

    if(newValue >= min && newValue <=max ){
        search_guests.setAttribute("value", newValue);
    }
}