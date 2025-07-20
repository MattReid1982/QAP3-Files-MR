// Desc: Mo Lawn Care
// Author: Matt Reid
// Dates: July 14th, 2025


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const BORDER_PERCENTAGE = 0.04;
const BORDER_RATE = 0.35;  // Per square foot.
const MOWING_PERCENTAGE = 0.95;
const MOWING_RATE = 0.07;  // Per square foot.
const FERTILIZER_RATE = 0.05;  // Per square foot of total area.
const HST_RATE = 0.15; // 15%
const ENV_TAX_RATE = 0.014; // 1.4% of the total charges

// Start main program here.
let custName = prompt("Enter the customer's name: ").toUpperCase();
let strAdd = prompt("Enter the customer's street address: ");
let city = prompt("Enter the customer's city: ");
let phoneNum = prompt("Enter the customer's phone number (555-555-5555): ");
let totalSqrfeet = parseInt(prompt("Enter the total number of square footage (######): "));

// Here is where the calculations start.
if (isNaN(totalSqrfeet) || totalSqrfeet <= 0){
  alert("Invalid square footage entered.")
}else{
let borderCost = totalSqrfeet * BORDER_PERCENTAGE * BORDER_RATE;
let mowingCost = totalSqrfeet * MOWING_PERCENTAGE * MOWING_RATE;
let fertCost = totalSqrfeet * FERTILIZER_RATE;

let totalCharges = borderCost + mowingCost + fertCost;
let salesTax = totalCharges * HST_RATE;
let enviroTax = totalCharges * ENV_TAX_RATE;
let invoiceTotal = totalCharges + salesTax + enviroTax;

//Create table with information provided.

// Display results in a table.
document.writeln("<br />");
document.writeln("<table class='Motable'>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2' class='tophead'><strong>Mo's Lawncare Services - Customer Invoice</strong></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2'>");
document.writeln(
  "<br /> Customer Information: <br />" + "<br />"
  + "&nbsp;&nbsp;&nbsp;&nbsp;" + (custName) + "<br />" + "&nbsp;&nbsp;&nbsp;&nbsp;" + (strAdd) + "<br />" + "&nbsp;&nbsp;&nbsp;&nbsp;" + (city) + "&nbsp;" + (phoneNum),"<br /><br />");

document.writeln("Property Size [in sq ft]: " + totalSqrfeet + "<br />");
document.writeln("<br />");

document.writeln("</td>");

document.writeln("<tr>");
document.writeln("<td>Border cost:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(borderCost) + "</td>"
);

document.writeln("<tr>");
document.writeln("<td>Mowing cost:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(mowingCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(fertCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'>" + "<br />" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total charges:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(totalCharges) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'>" + "<br />" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>SalesTax:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(salesTax) + "</td>"
);
document.writeln("<tr>");
document.writeln("<td>Environmental Tax:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(enviroTax) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'>" + "<br />" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice total:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(invoiceTotal) + "</td>"
);
document.writeln("<tr>");
document.writeln(
  "<td colspan='2' class='bottomfoot'><strong>Turning Lawns into Landscapes</strong></td>"
);
document.writeln("</tr>");

}