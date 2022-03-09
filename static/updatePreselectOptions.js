function eeUpdateSelect(updateRecord) {
    // take updateRecord (object with key:val pairs), 
    // pre-select options in dropdowns for eePosition and eeStatus

    eePositionSelect = document.getElementById("eePosition")
    for (let i = 0; i < eePositionSelect.children.length; i++) {
        // console.log(eePositionSelect.children[i].innerText)
        if (eePositionSelect.children[i].innerText.toLowerCase() === updateRecord["eePosition"].toLowerCase()) {
            eePositionSelect.children[i].selected = true;
        };
    }
    eeStatusSelect = document.getElementById("eeStatus")
    for (let i = 0; i < eeStatusSelect.children.length; i++) {
        // console.log(eeStatusSelect.children[i].innerText)
        if (eeStatusSelect.children[i].innerText.toLowerCase() === "current" && updateRecord["eeStatus"].toString() == "1") {
            eeStatusSelect.children[i].selected = true;
        } else if (eeStatusSelect.children[i].innerText.toLowerCase() === "former" && updateRecord["eeStatus"].toString() == "2") {
            eeStatusSelect.children[i].selected = true
        };
    };

};

function itemUpdateSelect(updateRecord) {
    // take updateRecord (single value), pre-select options in dropdowns for itemType
    itemType = document.getElementById("itemType")
    for (let i = 0; i < itemType.children.length; i++) {
        console.log(itemType.children[i].innerText.toLowerCase(), updateRecord.toLowerCase())
        if (itemType.children[i].innerText.toLowerCase() === updateRecord.toLowerCase()) {
            itemType.children[i].selected = true;
        };
    };
};

function customerUpdateSelect(updateRecord) {
    // take updateRecord (single value), pre-select options in dropdowns for membershipStatus
    membershipStatus = document.getElementById("membershipStatus")
    for (let i = 0; i < membershipStatus.children.length; i++) {
        // console.log(membershipStatus.children[i].innerText.toLowerCase(), updateRecord.toLowerCase())
        if (membershipStatus.children[i].innerText.toLowerCase() === "yes" && updateRecord.toString() === "1") {
            membershipStatus.children[i].selected = true;
        } else if (membershipStatus.children[i].innerText.toLowerCase() === "no" && updateRecord.toString() === "0") {
            membershipStatus.children[i].selected = true;
        };
    };
};