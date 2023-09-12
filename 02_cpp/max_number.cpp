#include <iostream>
#include <regex>
#include <sstream>
#include <string>

int main() {
  int max = 0;
  std::string user_input;

  std::cout << "Enter numbers separated by spaces: ";
  std::getline(std::cin, user_input);

  std::stringstream input_stream(user_input);
  std::string word;

  std::regex reg("^[0-9]{1,10}$");
  while (input_stream >> word) {
    if (!std::regex_match(word, reg))
      continue;

    int value = std::stoi(word);
    if (value > max)
      max = value;
  }

  std::cout << "The maximum number is: " << max << std::endl;

  return 0;
}
