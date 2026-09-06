#include <iostream>
#define endl '\n'
#define V_100_T 1020
#define V_100_P 100
#define V_100_G 6
#define UTIL_WEEK 7


using namespace std;

float standardizePercent(float p){ //p: percentage
    return (p*6900)/600;
}
float standardizeTicks(int ticks){
    return ((float)ticks*6900)/21;
}


// ----
//standardize
float stand(float val, float v100){
    return (val*100)/v100;
}

float prom(float p, float q){
    return p/q;
}
// TODO: change to list so it can actually sum the values in p
float calcSTAM(float p_x, float p_g, float p_t){ //sticks}: standard ticks, sp: standard percentage, t: time
    return prom(p_x+p_g+p_t, 3);
}




int main(){
    
    
    float x, x_0; //x: XCH achieved, x_0: XCH stablished
    float t; //t: encap time
    float g; //g: gamma (TTT)
    float p_x, p_t, p_g; //p: porcentage
    cout << "Hi there! Give me the values and I'll do the rest :)" << endl;
    cout << "x and x_0 please: " << endl;

    cin >> x >> x_0;
    
    cout << "Time in minutes: " << endl;

    cin >> t;
    
    cout << "Cool, now give me the TTT, please: " << endl;

    cin >> g;

    cout << "Awesome, I'm doing the magic..." << endl;

    //For a certain day
    p_x = stand(x, x_0);
    p_t = stand(t, V_100_T);
    p_g = stand(g, V_100_G);
    float STAM = calcSTAM(p_x, p_t, p_g);

    cout << "Your STAM is: " << STAM << endl;
    cout << "Your ENV is: " << 100 - STAM << endl;
    return 0;
}