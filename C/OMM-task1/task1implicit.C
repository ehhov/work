#include <iostream>
#include <cmath>
#define unit unsigned int
using namespace std;

const double h=.002, tau=.002, T=4, u_new_eps=1e-9;
const uint Nx=1/h, Nt=T/tau;

double border(double t) {return exp(-t);}
double initial(double x) {return 1+x*x;}

double checkfunc (double t, double x, double u) {
	double eu2=exp(u*u);
	if (u<1) return -log(u)+x*(1+eu2*eu2)/(2*u*eu2)-t;
	if (u>=1) return (x-sqrt(u-1))*(1+eu2*eu2)/(2*u*eu2)-t;
	return 0;
}

double derivfunc (double t, double x, double u) {
	double eu2=exp(u*u);
	if (u<=1) return -1/u+x*(2*eu2-(1+eu2*eu2)/(2*u*u*eu2)*(1+2*u*u));
	if (u>1) return -(1+eu2*eu2)/(4*u*eu2*sqrt(u-1))+x*(2*eu2-(1+eu2*eu2)/(2*u*u*eu2)*(1+2*u*u));
	return 0;
}


int main () {
	double u[Nt][Nx];
	double tmp, tmpf, fold, f1, f2;
	uint k,n;

	for (uint k=0; k<Nt; k+=1)
		u[k][0]=border(k*tau);
	for (uint n=0; n<Nx; n+=1)
		u[0][n]=initial(n*h);

	//	cout << checkfunc(0,0,1) << endl;
	
	/*for (k=1; k<Nt; k+=1)
 	for (n=1; n<Nx; n+=1)
	{
		tmp=u[k-1][n]; tmpf=checkfunc(k*tau,n*h,tmp);
		while (abs(tmpf)>u_new_eps) {
			fold =derivfunc(k*tau,n*h,tmp);
			tmp-=tmpf/fold;
			tmpf=checkfunc(k*tau,n*h,tmp);
		//	cout << "solution " << tmp << "\tfunc " << tmpf  << "\tderiv " << fold << endl;
		}
		u[k][n]=tmp;
		//cout << u[k][n] << "\t" << tmpf << endl;
		}*/

	for (k=1; k<Nt; k+=1)
 	for (n=1; n<Nx; n+=1)
	{
		tmp=1; fold=1;
		if (k*tau>n*h*(1+exp(1)*exp(1))/2/exp(1)) tmpf=0.01;
		else tmpf=2.01;
		f1=checkfunc(k*tau,n*h,tmp);
		f2=checkfunc(k*tau,n*h,tmpf);
		while (abs(fold)>u_new_eps) {
			fold=checkfunc(k*tau,n*h,tmp/2+tmpf/2);
			//cout << "solution " << tmp/2+tmpf/2 << " tmp" << tmp << " tmpf" << tmpf<< "\tf1 " << f1 << " f2" << f2  << "\tolder " << fold << endl;
			if (fold*f2<0) {tmp=tmp/2+tmpf/2; f1=fold;}
			if (fold*f1<0) {tmpf=tmp/2+tmpf/2; f2=fold;}
		}
		if (f1==fold) u[k][n]=tmp;
		if (f2==fold) u[k][n]=tmpf;
		//cout << u[k][n] << "\t" << tmpf << endl;
	}

	cout << "#t\tx\tu" << endl;
	for (uint k=0; k<Nt; k+=1)
	for (uint n=0; n<Nx; n+=1) {
		cout << k*tau << "\t" << n*h << "\t" << u[k][n] << endl;
		if (n==Nx-1) cout << endl;
	}
	return 0;
}
