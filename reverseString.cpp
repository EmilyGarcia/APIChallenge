#include <iostream>
#include <cstdlib>
#include <string>
#include <cassert>

using namespace std;

string reverseString(string original);
// Pre: Takes in a string
// Post: Returns a string with all elements reversed

int main()
{
  assert(reverseString("yecdfnmx") == "xmnfdcey");

  assert(reverseString("") == "");
  assert(reverseString("i") == "i");
  assert(reverseString("aa") == "aa");
  assert(reverseString("abc") == "cba");
  assert(reverseString("alphabet") == "tebahpla");

}

string reverseString(string original)
{
  string reversed = ""; // if length == 0, reversed == ""

  for (int i = 0; i < original.length(); i++)
    reversed = original[i] + reversed;

  return reversed;
}
