#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
	//estableciendo la semilla, ahora dependen del tiempo,
	//lo que hace que en cada ejecucion sean distintos
	//En cambio si se quita, se generan siempre los mismos numeros
	srand(time(NULL));
	int num, min=1, max=10, n = 10;
	for(int i = 0; i<n; i++){
		num = (rand() % (max - min + 1)) + min;
		printf("%d ", num);
	}
	printf("\n");
	return 0;
}
