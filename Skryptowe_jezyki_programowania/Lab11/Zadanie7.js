let liczba = 5;
let wartoscBinarna = "";
do {
    wartoscBinarna = (liczba % 2) + wartoscBinarna;
    liczba = Math.floor(liczba / 2);
} while (liczba > 0);
console.log("Wartość binarna: " + wartoscBinarna);
