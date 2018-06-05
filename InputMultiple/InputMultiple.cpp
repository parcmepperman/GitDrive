// InputMultiple.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string	firstName;
	string	lastName;
	int		age;
		cout << endl << "Type  First name	Last name 	Age  " <<endl << endl << "	";
		cin >> firstName >> lastName >> age;  

		cout << endl << endl << "	";
		cout << lastName << ", " << firstName << "	" << " Age:	" << age << endl;

		cout << endl;
	system("pause");


	return 0;
}

