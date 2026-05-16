# 🧠 MEMORY.md — Formação Nutrição Avançada (FNA T8)

## 📌 Contexto e Objetivo
Este projeto (`apps/imersao/vendas-fna`) é a página de vendas premium e de altíssima conversão para a Turma 8 da Formação Nutrição Avançada (FNA).
O objetivo é apresentar uma proposta de valor irresistível (Ancoragem de R$ 5.826 vs Oferta de R$ 1.597 ou 12x R$ 165), destacando a Biblioteca de 11 Agentes de IA, as 19 Trilhas de aprendizagem e os 12 Bônus exclusivos.

## 🏗️ Arquitetura e Decisões de Design
- **Framework:** Astro 4.x
- **Estilização:** CSS nativo puro (`src/styles/global.css`) focado em performance, responsividade mobile-first e glassmorphism premium.
- **Paleta de Cores:** Azul Escuro (`#0A192F` / `#0f172a`), Azul Vibrante (`#1D4ED8` / `#2563EB`), Branco Gelo (`#F8FAFC`), toques sutis de Dourado/Amarelo para destaque de oferta e badges.
- **Tipografia:** **Libre Franklin** (corpo e leitura) e **Bebas Neue** (títulos e impacto).
- **Interatividade:** JavaScript nativo puro (modais, FAQ accordion, Swiper carrossel).

## 🚀 Histórico de Mudanças
- **16/05/2026:** Inicialização do projeto Astro, configuração base (`package.json`, `astro.config.mjs`, `tsconfig.json`) e criação da estrutura modular de componentes e PMP.
- **16/05/2026 (Parte 2):** Criação e estilização premium de todos os componentes (`Hero`, `Metodologia`, `AgentesIA`, `TrilhasGrid`, `BonusSection`, `PriceCard`, `Testimonials`, `BioNey`, `Faq`). Correção cirúrgica das horas exatas das trilhas (124h totais de vídeo) com base nos dados reais do Excel. Inicialização do repositório Git e push para `https://github.com/netoduwe/pagina-vendas-fna-maio26.git`.
- **16/05/2026 (Parte 3):** Atualização dos links oficiais de checkout (`https://links.nutrineyfelipe.com/turma-8`) no `PriceCard.astro` e de suporte do WhatsApp (`https://links.nutrineyfelipe.com/suporte-whatsapp`) no `Faq.astro`. Commit e push para o GitHub.
- **16/05/2026 (Parte 4):** Criação e integração de novas seções de alta conversão: `ProblemaSolucao.astro` (17 dores e soluções do consultório), `GrandesEntregas.astro` (As 4 grandes entregas da Formação), `ComparacaoOferta.astro` (Oferta Normal vs Oferta Imersão), detalhamento dos 7 Agentes de IA específicos no `AgentesIA.astro` e ajuste do texto da garantia de 7 dias no `PriceCard.astro`. Build verificado com sucesso. Commit e push para o GitHub.
- **16/05/2026 (Parte 5):** Identificação e correção de divergência de repositórios remotos. Configuração do remote `vercel` (`https://github.com/netoduwe/fna-vendas.git`) e push forçado para sincronizar com o projeto ativo na Vercel (`fna-vendas.vercel.app`).
