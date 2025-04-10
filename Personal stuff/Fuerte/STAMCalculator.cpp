// First Version. 10/04/2025

#include <iostream>
#define endl '\n'

using namespace std;

float standardizePercent(float p){ //p: percentage
    return (p*6900)/600;
}

float calcSTAM(float t, float sp){ //t: time, sp: standard percentage
    return (t+sp)/2;
}


int main(){
    float percentage, timeMin;
    cout << "Hi there! Give me the values and I'll do the rest :)" << endl;
    cout << "Time in minutes: " << endl;

    cin >> timeMin;

    cout << "Perfect, now the percentage please: " << endl;

    cin >> percentage;

    cout << "Awesome, I'm doing the magic..." << endl;


    float STAM = calcSTAM(timeMin, standardizePercent(percentage));

    cout << "Your STAM is: " << STAM << endl;

    return 0;
}