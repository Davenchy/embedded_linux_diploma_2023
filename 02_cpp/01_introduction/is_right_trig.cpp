#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using std::cout, std::cin, std::endl;
using std::pow;
using std::vector, std::max_element;

int main() {
  int a, b, c, hyp;

  cout << "Enter three sides of a triangle:-" << endl;
  cout << "Side A: ";
  cin >> a;
  cout << "Side B: ";
  cin >> b;
  cout << "Side C: ";
  cin >> c;

  vector<int> sides = {a, b, c};

  // raise all sides to the power of 2
  for (auto &side : sides)
    side = pow(side, 2);

  // get the largest side as hypotenuse
  auto max_e = max_element(sides.begin(), sides.end());
  hyp = *max_e;
  sides.erase(max_e);

  // check if it is a right angled triangle
  bool is_right = sides[0] + sides[1] == hyp;

  if (is_right)
    cout << "This is a right angled triangle." << endl;
  else
    cout << "This is not a right angled triangle." << endl;

  return 0;
}
