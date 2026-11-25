# Mudanças no cadastro de CNPJ do Brasil

Dados abertos, mês a mês, sobre empresas que mudaram no cadastro público de CNPJ da Receita Federal: quantas ficaram inaptas, foram baixadas, saíram do Simples Nacional, mudaram de porte ou ganharam sócio novo, por estado.

Mantido pela [Reveno](https://reveno.com.br) a partir do motor de mudanças do [LeadIA](https://leadia.reveno.com.br), que compara as bases mensais da Receita empresa a empresa.

## Arquivos

| Arquivo | O que tem |
|---|---|
| `dados/mudancas-2026-11.csv` | Comparação entre as bases de 10/2026 e 11/2026, por estado e tipo de mudança |

Colunas: `referencia` (mês da base), `uf`, `tipo` (`inaptas`, `baixadas`, `saiu-do-simples`, `mudou-de-porte`, `socio-novo`) e `empresas` (contagem).

O boletim de cada mês, com tabelas e método, fica em https://leadia.reveno.com.br/research/boletim-receita e o CSV mais recente em https://leadia.reveno.com.br/dados/mudancas-AAAA-MM.csv

## Consultar uma empresa

Cada sociedade tem uma ficha em JSON, grátis e sem chave:

```
GET https://leadia.reveno.com.br/cnpj/{cnpj}.json
```

Veja `exemplos/` (Python e JavaScript) e a documentação em https://leadia.reveno.com.br/api-cnpj

## Método e limites

- Fonte: cadastro público de CNPJ da Receita Federal (dados abertos), comparado mês a mês.
- Contagens incluem todas as naturezas jurídicas, MEI inclusive. Saída do Simples e mudança de porte contam só empresas que seguem ativas. Sócio novo conta empresas ativas com entrada de sócio nos 30 dias até a data mais recente publicada.
- A referência é mensal: a data exata de cada mudança não é informada.
- Situação cadastral não é regularidade fiscal.
- Sem dados de pessoas físicas.

## Licença

- Dados: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR). Cite "LeadIA by Reveno, com dados da Receita Federal", com link para https://leadia.reveno.com.br
- Código dos exemplos: MIT.
