#include <iostream>
#include <string>
#include <chrono>
#include <sstream>

using namespace std;
using namespace std::chrono;

int main() {
    // ============================
    // 1) Obtener la fecha actual
    // ============================
    // sys_days es una forma de representar fechas con precisión de días
    auto today = floor<days>(system_clock::now());  

    // ============================
    // 2) Leer la fecha ingresada
    // ============================
    string input;
    cout << "Ingrese la fecha (DD-MM-YYYY): ";
    cin >> input;

    // Extraer día, mes y año de la cadena
    int DD, MM, YYYY;
    char dash1, dash2;
    stringstream ss(input);
    ss >> DD >> dash1 >> MM >> dash2 >> YYYY;

    // Crear una fecha con year_month_day
    year_month_day ymd = year(YYYY) / month(MM) / day(DD);

    // Convertir a sys_days para poder hacer operaciones
    sys_days input_date = sys_days(ymd);

    // ============================
    // 3) Calcular diferencia
    // ============================
    auto diff = input_date - today; // duración en días
    auto total_days = diff.count(); // número de días entre hoy y la fecha ingresada

    if (total_days <= 0) {
        cout << "La fecha ingresada no es futura respecto a hoy.\n";
        return 0;
    }

    cout << "Días entre hoy y la fecha ingresada: " << total_days << "\n";

    // ============================
    // 4) Calcular los 4 puntos (cuartos de tiempo)
    // ============================
    // Primer cuarto, mitad, tres cuartos y la fecha final
    sys_days q1 = today + days(total_days / 4);
    sys_days q2 = today + days(total_days / 2);
    sys_days q3 = today + days((3 * total_days) / 4);
    sys_days q4 = input_date; // la fecha ingresada

    // ============================
    // 5) Mostrar resultados
    // ============================
    auto print_date = [](sys_days d) {
        year_month_day ymd = year_month_day(d);
        cout << static_cast<unsigned>(ymd.day()) << "/"
             << static_cast<unsigned>(ymd.month()) << "/"
             << int(ymd.year()) << "\n";
    };

    cout << "\nFechas de retorno:\n";
    cout << "1er cuarto: "; print_date(q1);
    cout << "Mitad:      "; print_date(q2);
    cout << "3er cuarto: "; print_date(q3);
    cout << "Final:      "; print_date(q4);

    return 0;
}
