#include <bitset>
#include <iostream>

int main() {
  int number;

  std::cout << "Enter a decimal number: ";
  std::cin >> number;

  std::cout << "The binary representation of " << number << " is ";

  // convert number into bits
  std::bitset<8> bs(number);
  std::cout << bs << '\n' << std::endl;

  std::string bits;
  std::cout << "Enter a binary unsigned number of 8 bits: ";
  std::cin >> bits;

  std::cout << "The decimal representation of " << bits << " is ";

  // convert bits string into bitset
  std::bitset<8> bs2(bits);
  // convert and print bitset into unsigned long
  std::cout << bs2.to_ulong() << std::endl;

  return 0;
}
