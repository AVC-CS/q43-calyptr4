#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int num1, num2, num3;
    int maxVal, midVal, minVal;

    cout << "Enter three integers: ";
    cin >> num1 >> num2 >> num3;

    if (num1 < num2 && num1 < num3){
        minVal = num1;
    } else if (num2 < num1 && num2 < num3){
        minVal = num2;
    } else minVal = num3;

    if (num1 > num2 && num1 > 3){
        maxVal = num1;
    } else if (num2 > num1 && num2 > num3){
        maxVal = num2;
    } else maxVal = num3;

    if (num1 != minVal && num1 != maxVal){
        midVal = num1;
    } else if (num2 != minVal && num2 != maxVal){
        midVal = num2;
    } else midVal = num3;

    cout << maxVal << " " << midVal << " " << minVal << endl;

    return 0;
}
