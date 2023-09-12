#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

int main() {
  int a, b, c, hyp;

  std::cout << "Enter three sides of a triangle:-" << std::endl;
  std::cout << "Side A: ";
  std::cin >> a;
  std::cout << "Side B: ";
  std::cin >> b;
  std::cout << "Side C: ";
  std::cin >> c;

  std::vector<int> sides = {a, b, c};

  // get the largest side as hypotenuse
  auto max_e = std::max_element(sides.begin(), sides.end());
  hyp = *max_e;
  sides.erase(max_e);

  // check if it is a right angled triangle
  bool is_right =
      std::pow(sides[0], 2) + std::pow(sides[1], 2) == std::pow(hyp, 2);

  if (is_right)
    std::cout << "This is a right angled triangle." << std::endl;
  else
    std::cout << "This is not a right angled triangle." << std::endl;

  return 0;
}
