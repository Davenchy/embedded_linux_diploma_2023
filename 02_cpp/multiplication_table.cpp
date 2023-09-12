#include <iomanip>
#include <iostream>

int main() {
  for (int i = 1; i <= 10; i++) {
    for (int j = 1; j <= 10; j++) {
      std::cout << std::right << std::setw(4) << (i * j);
    }
    std::cout << std::endl;
  }

  return 0;
}
