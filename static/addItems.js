function addFieldsHelper(itemIdVal = null, itemQuantityVal = null, inventoryItems = null) {
    /*  itemIdVal: corresponds to Item.itemId for existing PurchaseItem
    *   itemQuantityVal: corresponds to Item.itemId for existing PurchaseItem
    *   inventoryItems: itemId values to pre-fill form with data
    */

    // itemsContainer where item lines will be dynamically generated
    let itemsContainer = document.getElementById("itemsContainer");

    // Determine number of existing rows for naming subsequent rows 
    let itemNum = itemsContainer.getElementsByClassName('form-row').length

    // If previous itemId select was not filled, do nothing and display prompt:
    if (itemNum > 0) {
        let pvsItemIdVal = document.getElementById('itemId' + (itemNum).toString())
        if (pvsItemIdVal.value === "") {
            alert("Select Item ID and Quantity prior to adding row")
            return
        };
    };

    // Find any previous form submit button and remove 
    if (document.getElementById('submitButton') !== null) {
        submitButton = document.getElementById('submitButton')
        submitButton.remove();
        submitButton = document.getElementById('awesomeBreak');
        submitButton.remove();
    };

    // Create row label 
    let rowLabel = document.createElement("p")
    rowLabel.innerText = "Item " + (itemNum + 1);
    rowLabel.style = "font-weight: bolder";
    itemsContainer.appendChild(rowLabel);

    // Create div for form row 
    let itemRow = document.createElement("div")
    itemRow.className = "form-row";

    // Create div for form col 1
    let rowCol1 = document.createElement("div")
    rowCol1.className = "col-2";

    // Create select dropdown for itemId field pre-populated with items in inventory
    let itemId = document.createElement("select");
    itemId.className = "form-control";
    itemId.name = "itemId" + (itemNum + 1);
    itemId.id = "itemId" + (itemNum + 1);
    itemId.required = true;
    // On creation of new PurchaseItems, a placeholder value for the select 'Item ID'
    if (itemIdVal === null) {
        let itemOption = document.createElement("option");
        itemOption.className = "form-control";
        itemOption.innerText = 'Item ID';
        itemOption.value = "";
        itemOption.disabled = true;
        itemOption.selected = true;
        itemId.appendChild(itemOption)
    };
    // On update of existing PurchaseItems, there is ONLY ONE pre-selected option
    if (itemIdVal !== null) {
        // Set the exisintg value of the select to the itemIdVal
        itemId.value = itemIdVal;
        // Declare other options 
        let existingItem = document.createElement("option");
        existingItem.className = "form-control";
        existingItem.innerText = itemIdVal;
        existingItem.selected = true;
        itemId.appendChild(existingItem)
    };
    // On create / update beyond existing items, dropdown has MULTIPLE options 
    if (itemIdVal === null) {
        // Iterate through inventoryItems, create additional options within select
        for (j = 0; j < Object.keys(inventoryItems).length; j++) { // j bc i is used elsewhere 
            let itemOption = document.createElement("option");
            itemOption.className = "form-control";
            itemOption.innerText = Object.keys(inventoryItems)[j];

            // Beyond first item row, deactivate any previously selected itemId from options
            if (itemNum > 0) {
                let pvsItemIdVals = []
                // Iterate through all previous selects by itemId
                for (k = 0; k < itemNum; k++) {
                    let pvsItemIdVal = document.getElementById('itemId' + (k + 1).toString())
                    if (pvsItemIdVal !== "") {
                        pvsItemIdVals.push(pvsItemIdVal.value)
                    };
                };
                // Check if the item has been previously selected
                if (pvsItemIdVals.includes(itemOption.innerText)) {
                    itemOption.disabled = true;
                };
            };
            itemId.appendChild(itemOption);
        };
    };
    // Add itemId to rowCol1 and rowCol1 to itemRow
    rowCol1.appendChild(itemId);
    itemRow.appendChild(rowCol1)

    // Create div for form col 2
    let rowCol2 = document.createElement("div");
    rowCol2.className = "col-3";

    // Create input for itemQuantity field
    let itemQuantity = document.createElement("input");
    itemQuantity.type = "number";
    itemQuantity.min = 0;
    // For newly added PurchaseItems, cannot add to quantity before an itemId chosen
    if (itemIdVal === null){
        itemQuantity.max = 0;
    };
    itemQuantity.className = "form-control";
    itemQuantity.name = "itemQuantity" + (itemNum + 1);
    if (itemQuantityVal === null) {
        itemQuantity.placeholder = "Quantity";
        // TO DO: Cannot have a 0 item quantity on create
        // itemQuantity.min = 0;
    } else {
        itemQuantity.value = itemQuantityVal;
        // Set existing item quantity max to the max amount in inventory 
        // 220308 BUG FIX: On update there was bug that wouldn't allow existing value to exceed current inventory
        // ...fix by making it itemQuantityVal + Item.inventoryOnHand 
        itemQuantity.max = inventoryItems[itemId.value] + itemQuantityVal;
    };
    itemQuantity.required = true;

    // Modify the parent itemId select and each itemQuantity field so itemId 
    // option chosen will set max on itemQuantity according to inventoryOnHand 
    // for that itemId
    itemId.addEventListener("change", function () {
        if (itemId.value !== "") {
            // let inventoryOnHand = inventoryItems[this.value];
            itemQuantity.max = inventoryItems[this.value];
        };
    });

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
    } else {
        completePurchaseButton.innerText = "Complete Purchase";
    };
    document.getElementById("itemsContainer").appendChild(completePurchaseButton);

};
// LEFT OFF HERE
function addFields(existingItems = 0, inventoryItems = null) {
    /*  add PurchaseItem fields during Create or Update of a Purchase 
    *   existingItems: either array of [itemId, itemQuantity] for existing PurchaseItems or 0 
    *   inventoryItems: itemId values to pre-fill form with data
    */

    // Create & Update - New blank row w/ dropdown for items in inventory 
    if (existingItems === 0) {
        addFieldsHelper(null, null, inventoryItems);

        // Update - Rows with existing items from pruchase during update purchase + items from inventory
    } else {
        for (i = 0; i < existingItems.length; i++) {
            addFieldsHelper(existingItems[i]['itemId'], existingItems[i]['itemQuantity'], inventoryItems);
        };
    };
};
