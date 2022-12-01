#include <stdl

void fibonacci(int n)
{
	if (n < 2)
	{
		std::cout << n << std::endl;
	}
	else 
	{
		fibonacci(n-1) + fibonacci(n-2);
	}
};

int main()
{
	fibonacci(2);
}
