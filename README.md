# Bioinformatics & Clinical Data Analysis

This repository contains Python scripts designed for medical dataset verification, genomic, and molecular biology analysis. It serves as a practical portfolio for clinical data validation workflows using international scientific standards.

## Overview

### 1. Análise_dna.py (DNA Analysis Pipeline)
A Python script utilizing the **Biopython** library to simulate a clinical molecular diagnostic pipeline.
*   **Features:** Automates DNA translation to mRNA, protein synthesis simulation, and calculates GC content percentage (essential for PCR primer validation and stability analysis).
*   **Output:** Generates a structured JSON clinical report ready for laboratory documentation.

### 2. Zika_download_dna.py (Genomic Data Acquisition)
A pipeline that establishes a secure remote connection with the **NCBI (National Center for Biotechnology Information)** servers in the United States.
*   **Features:** Fetches the real genomic sequence of the Zika Virus (Accession: NC_012532.1) in real-time.
*   **Output:** Extracts biological metadata (organism name, sequence length) and exports the complete genome into a standardized `.fasta` file.

## Tech Stack & Libraries
*   **Language:** Python 3
*   **Core Libraries:** Biopython (Seq, SeqIO, Entrez, gc_fraction), JSON.
*   **Data Formats:** FASTA, GenBank (GB), JSON.

## Author
**Rafael Azambuja Gonçalves Junior**
Licensed Biomedical Scientist (CRBM-RS 015238) specialized in Clinical Data Validation and Scientific Literature Review.
