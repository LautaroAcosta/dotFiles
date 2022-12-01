#include <iostream>
#include <stdio.h>


class Bolita
{
	int radio;
public:
	Bolita(int r)
	{
		radio = r;
	};

	void presentar()
	{
		std::cout << radio << std::endl;  
	};
};

int main()
{
	Bolita p = Bolita(10);
	p.presentar();
	return 0;

}
