from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import json

# Simulação de uma fita de DNA obtida de um banco de dados público (Ex: NCBI)
# ID do Paciente: PACIENTE_001_ID
sequence_data = "ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCGCTAAGCTAGCTAGCTAGCT"

# 1. Transformando a string pura em um objeto de sequência biológica (Biopython)
my_dna = Seq(sequence_data)

# 2. Operações de Bioinformática básicas
print("--- ANÁLISE BIOMÉDICA DE DADOS ---")
print(f"Sequência Original: {my_dna}")
print(f"Tamanho da Fita: {len(my_dna)} pares de bases.")

# Transcrição: DNA -> RNA Mensageiro
my_mrna = my_dna.transcribe()
print(f"RNA Mensageiro:     {my_mrna}")

# Tradução: RNA Mensageiro -> Proteína (Cadeia de Aminoácidos)
my_protein = my_mrna.translate()
print(f"Cadeia de Proteína: {my_protein}")

# Cálculo do Conteúdo GC (Porcentagem de Guaninas e Citosinas)
# Essencial para desenho de primers de PCR que você viu na faculdade
porcentagem_gc = gc_fraction(my_dna) * 100
print(f"Conteúdo GC:        {porcentagem_gc:.2f}%")

# 3. Estruturando o relatório automático para exportação (Formato JSON)
relatorio_paciente = {
    "paciente_id": "PACIENTE_001_ID",
    "tamanho_sequencia": len(my_dna),
    "conteudo_gc_porcentagem": round(porcentagem_gc, 2),
    "proteina_gerada": str(my_protein)
}

# Salvando o relatório estruturado em um arquivo físico
with open("relatorio_clinico_id.json", "w") as arquivo:
    json.dump(relatorio_paciente, arquivo, indent=4)

print("\n[SUCESSO] Relatório estruturado gerado e salvo em 'relatorio_clinico_id.json'!")
