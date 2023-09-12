#include <iomanip>
#include <iostream>

using namespace std;

const string line = string(8, '-');

/**
 * @brief Prints a horizontal table border
 */
void draw_line() { cout << "+" << line << "+" << line << "+" << endl; }

int main() {
  draw_line();
  // print the table header
  cout << "|  Char  |  ASCII |" << endl;
  draw_line();

  for (int i = 0; i <= 255; i++) {
    // check if character is printable and convert it into a string
    // otherwise use empty string
    string c = isprint(i) ? string(1, static_cast<int>(i)) : "";
    cout << "|" << setw(7) << c << " |";
    // print the ASCII code
    cout << setw(7) << i << " |" << endl;
  }

  draw_line();
  return 0;
}
