"""Consulta a ficha de uma sociedade no LeadIA (grátis, sem chave). Uso: python consulta.py 00000000000191"""
import json
import sys
import urllib.request

cnpj = "".join(c for c in (sys.argv[1] if len(sys.argv) > 1 else "") if c.isalnum()).upper()
with urllib.request.urlopen(f"https://leadia.reveno.com.br/cnpj/{cnpj}.json") as resposta:
    empresa = json.load(resposta)
print(empresa["razaoSocial"], "|", empresa["situacao"], "|", empresa["atividadePrincipal"]["descricao"])
for mudanca in (empresa.get("mudancas") or {}).get("itens", []):
    print("Mudou:", mudanca["campo"], "->", mudanca["descricao"])
