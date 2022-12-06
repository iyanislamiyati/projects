/* PROJECT PEMROGRAMAN KOMPUTER
	Nama	: Iyan Islamiyati
	NIM		: G1B016021
	Program kumpulan konstanta fisis (sumber: Buku Serway)
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int pilihan;
	
	printf("\n\t==============================");
	printf("\n\tAPLIKASI KAMUS KONSTANTA FISIS");
	printf("\n\t==============================");
	printf("\n\n\t\tIYAN ISLAMIYATI");
	printf("\n\tFISIKA MIPA UNIVERSITAS MATARAM");
	
	printf("\n\n");
	printf(" PILIH KONSTANTA FISIS YANG DIBUTUHKAN \n");
	printf("1. SATUAN MASSA ATOM\n");
	printf("2. BILANGAN AVOGADRO\n");
	printf("3. KONSTANTA BOLTZMANN\n");
	printf("4. KONSTANTA COULOMB\n");
	printf("5. MASSA ELEKTRON\n");
	printf("6. ELEKTRON VOLT\n");
	printf("7. MASSA NEUTRON\n");
	printf("8. KONSTANTA GRAVITASI\n");
	printf("9. MASSA PROTON\n");
	printf("10.KELAJUAN CAHAYA DALAM RUANG HAMPA\n");
	printf("\nPILIHAN	:\n");
	scanf("%d", &pilihan);
	switch(pilihan)

	{
	case 1:
	printf(" SATUAN MASSA ATOM\n");
	printf(" SIMBOL : u\n");
	printf(" NILAI	: 1,660 538 73 (13)E-27 kg\n");
	printf("\n");
	break;

	case 2:
	printf(" BILANGAN AVOGADRO\n");
	printf(" SIMBOL : NA\n");
	printf(" NILAI	: 6,022 141 99 (47)E23 partikel/mol\n");
	printf("\n");
	break;

	case 3:
	printf(" KONSTANTA BOLTZMANN\n");
	printf(" SIMBOL : kB\n");
	printf(" NILAI	: 1,380 650 (24)E-23 J/K\n");
	printf("\n");
	break;

	case 4:
	printf(" KONSTANTA COULOMB\n");
	printf(" SIMBOL : ke\n");
	printf(" NILAI	: 8,987 551 788E9 N.m^2/C^2\n");
	printf("\n");
	break;

	case 5:
	printf(" MASSA ELEKTRON\n");
	printf(" SIMBOL : me\n");
	printf(" NILAI	: 9,109 381 88 (72)E-31 kg\n");
	printf("\n");
	break;
	
	case 6:
	printf(" ELEKTRON VOLT\n");
	printf(" SIMBOL : eV\n");
	printf(" NILAI	: 1,602 176 462 (63)E-19 J\n");
	printf("\n");
	break;
	
	case 7:
	printf(" MASSA NEUTRON\n");
	printf(" SIMBOL : mn\n");
	printf(" NILAI	: 1,674 927 16 (13) E-27 kg\n");
	printf("\n");
	break;
	
	case 8:
	printf(" KONSTANTA GRAVITASI\n");
	printf(" SIMBOL : G\n");
	printf(" NILAI	: 6,673 (10) E-11 N.m^2/kg^2\n");
	printf("\n");
	break;
	
	case 9:
	printf(" MASSA PROTON\n");
	printf(" SIMBOL : mp\n");
	printf(" NILAI	: 1,672 621 58 (13) E-27 kg\n");
	printf("\n");
	break;
	
	case 10:
	printf(" KELAJUAN CAHAYA DALAM RUANG HAMPA\n");
	printf(" SIMBOL : c\n");
	printf(" NILAI	: 2,997 924 58E8 m/s\n");
	printf("\n");
	}

}