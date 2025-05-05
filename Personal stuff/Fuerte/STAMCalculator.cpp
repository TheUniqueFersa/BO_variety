// First Version. 10/04/2025

#include <iostream>
#define endl '\n'

using namespace std;

float standardizePercent(float p){ //p: percentage
    return (p*6900)/600;
}
float standardizeTicks(int ticks){
    return ((float)ticks*6900)/21;
}

float calcSTAM(float sticks, float sp, float t){ //sticks}: standard ticks, sp: standard percentage, t: time
    return (sticks+t+sp)/3;
}

float standardize(float val, float v100){
    return (val*100)/v100;
}

int main(){
    float percentage, timeMin;
    int ticks;
    cout << "Hi there! Give me the values and I'll do the rest :)" << endl;
    cout << "Time in minutes: " << endl;

    cin >> timeMin;

    cout << "Perfect, now the percentage please: " << endl;

    cin >> percentage;

    cout << "Cool, now give me the ticks, please: " << endl;

    cin >> ticks;

    cout << "Awesome, I'm doing the magic..." << endl;

    float STAM = calcSTAM(standardizeTicks(ticks), standardizePercent(percentage), timeMin);

    cout << "Your STAM is: " << STAM << endl;
    cout << "Your STAM in percentage is: " << standardize(STAM, 6900) << endl;

    return 0;
}