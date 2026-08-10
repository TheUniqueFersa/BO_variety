#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randNum(int min, int max){
	return (rand() % (max - min + 1)) + min;
}

int main(int argc, char* argv[]){
	int max, min = 0, ranNumber;
	//Cuando no hay argumentos, regresa null
	srand(time(NULL));
	//if(argv[1] == NULL) printf("XDD"); //Proves NULL is the correct type identified
	
	if(argc <= 2){
		printf("%c\n", randNum(65, 71)); //65 and 71, ASCII respective codes for A -> G
	} else {
		min = atoi(argv[1]);
		max = atoi(argv[2]);
		ranNumber = randNum(min, max);
		printf("%d\n", ranNumber);

	}
	//printf("%d", ranNumber);
	return 0;
}
