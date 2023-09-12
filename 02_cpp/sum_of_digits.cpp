#include <iostream>

int main() {
  int number, tmp, sum = 0;

  std::cout << "Enter a number: ";
  std::cin >> number;

  tmp = number;
  while (tmp > 0) {
    sum += tmp % 10;
    tmp /= 10;
  }

  std::cout << "Sum of digits in number " << number << " is " << sum
            << std::endl;
}
