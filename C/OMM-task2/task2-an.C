#include <iostream>
#include <fstream>
#include <cmath>
#define uint unsigned int
using namespace std;

const double pi=M_PI;
const uint Nx=257, Ny=257, Nt=257, Nterms=5000;
const double hx=1.0/(Nx-1), hy=1.0/(Ny-1), tau=1.0/(Nt-1), T=1.0;
double u [Nx][Ny][Nt];


int main (){
	double sinx, time;
	uint par_k, k=1;

	cin >> par_k;

	for (uint n=0; n<Nx; n+=1) {
		sinx=sin(3*pi*n*hx);
		for (uint m=0; m<Ny; m+=1) {
			//for (uint k=0; k<Nt; k+=1){
				u[n][m][k]=0;
				for (uint i=0; i<Nterms; i+=1)
					for (uint j=0; j<Nterms; j+=1){
						u[n][m][k]+=коэффициент(i,j)*sin(i*x)*cos(pi*j*y/3);
						//u[n][m][k]+=4.0/(pi*(2.0*i+1)*(pi*pi*(4.0*i*i+4.0*i+10.0)-1.0))*(exp(-tau*k)-exp(-pi*pi*(4*i*i+4*i+10)*k*tau))*sin(pi*(2*i+1)*m*hy);
				}
				//u[n][m][k]*=sinx;
				//}
		}
	}

	//par_k=(uint)(time/tau);
	//if (par_k<0) par_k=0;
	//if (par_k>=Nt) par_k=Nt-1;

	time=0;
	for (uint n=0; n<Nx; n+=1) {
		for (uint m=0; m<Ny; m+=1) {
			cout << hx*n << ' ' << hy*m << ' ' << u[n][m][k] << endl;
			if (time<abs(u[n][m][par_k])) time=abs(u[n][m][k]);
			if (m==Ny-1) cout << endl;
		}
	}

	cerr << time << endl;

	//	cout << hx << ' ' << hy << ' ' << tau << endl;
	
	return 0;
}
