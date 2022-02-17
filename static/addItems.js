function addFields(numberOfItems=1){

    // itemsContainer where item lines will be dynamically generated
    let itemsContainer = document.getElementById("itemsContainer");

    // Determine number of existing rows for naming subsequent rows 
    let itemNum = itemsContainer.getElementsByClassName('form-row').length
    console.log(itemNum)

    // Find any previous form submit button and remove 
    if (document.getElementById('submitButton') !== null){
        submitButton = document.getElementById('submitButton')
        submitButton.remove();
        submitButton = document.getElementById('awesomeBreak');
        submitButton.remove();
        }

    // Create row label 
    //let rowLabel = document.createElement("p")
    //rowLabel.innerText = "Item " + (itemNum+1);
    //rowLabel.style = "font-weight: bolder";
    //itemsContainer.appendChild(rowLabel);

    // Create div for form row 
    let itemRow = document.createElement("div")
    itemRow.className = "form-row";

    // Create div for form col 1
    let rowCol1 = document.createElement("div")
    rowCol1.className = "col-2";

    // Create input for itemId field
    let itemId = document.createElement("input");
    itemId.type = "text";
    itemId.className = "form-control";
    itemId.name = "itemId" + (itemNum+1);
    itemId.placeholder = "Item ID"
    itemId.required = true;

    // Add itemId to rowCol1 and rowCol1 to itemRow
    rowCol1.appendChild(itemId);
    itemRow.appendChild(rowCol1)

    // Create div for form col 1
    let rowCol2 = document.createElement("div");
    rowCol2.className = "col-3";

    // Create input for itemQuantity field
    let itemQuantity = document.createElement("input");
    itemQuantity.type = "number";
    itemQuantity.min = 1;
    itemQuantity.className = "form-control";
    itemQuantity.name = "itemQuantity" + (itemNum+1);
    itemQuantity.placeholder = "Quantity";
    itemQuantity.required = true;

    // Add itemQuantity to rowCol2 and rowCol2 to itemRow
    rowCol2.appendChild(itemQuantity);
    itemRow.appendChild(rowCol2)

    // Then, add itemRow to itemsContainer
    itemsContainer.appendChild(itemRow);

    
    // Add break at the bottom 
    let containerBreak = document.createElement("br");
    containerBreak.id = "awesomeBreak"
    document.getElementById("itemsContainer").appendChild(containerBreak);


    // Add the submit button to the bottom again 
    let link = document.createElement("button");
    link.href = "/{{dbEntity}}/{{operation}}";
    link.type = "submit";
    link.id = "submitButton"
    link.className = "btn btn-outline-primary";
    link.innerText = "Complete Purchase";
    document.getElementById("itemsContainer").appendChild(link);
    //itemsContainer.appendChild(document.createElement("br"));

};