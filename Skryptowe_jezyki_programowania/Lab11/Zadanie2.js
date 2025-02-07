let tekst = "\"Pan Wołodyjowski\" przedstawia losy pana Michała – najlepszej szabli Rzeczpospolitej";
console.log("Długość tekstu:", tekst.length);
let indeksSzabli = tekst.indexOf("szabli");
console.log("Indeks pierwszego wystąpienia 'szabli':", indeksSzabli);
let zmienionyTekst = tekst.replace("najlepszej", "pierwszej");
console.log("Zmieniony tekst:", zmienionyTekst);
