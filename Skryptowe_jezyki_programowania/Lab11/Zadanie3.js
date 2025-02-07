// Tworzymy zmienną przechowującą napis
let tekst = "Turków. przez Podolskiego Kamieńca przejęcie i Oblężenie";

// Dzielimy ciąg na słowa
let slowa = tekst.split(' ');

// Odwracamy kolejność słów
let odwroconeSlowa = slowa.reverse();

// Łączymy słowa w odwróconej kolejności
let odwroconyTekst = odwroconeSlowa.join(' ');

// Wypisujemy tekst od tyłu w wyskakującym okienku
alert(odwroconyTekst);
