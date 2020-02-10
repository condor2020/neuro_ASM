Python 2.7 enviroment

adjust_p_value.py  Complete the calculation of corrected pvalue

pwl.py  Calculation of piecewise linear regression

Extract_genotype.py  Complete the extraction of genotype of different disease types

Extract_signal.py  Complete the extraction of methy signal of different disease types

calcuate_hwe_maf.py Calculate HWE and MAF values

basic_filtering.py  Complete SNP ID mapping and noise data filtering

select_ASM.py  Finish filtering ASM data

BPD DATA:
	signal : GSE71443_BD_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt
	genotype: GSE71443_BD_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt
	
SCZ DATA:
	signal : GSE71443_SZ_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt
	genotype: GSE71443_SZ_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt
	
CONTROL DATA:
	signal : GSE71443_control_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt
	genotype: GSE71443_control_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt
	
ALL DATA:
	signal : GSE71443_control+case_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt
	genotype: GSE71443_control+case_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt


Running for gwas:

firstly run: Extract_genotype.py

secondly run: Extract_signal.py

third run: calcuate_hwe_maf.py

fourth run: basic_filtering.py

fifth run: select_ASM.py


