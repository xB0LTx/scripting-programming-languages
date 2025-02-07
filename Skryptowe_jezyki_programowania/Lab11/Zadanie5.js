let fibNMinusTwo = 0;
let fibNMinusOne = 1;
let piatyWyrazFibonacci;
for (let i = 2; i < 5; i++) {
    piatyWyrazFibonacci = fibNMinusTwo + fibNMinusOne;
    fibNMinusTwo = fibNMinusOne;
    fibNMinusOne = piatyWyrazFibonacci;
}
console.log("Piąty wyraz ciągu Fibonacciego:", piatyWyrazFibonacci);
