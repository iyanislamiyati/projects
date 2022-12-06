/*
	calculating density matrix of the single particle quantum system in the infinite square well
	using finite difference time domain method (FDTD)
	additional cases: calculate helmholtz's free energy and entropy
	
	last updated: 22/10/20
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define IDX(a1,a2,n1,n2) ((a1)*(n2)+(a2))

int main(int argc, char *argv[])
{
	long int i, j, n, m, NX, NX1, NT;
	double delt, delx;
	double delxsq, div2delxsq, deltdiv2delxsq, delxsqdivdelt;
	double temp, energy, tempenergy;
	double psitemp, T, beta;
	double *psi, *psiNew;
	double *v, *ca, *cb, *partition, *denmat, *internal_energy, *free_energy, *entropy;
	size_t nblock, nblock2;
	
	FILE *outdata;
	
	//Input parameters
	NX = 300;
	NT = 32768;
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
	
	//Initialize to zero
	for(i = 0; i <= NX; i++){
		v[i] = 0.0E0;
		psi[i] = 0.0E0;
		psiNew[i] = 0.0E0;		
	}
	
	//Set potentials
	for(i = 0; i <= NX; i++){
		v[i] = 0.0E0;
	}
	
	//Compute ca and cb
	for(i = 0; i <= NX; i++){
		temp = 1.0 + 0.5*delt*v[i];
		ca[i] = (1.0 - 0.5*delt*v[i])/temp;
		cb[i] = 1.0/temp;
	}
	
	//Do iterations
	//Initialize to zero
	for(n = 1; n < NT; n++){
		partition[n] = 0.0;
		internal_energy[n] = 0.0;
	}
	
	for(i = 0; i <= NX; i++){
		for(j = 0; j <= NX; j++){
			denmat[IDX(i,j,NX1,NX1)] = 0.0E0;
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
		
		for(n = 1; n <= NT; n++){
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
				
			//Compute partition function
			temp = 0.0;
			for(i = 0; i <= NX; i++){
				temp = temp + psi[i]*psi[i];
			}
			partition[n] += temp*delx;

			// Compute internal energy
			energy = 0;
			for(i = 1; i < NX; i++){
				tempenergy = 0;
				tempenergy -= (psi[i-1] - 2.0*psi[i] + psi[i+1])/(2.0*delxsq);
				tempenergy += v[i]*psi[i];
				energy += psi[i]*tempenergy;
			}
			internal_energy[n] += energy*delx;
			
		}
			
		//Density matrix
		for(i = 0; i <= NX; i++){
			for(j = 0; j <= NX; j++){
				denmat[IDX(i,j,NX1,NX1)] += psi[i]*psi[j];
			}
		}
	}
	
	// Compute free energy
	for(n = 1; n <= NT; n++){
		beta = 2.0*delt*n;
		free_energy[n]= 0;
		free_energy[n] = ((-1.0)*log(partition[n]))/beta;
	}
	
	// Compute entropy
	for(n = 1; n <= NT; n++){
		beta = 2.0*delt*n;
		entropy[n] = 0;
		entropy[n] = (internal_energy[n] - free_energy[n])*beta;
	}
	
	printf("<< Results >>\n");
	printf(" Partition Function: %ld  %le \n", NT, partition[NT]);

	//Save
	if((outdata = fopen("fungsi-partisi-fdtd-15.dat","w")) == NULL){
		fprintf(stderr," Cannot open file fungsi-partisi-fdtd-15.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*i*delt), partition[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("entropi-fdtd-15.dat","w")) == NULL){
		fprintf(stderr," Cannot open file entropi-fdtd-15.dat\n");
		exit(3);
	}
	for(i = 256; i <= 16384; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*i*delt), entropy[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("energi-bebas-fdtd-15.dat","w")) == NULL){
		fprintf(stderr," Cannot open file energi-bebas-fdtd-15.dat\n");
		exit(3);
	}
	for(i = 3841; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*i*delt), free_energy[i]);
	} 
	fclose(outdata);

	if((outdata = fopen("energi-dalam-fdtd-16.dat","w")) == NULL){
		fprintf(stderr," Cannot open file energi-dalam-fdtd-16.dat\n");
		exit(3);
	}
	for(i = 1; i <= NT; i++){
		fprintf(outdata,"%lf	%10.6le \n", 1.0/(2.0*i*delt), internal_energy[i]);
	} 
	fclose(outdata);
	
	if((outdata = fopen("density-matrix-fdtd.dat","w")) == NULL){
		fprintf(stderr," Cannot open file density-matrix-fdtd.dat\n");
		exit(3);
	}
	
	for(i = 1; i <= NX; i++){
		for(j = 1; j <= NX; j++){
			fprintf(outdata,"%le	", denmat[IDX(i,j,NX1,NX1)]/partition[NT]);
		}
		fprintf(outdata,"\n");
	} 
	fclose(outdata);
	
	if((outdata = fopen("densitas-fdtd-15.dat","w")) == NULL){
		fprintf(stderr," Cannot open file densitas-fdtd-15.dat\n");
		exit(3);
	}
	
	for(i = 1; i <= NX; i++){
		for(j = 1; j <= NX; j++){
			if (i == j){
				fprintf(outdata,"%lf	%le", i*delx, denmat[IDX(i,j,NX1,NX1)]/partition[NT]);
			}
		}
		fprintf(outdata,"\n");
	} 
	fclose(outdata);
	
	return 0;
}