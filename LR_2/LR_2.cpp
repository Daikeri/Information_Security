
#include <iostream>
#include <math.h>
using namespace std;

int SymNumb(int n)
{
	int sym = 0;
	while (n > 0)
	{
		sym += n % 10;
		n /= 10;
	}
	return sym;
}

int Find(int num)
{
	cout << "num = " << num << endl;

	int multiplicity = 9;

	int final_sym = SymNumb(num);

	while (final_sym >= multiplicity)
		multiplicity += 9;

	return multiplicity - final_sym;

}
int main()
{
	cout << "r2 = " << Find(356633); // 1 356 666 - 33 = 1 356 633 -> 156633 удалили 3 | 356633 убрали 1
}


