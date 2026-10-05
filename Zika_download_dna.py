from Bio import Entrez
from Bio import SeqIO

# 1. Configuração obrigatória para acessar o NCBI
# Coloque o seu e-mail real aqui. O NCBI exige isso para identificar quem está baixando os dados.
Entrez.email = "rafael.azambuja.jr@hotmail.com"

print("Conectando ao banco de dados do NCBI nos EUA...")

# 2. Buscando o genoma completo do Zika Vírus (Código de Acesso: NC_012532.1)
# Buscamos no banco de dados de nucleotídeos ("nucleotide") no formato GenBank ("gb")
with Entrez.efetch(db="nucleotide", id="NC_012532.1", rettype="gb", retmode="text") as handle:
    # Usamos o SeqIO para ler o arquivo retornado pelo servidor
    registro_virus = SeqIO.read(handle, "genbank")

print("\n--- DADOS DA SEQUÊNCIA BAIXADA ---")
print(f"ID do Registro: {registro_virus.id}")
print(f"Nome do Organismo: {registro_virus.annotations['organism']}")
print(f"Descrição Completa: {registro_virus.description}")
print(f"Tamanho do Genoma: {len(registro_virus.seq)} pares de bases (RNA).")

# Exibindo os primeiros 100 caracteres da sequência genética real do vírus
print(f"\nPrimeiros 100 nucleotídeos: {registro_virus.seq[:100]}...")

# 3. Salvando a sequência em um arquivo físico no formato FASTA (Padrão internacional da bioinformática)
nome_arquivo = "zika_virus_genome.fasta"
SeqIO.write(registro_virus, nome_arquivo, "fasta")

print(f"\n[SUCESSO] Genoma completo do Zika salvo com sucesso em '{nome_arquivo}'!")
