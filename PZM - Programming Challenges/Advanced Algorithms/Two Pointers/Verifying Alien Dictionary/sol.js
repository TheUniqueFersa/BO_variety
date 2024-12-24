var isAlienSorted = function (palabras, orden) {
	// Crear mapa del diccionario alienigena
	mapa_diccionario = new Map();
	for (let i = 0; i < orden.length; i++) {
		mapa_diccionario[orden[i]] = i;
	}

	// Revisar el orden de las palabras
	for (let i = 1; i < palabras.length; i++) { // T = 0(n)   S = 0(m)
		if (comparar(palabras[i - 1], palabras[i]) === false) {
			return false;
		}
	}
    return true;
};

// O(longitud de la palabra mÃ¡s larga)
var comparar = function (palabra1, palabra2) {
	const longitud = Math.min(palabra1.length, palabra2.length);
	for (let i = 0; i < longitud; i++) {
		if (mapa_diccionario[palabra1[i]] < mapa_diccionario[palabra2[i]]) {
			return true;
		}
		if (mapa_diccionario[palabra1[i]] > mapa_diccionario[palabra2[i]]) {
			return false;
		}
	}
	return palabra1.length <= palabra2.length;
};

/*
Ejemplos:
words = {"conocer", "cono"};
alien_alphabet = "abcdefhgijklmnopqrstuvwxyz";

isAlienSorted(["conocer", "cono"], "abcdefhgijklmnopqrstuvwxyz") 
*/