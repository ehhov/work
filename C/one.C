#include <iostream>

using namespace std;

class one {
private:
	double self;
	char name [3];
public:
	one() {
		self=0;
		name[0]='o'; name[1]='n'; name[2]='e';
	}
	virtual void normal() {
		cout << "one's normal" << endl;
	}
	
	void test() {
		cout << "one's test" << endl;
	}
	
};

class two: public one {
private:
	double self;
	char name [3];
public:
	two() {
		self=0;
		name[0]='t'; name[1]='w'; name[2]='o';
	} 
	void normal() {
		cout << "two's normal" << endl;
	}

	void test() {
		cout << "two's test" << endl;
	}
};


int main() {
	one* hmm = new two;
	hmm->normal();
	hmm->test();
	return 0;
}
