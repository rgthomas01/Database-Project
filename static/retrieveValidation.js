function retrieveValidation (dbEntity){
    
    if (dbEntity == "employees"){
         
        //grab input variables
        let eeId = retrieveForm.eeId.value
        let eeFirstName = retrieveForm.eeFirstName.value
        let eeLastName = retrieveForm.eeLastName.value
        let eeStatus =retrieveForm.eeStatus.value

        //check if empty search params 
        if (eeId ==""
            && eeFirstName ==""
            && eeLastName == ""
            && eeStatus == ""
            ){alert("Must use at least 1 search criteria")}
        }
    if (dbEntity == "customers"){ 
        
        let customerId = retrieveForm.customerId.value
        let customerFirstName = retrieveForm.customerFirstName.value
        let customerLastName = retrieveForm.customerLastName.value
        let customerEmail =retrieveForm.customerEmail.value

        //check if empty search params 
        if (customerId ==""
            && customerFirstName ==""
            && customerLastName == ""
            && customerEmail == ""
            ){alert("Must use at least 1 search criteria")}

    }
    if (dbEntity == "purchases"){ 
        
        let purchaseId = retrieveForm.purchaseId.value
        let customerId = retrieveForm.customerId.value
        let eeId = retrieveForm.eeId.value

        //check if empty search params 
        if (purchaseId ==""
            && customerId ==""
            && eeId == ""
            && purchaseDate == ""
            ){alert("Must use at least 1 search criteria")}
    }
    if (dbEntity == "items"){ 
        
        let itemId = retrieveForm.itemId.value
        let itemName = retrieveForm.itemName.value
        let itemPrice = retrieveForm.itemPrice.value
        let itemType = retrieveForm.itemType.value


        //check if empty search params 
        if (itemId ==""
            && itemName ==""
            && itemPrice == ""
            && itemType == ""

            ){alert("Must use at least 1 search criteria")}
    }
    }