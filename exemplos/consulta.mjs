// Consulta a ficha de uma sociedade no LeadIA (grátis, sem chave). Uso: node consulta.mjs 00000000000191
const cnpj = String(process.argv[2] ?? '').replace(/[^0-9A-Za-z]/g, '').toUpperCase();
const resposta = await fetch(`https://leadia.reveno.com.br/cnpj/${cnpj}.json`);
if (!resposta.ok) throw new Error(`Não encontrado (${resposta.status})`);
const empresa = await resposta.json();
console.log(empresa.razaoSocial, '|', empresa.situacao, '|', empresa.atividadePrincipal.descricao);
for (const m of empresa.mudancas?.itens ?? []) console.log('Mudou:', m.campo, '->', m.descricao);
