#include <iostream>
#include <cmath>
#define uint unsigned int
using namespace std;

const double pi=3.141592653589793238462643383279502884197169399, divide=4.304127680474161;
const uint Nx=101, Ny=101, Nt=201, k0=2;
const double hx=1.0/(Nx-1), hy=1.0/(Ny-1), tau=1.0/(Nt-1), T=1.0;
double u[Nx][Ny][Nt];
double alphax[Nx-1], betax[Nx-1], alphay[Ny-1], betay[Ny-1];
uint count=0;


double func(double x, double y, double t) {return sin(pi*x)*y*(y-1)*t;}
double init(double x, double y) {return 0;}

void calculate_x (uint k, uint m) {
	for (uint n=1; n<Nx-1; n+=1) {
		double f=hx*hx*func(n*hx,m*hy,k*tau), d2uy=hx*hx/hy/hy*(u[n][m+1][k]-2*u[n][m][k]+u[n][m-1][k]);
		betax[n]=(betax[n-1]+f+d2uy+hx*hx*u[n][m][k]/tau)*alphax[n];
	}
	u[Nx-1][m][k+1]=u[Nx-1][m][k+1];
	for (int n=Nx-2; n>=0; n-=1) {
		u[n][m][k+1]=alphax[n]*u[n+1][m][k+1]+betax[n];
	}
	u[Nx-1][m][k+1]=u[Nx-2][m][k+1];
	return;
}

void calculate_y (uint k, uint n) {
	for (uint m=1; m<Ny-1; m+=1) {
		double f=hy*hy*func(n*hx,m*hy,k*tau), d2ux=hy*hy/hx/hx*(u[n+1][m][k]-2*u[n][m][k]+u[n-1][m][k]);
		betay[m]=(betay[m-1]+f+d2ux+hy*hy/tau*u[n][m][k])*alphay[m];
	}
	u[n][Ny-1][k+1]=u[n][Ny-1][k];
	for (int m=Ny-2; m>=0; m-=1) {
		u[n][m][k+1]=alphay[m]*u[n][m+1][k+1]+betay[m];
	}
	u[n][Ny-1][k+1]=u[n][Ny-2][k+1];
	return;
}


int main () {
	double time;
	uint par_k=k0, is_max=1;

	//cin >> time;
	
	alphax[0]=1.0;
	betax[0]=0.0;
	for (uint i=1; i<Nx-1; i+=1)
		alphax[i]=1.0/(2+hx*hx/tau-alphax[i-1]);
	alphay[0]=1.0;
	betay[0]=0.0;
	for (uint i=1; i<Ny-1; i+=1)
		alphay[i]=1.0/(2+hy*hy/tau-alphay[i-1]);

	for (uint k=0; k<Nt; k+=1) {
		for (uint m=0; m<Ny; m+=1)
			{u[0][m][k]=0; u[Nx-1][m][k]=0;}
		for (uint n=0; n<Nx; n+=1)
			{u[n][0][k]=0; u[n][Ny-1][k]=0;}
	}
	
	for (uint n=0; n<Nx; n+=1)
		for (uint m=0; m<Ny; m+=1)
			u[n][m][0]=init(hx*n, hy*m);

	//cerr << u[Nx/2][Ny/2][0];
	
	for (uint k=0; k<Nt-2; k+=2) {
		for (uint m=1; m<Ny-1; m+=1)
			calculate_x(k,m);
		for (uint n=1; n<Nx-1; n+=1)
			calculate_y(k+1,n);
	}

	//par_k=time/tau/2;
	//par_k*=2;
	//if (par_k>=Nt) par_k=2*(Nt-1)/2;

	for (uint n=0;n<Nx;n+=1)
		for (uint m=0;m<Ny;m+=1) {
			cout << n*hx << ' ' << m*hy << ' ' << u[n][m][par_k] << endl;
			if (m==Ny-1) cout << endl;
		}

	if (is_max==1) {
		time=0;
		for (uint k=0; k<Nt; k+=1)
		for (uint n=0; n<Nx; n+=1)
		for (uint m=0; m<Ny; m+=1)
			if (time<abs(u[n][m][k])) {time=abs(u[n][m][k]); par_k=k;}
		cerr << "Maximum " << time << " at time " << par_k*tau << ',' << par_k << endl;
	}
	
	return 0;
}
