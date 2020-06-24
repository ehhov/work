#include <iostream>
#include <cmath>
#define unit unsigned int
using namespace std;

const double h=.002, tau=.002, T=4, u_new_eps=1e-8;
const uint Nx=1/h, Nt=T/tau;


double func(double x) {return atan(exp(x*x));}
double deriv(double x) {return 2*x*exp(x*x)/(1+exp(2*x*x));}
double initial(double t) {return exp(-t);}
double border(double x) {return 1+x*x;}

double checkfunc (double t, double x, double u) {
	if (u<1) return -log(u)+x*(1+exp(2*u*u))/(2*u*exp(u*u))-t;
	if (u>=1) return (x-sqrt(u-1))*(1+exp(2*u*u))/(2*u*exp(u*u))-t;
	return 0;
}


int main () {
	double u[Nt][Nx];
	double fold, tmp, tmpf;
	int check=2;
	
	for (uint k=0; k<Nt; k+=1)
		u[k][0]=initial(k*tau);
	for (uint n=0; n<Nx; n+=1)
		u[0][n]=border(n*h);

	for (uint k=0; k<Nt-1; k+=1)
	for (uint n=0; n<Nx-1; n+=1){
			fold=func(u[k+1][n]);
			tmp=u[k+1][n]; tmpf=h/tau*tmp+func(tmp)-h/tau*u[k][n+1]-fold;
			while (abs(tmpf)>u_new_eps){
				tmp-=tmpf/(h/tau+deriv(tmp));
				tmpf=h/tau*tmp+func(tmp)-h/tau*u[k][n+1]-fold;
			}
			u[k+1][n+1]=tmp;
	}

	if (check==1) {
		tmp=0;
		for (uint k=0; k<Nt; k+=1)
		for (uint n=0; n<Nx; n+=1){
			fold=checkfunc(k*tau, n*h, u[k][n]);
			if(abs(fold)>tmp) tmp=fold;
			tmpf+=abs(fold);
		}
		cout << "Max=" << tmp << "\tAvg=" << tmpf/Nx/Nt << endl;
	}
	if (check==0) {
		cout << "#t\tx\tu" << endl;
		for (uint k=0; k<Nt; k+=1)
		for (uint n=0; n<Nx; n+=1) {
			cout << k*tau << " " << n*h << " " << u[k][n] << endl;
			if (n==Nx-1) cout << endl;
		}
	}
	if (check==2) {
		cout << "#t\tx\tu" << endl;
		for (uint k=0; k<Nt; k+=1)
		for (uint n=0; n<Nx; n+=1) {
			cout << k*tau << "\t" << n*h << "\t" << checkfunc(k*tau,n*h,u[k][n]) << endl;
			if (n==Nx-1) cout << endl;
		}
	}
	return 0;
}
