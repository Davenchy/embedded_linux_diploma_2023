#include <cctype>
#include <cstdlib>
#include <iostream>

int main() {
  char c, vowels[] = {'a', 'e', 'i', 'o', 'u'};

  std::cout << "Enter a character: ";
  std::cin >> c;

  // check if character is a letter
  if (!isalpha(c)) {
    std::cout << c << " is not a letter" << std::endl;
    exit(1);
  }

  std::cout << c << " is ";

  for (char i : vowels) {
    // convert character to lowercase then compare to vowels
    if (tolower(c) == i) {
      std::cout << "a vowel" << std::endl;
      return 0;
    }
  }

  std::cout << "a consonant" << std::endl;
  return 0;
}
