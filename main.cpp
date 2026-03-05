#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int num1, num2, num3;
    int maxVal, midVal, minVal;

    cout << "Enter three integers: ";
    cin >> num1 >> num2 >> num3;

    // TODO
    // Find max, min, mid using only if-statements (no loops, no functions, no arrays)

    // Find max
    maxVal = num1;
    if (num2 > maxVal) maxVal = num2;
    if (num3 > maxVal) maxVal = num3;

    // Find min
    minVal = num1;
    if (num2 < minVal) minVal = num2;
    if (num3 < minVal) minVal = num3;

    // Find mid (the one that is not max and not min)
    midVal = num1 + num2 + num3 - maxVal - minVal;

    cout << maxVal << " " << midVal << " " << minVal << endl;

    return 0;
}
