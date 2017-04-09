function checkDate(day, month) {

    var isValid = "";

   if ((month == 4 || month == 6 || month == 9 || month == 11) && day < 30) {
       return true;
   }
   else if (month == 2 && day <= 28) {
       return true;
   }
   else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day <= 31) {
       return true;
   }
   else {
       return false;
   }
};

$(document).ready(function() {

    $(".slideDiv").show("drop", {direction: "up"}, 300, function() {

        $(".slideDiv2").show("drop", {direction: "up"}, 200);
    });

});

$(".check-date").click(function(e) {

    var day = parseInt($("#sel1").val());
    var month = parseInt($("#sel2").val());

    if (checkDate(day,month) == true) {
        console.log("Date is valid!");
    } else {
        alert("Date is in-valid!");
        e.preventDefault();
    }
});




