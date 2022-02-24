function addFieldsHelper(itemIdVal=null, itemQuantityVal=null){

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
    let rowLabel = document.createElement("p")
    rowLabel.innerText = "Item " + (itemNum+1);
    rowLabel.style = "font-weight: bolder";
    itemsContainer.appendChild(rowLabel);

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
    if (itemIdVal === null){
        itemId.placeholder = "Item ID";
    } else {
        itemId.value = itemIdVal;
    }
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
    itemQuantity.min = 0;
    itemQuantity.className = "form-control";
    itemQuantity.name = "itemQuantity" + (itemNum+1);
    if (itemQuantityVal === null){
        itemQuantity.placeholder = "Quantity";
    } else {
        itemQuantity.value = itemQuantityVal;
    }

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

    // Add the complete purchase button to the bottom 
    let completePurchaseButton = document.createElement("button");
    completePurchaseButton.href = "/{{dbEntity}}/{{operation}}";
    completePurchaseButton.type = "submit";
    completePurchaseButton.id = "submitButton"
    completePurchaseButton.className = "btn btn-outline-primary";
    // On update make the button reference update
    if (itemIdVal !== null) {
        completePurchaseButton.innerText = "Complete Purchase Update";
    }else {
        completePurchaseButton.innerText = "Complete Purchase";
    };
    document.getElementById("itemsContainer").appendChild(completePurchaseButton);

};

function addFields(existingItems=0){
    console.log(existingItems)
    // Add new blank row during create & update purchase
    if (existingItems===0) {
        addFieldsHelper();
    // Adds existing items during update purchase
    } else {
        for (i = 0; i<existingItems.length; i++) {
            addFieldsHelper(existingItems[i]['itemId'],existingItems[i]['itemQuantity']);
         };
        let editExisting = document.getElementById("editExistingDiv");
        console.log(editExisting);
        editExisting.remove()
    };     
};