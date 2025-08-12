#include <iostream>
#include <chrono>
#include <format>  // C++20
using namespace std;
using namespace std::chrono;

int main() {
    // Obtener fecha y hora actual
    //std::chrono::time_point<std::chrono::system_clock>
    auto ahora = system_clock::now();

    // Convertir a tiempo calendario
    time_t t = system_clock::to_time_t(ahora);
    cout << "Fecha y hora actual: " << ctime(&t);

    // Agregar 3 días
    auto tres_dias_despues = ahora + hours(24 * 3);
    time_t t2 = system_clock::to_time_t(tres_dias_despues);
    cout << "Dentro de 3 días: " << ctime(&t2);

    // Si tienes C++20, formateo elegante
    // std::cout << std::format("{:%Y-%m-%d %H:%M:%S}\n", floor<seconds>(ahora));
    return 0;
}
