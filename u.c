#include<stdio.h>
int main()
{
	int a;
	int *p;
	a=10;
	p=&a;
	printf("%u",p);
	printf("%u",p+1);
}
