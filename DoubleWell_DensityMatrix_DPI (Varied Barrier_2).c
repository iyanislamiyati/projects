/*
	calculating density matrix of the single particle quantum system in the double well potential
	additional cases: calculate helmholtz's free energy and entropy
	
	last updated: 22/10/20
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define IDX(a1,a2,n1,n2) ((a1)*(n2)+(a2))

int main(int argc, char *argv[])
{
	long int i, j, ij, n, m, NX, NX1, NT, N;
	long int k, ik, kj;
	double delt, delx, beta, x2, x4;
	double delxsq, div2delxsq, deltdiv2delxsq, delxsqdivdelt;
	double temp, *tempenergy;
	double psitemp, *partition, *internal_energy, *free_energy, *entropy;
	double *psi, *psiNew;
	double *v, *ca, *cb, *denmat;
	double *rho0, *rho, *rhonew;
	double sum;
	size_t nblock, nblock2;
	
	FILE *outdata;
	
	//Input parameters
	NX = 400;
	NT = 15;
	delx = 0.01;
	delxsqdivdelt = 5.0;
		
	//Initialize parameters
	NX1 = NX + 1;
	delxsq = delx*delx;
	delt =  delx*delx/delxsqdivdelt;
	div2delxsq = 1.0/(2.0*delxsq);
	deltdiv2delxsq = delt*div2delxsq;
	
	//Allocate memory
	nblock = NX1;
	v = (double *) malloc((size_t) (nblock*sizeof(double)));
	psi = (double *) malloc((size_t) (nblock*sizeof(double)));
	psiNew = (double *) malloc((size_t) (nblock*sizeof(double)));
	ca = (double *) malloc((size_t) (nblock*sizeof(double)));
	cb = (double *) malloc((size_t) (nblock*sizeof(double)));
	
	//Partition function
	partition = (double *) malloc((size_t) ((NT+1)*sizeof(double)));
	
	//Internal Energy
	internal_energy = (double *) malloc((size_t) ((NT+1)*sizeof(double)));
	
	// Free Energy
	free_energy = (double *) malloc((size_t) ((NT+1)*sizeof(double)));
	
	// Entropy
	entropy = (double *) malloc((size_t) ((NT+1)*sizeof(double)));
	
	//Density matrix
	nblock2 = NX1*NX1;
	denmat = (double *) malloc((size_t) (nblock2*sizeof(double)));
	tempenergy = (double*) malloc((size_t) (nblock2*sizeof(double)));
	rho = (double*) malloc((size_t) (nblock2*sizeof(double)));
	rhonew = (double*) malloc((size_t) (nblock2*sizeof(double)));
	
	//Initialize to zero
	for(i = 0; i <= NX; i++){
		v[i] = 0.0E0;
		psi[i] = 0.0E0;
		psiNew[i] = 0.0E0;		
	}
	
	for(i = 0; i <= NT; i++){
		partition[i] = 0.0;
		free_energy[i] = 0.0;
		internal_energy[i] = 0.0;
		entropy[i] = 0.0;
	}
	
	//Set potentials
	for(i = 0; i <= NX; i++){
		if (i >= 0 && i <= 80){
			v[i] = 20.0;
		}else if(i >= 81 && i <= 160){
			v[i] = 0.0E0;
		}else if(i >= 161 && i <= 240){
			v[i] = 8.0;
		}else if(i >= 241 && i <= 320){
			v[i] = 0.0E0;
		}else{
			v[i] = 20.0;
		}
	}
	
	//Compute ca and cb
	for(i = 0; i <= NX; i++){
		temp = 1.0 + 0.5*delt*v[i];
		ca[i] = (1.0 - 0.5*delt*v[i])/temp;
		cb[i] = 1.0/temp;
	}
	
	//Do iterations
	//Initialize to zero	
	for(i = 0; i <= NX; i++){
		for(j = 0; j <= NX; j++){
			denmat[IDX(i,j,NX1,NX1)] = 0.0;
			tempenergy[IDX(i,j,NX1,NX1)] = 0.0;
		}
	}
	
	//Do summations
	for(m = 1; m < NX; m++){
		//Initial psi
		for(i = 0; i <= NX; i++){
			if(m == i){
				psi[i] = 1.0/sqrt(delx);
			} 
			else psi[i] = 0;
		}
		
		N = 1;
		for(n = 1; n <= N; n++){
			//Update psi
			for(i = 1; i < NX; i++){
				psitemp = deltdiv2delxsq*(psi[i+1] + psi[i-1] - 2.0*psi[i]);
				psiNew[i] = ca[i]*psi[i] + cb[i]*psitemp;
			}
			
			//Imposing boundary condition
			psiNew[0] = 0;
			psiNew[NX] = 0;
			
			//Store psi
			for(i = 0; i <= NX; i++){
				psi[i] = psiNew[i];
			}
			
		}
		
		//Density matrix
		for(i = 0; i <= NX; i++){
			for(j = 0; j <= NX; j++){
				denmat[IDX(i,j,NX1,NX1)] += psi[i]*psi[j];
			}
		}
	}
	// DPI
	for (i = 0; i <= NX; i++){
		for (j = 0; j<= NX; j++){
			ij = IDX(i,j,NX1,NX1);
			rho[ij] = denmat[ij];
		}
	}
	
	// Do iteration
	for (m = 1; m <= NT; m++){
		// one step rho(x,x',2 epsilon) 
		for (i = 0; i <= NX; i++){
			for (j = 0; j <= NX; j++){	
				// index
				ij = IDX(i,j,NX1,NX1);
			
				// compute integral
				sum = 0.0;
				for(k = 0; k <= NX; k++){
					ik = IDX(i,k,NX1,NX1);
					kj = IDX(k,j,NX1,NX1);
					sum += rho[ik]*rho[kj];
				}
				rhonew[ij] = sum*delx;
			}
		}
		// save for next iteration
		for (i = 0; i <= NX; i++){
			for (j = 0; j <= NX; j++){	
				ij = IDX(i,j,NX1,NX1);
				rho[ij] = rhonew[ij];
			}
		}
		
		// compute partition function
		partition[m] = 0.0;
		temp = 0.0;
		for(i = 0; i <= NX; i++){
			for(j = 0; j <= NX; j++){
				if(i == j){
					ij = IDX(i,j,NX1,NX1);
					temp += rho[ij];
				}
			}
		}
		partition[m] = temp*delx;
		
		// compute free energy
		beta = 2.0*delt*pow(2,m);
		free_energy[m]= 0;
		free_energy[m] = ((-1.0)*log(partition[m]))/beta;
		
		// compute internal energy
		for(i = 1; i < NX; i++){
			for(j = 1; j < NX; j++){
				tempenergy[IDX(i,j,NX1,NX1)] = 0.0;
				tempenergy[IDX(i,j,NX1,NX1)] -= (rho[IDX(i-1,j,NX1,NX1)] - 2.0*rho[IDX(i,j,NX1,NX1)] + rho[IDX(i+1,j,NX1,NX1)])/(2.0*delxsq);
				tempenergy[IDX(i,j,NX1,NX1)] += v[i]*rho[IDX(i,j,NX1,NX1)];
			}
		}
		// Trace
		internal_energy[m] = 0.0;
		temp = 0.0;
		for(i = 1; i < NX; i++){
			for(j = 1; j < NX; j++){
				if (i == j){
					temp += tempenergy[IDX(i,j,NX1,NX1)];
				}
			}
		}
		internal_energy[m] += temp*delx;
	}
	// Compute Entropy
	for(m = 1; m <= NT; m++){
		beta = 2.0*delt*pow(2,m);
		entropy[m] = 0;
		entropy[m] = (internal_energy[m] - free_energy[m])*beta;
	}
	
	
	printf("<< Results >>\n");
	printf(" Partition Function: %le \n",partition[NT]);

	
	//Save
	if((outdata = fopen("fungsi-partisi-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file fungsi-partisi-dpi-8.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*pow(2,i)*delt), partition[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("entropi-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file entropi-dpi-8.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*pow(2,i)*delt), entropy[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("energi-bebas-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file energi-bebas-dpi-8.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*pow(2,i)*delt), free_energy[i]);
	} 
	fclose(outdata);

	if((outdata = fopen("energi-dalam-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file energi-dalam-dpi-8.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*pow(2,i)*delt),  internal_energy[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("density-matrix-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file density-matrix-dpi-8.dat\n");
		exit(3);  
	}
	for(i = 1; i <= NX; i++){
		for(j = 1; j <= NX; j++){
			fprintf(outdata,"%le	", rho[IDX(i,j,NX1,NX1)]/partition[NT]);
		}
		fprintf(outdata,"\n");
	} 
	fclose(outdata);
	
	if((outdata = fopen("densitas-dpi-8.dat","w")) == NULL){
		fprintf(stderr," Cannot open file densitas-dpi-8.dat\n");
		exit(3);
	}
	
	for(i = 1; i <= NX; i++){
		for(j = 1; j <= NX; j++){
			if(i == j){
				fprintf(outdata,"%lf	%le", i*delx, rho[IDX(i,j,NX1,NX1)]/partition[NT]);
			}
		}
		fprintf(outdata,"\n");
	} 
	fclose(outdata);
	
	return 0;
}