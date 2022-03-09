function eeUpdateSelect(updateRecord){
    eePositionSelect = document.getElementById("eePosition")
    for (let i=0; i < eePositionSelect.children.length; i++){
        // console.log(eePositionSelect.children[i].innerText)
        if (eePositionSelect.children[i].innerText.toLowerCase() === updateRecord["eePosition"].toLowerCase()){
            eePositionSelect.children[i].selected = true; 
        };
    }
    eeStatusSelect = document.getElementById("eeStatus")
    for (let i=0; i < eeStatusSelect.children.length; i++){
        // console.log(eeStatusSelect.children[i].innerText)
        if (eeStatusSelect.children[i].innerText.toLowerCase() === "current" && updateRecord["eeStatus"].toString() == "1"){
            eeStatusSelect.children[i].selected = true; 
            // console.log("BINGO CURRENT")
        } else if (eeStatusSelect.children[i].innerText.toLowerCase() === "former" && updateRecord["eeStatus"].toString() == "2"){
            eeStatusSelect.children[i].selected = true
        };
    }
    
};