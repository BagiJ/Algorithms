// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

int main()
{
	long size;
	long sizeCeil;
	std::cin >> size;
	
	if (size % 4 == 0)
		sizeCeil = ((size / 4)) * 4;
	else
		sizeCeil = ((size / 4) + 1) * 4;

	std::cout << sizeCeil;
}

