# Página de Mentoria — Estrutura e Copy (proposta)

> Documento de trabalho para revisão antes de virar `application_content/pt_br/contact.json` + `pages/contact.html`. Tudo depois de "Copy da página" em cada seção é texto pronto para uso; o resto são notas minhas pra você decidir.
>
> **Segunda revisão:** a versão anterior estava puxando forte pro lado corporativo (Grupo Stefanini como gancho principal, linguagem de "arquitetura empresarial"). O público real é instituição de ensino — escola, curso técnico, universidade — não empresa. Reordenei pra liderar com a prova que mais importa pra esse público (o currículo gratuito já publicado) e reposicionei a experiência profissional como reforço de que o conteúdo é atual, não como o argumento principal.

---

## Headline — 3 opções

**A — currículo primeiro (recomendada)**
> Headline: Já construí, sozinho e de graça, um currículo completo de programação e IA — com aula, quiz, projeto prático e correção automática. Agora posso levar isso pra dentro da sua escola ou curso técnico.
> Subheadline: 41 módulos e 22 projetos publicados em português, open source. Também atuo profissionalmente com IA Generativa no mercado — o que mantém o conteúdo conectado com o que se usa hoje, não com o que era relevante há três anos.

Por quê: pra uma escola, a prova que mais pesa é currículo pronto e testado, não currículo profissional. A experiência de mercado entra como reforço de atualidade, não como o gancho.

**B — dor da instituição de ensino**
> Headline: Sua escola quer ensinar programação e IA de verdade. Sua equipe pedagógica não tem tempo de montar esse currículo do zero.
> Subheadline: Eu já montei: um percurso completo, gratuito e testado, com aula, quiz, projeto prático e correção automática. Posso adaptar isso pro currículo da sua instituição, ou formar os professores que vão aplicá-lo.

**C — trajetória pessoal / missão**
> Headline: Aprendi a programar aos 12 anos. Hoje ajudo escolas e cursos técnicos a ensinar isso direito.
> Subheadline: Sou o criador do Ready To Deploy — currículo gratuito de programação e IA em português — e atuo profissionalmente como Engenheiro de IA, o que mantém o que ensino conectado com o mercado real.

---

## Meta (aba do navegador / SEO)

- **title:** `Mentoria para instituições de ensino — Ready To Deploy`
- **description:** `Programas de mentoria em programação e Inteligência Artificial para escolas, cursos técnicos e universidades, guiados por quem criou o Ready To Deploy e atua profissionalmente com IA.`

---

## 1. Hero

| Campo | Copy |
|---|---|
| kicker | `// mentoria` |
| título | *(headline escolhida acima)* |
| subtítulo | *(subheadline correspondente)* |
| CTA primário | `Falar no LinkedIn →` → `https://www.linkedin.com/in/enzoschitini` (external) |
| CTA secundário | `Ver como funciona ↓` → `#como-funciona` |

O modal "Contratar mentoria" que já existe no `index.html` manda o visitante pra cá com a promessa "Tenha mentoria de programação e IA na sua instituição." As opções de headline mantêm essa promessa, priorizando prova de currículo sobre credencial de mercado.

---

## 2. Prova em números

Reaproveita os `stats` que já existem em `index.json` — é o ativo mais objetivo e verificável disponível, e fala diretamente com quem avalia currículo:

- **41** módulos publicados
- **22** projetos práticos
- **483** nós de conteúdo
- **100%** gratuito e open source — `AGPL-3.0` (código) · `CC BY-SA 4.0` (conteúdo)

**Legenda abaixo dos números:**
> Tudo isso foi escrito, estruturado e publicado por uma pessoa só, em português, sem paywall — antes de qualquer instituição pedir.

*(Sem número de alunos/visitantes — não há essa métrica verificada em lugar nenhum do projeto.)*

---

## 3. A prova já está publicada

**Kicker:** `// prova de trabalho`
**Título:** Antes de pedir confiança, mostrei o trabalho.

**Copy da página:**
> A maioria dos mentores vende currículo. Aqui tem link. Qualquer coordenador pedagógico ou diretor de curso pode abrir agora e conferir a qualidade do material antes de marcar uma conversa: [ver os módulos →](../pages/modules.html) · [ver o código no GitHub →](https://github.com/enzoschitini/ready-to-deploy)
>
> Isso importa pedagogicamente, não só como portfólio: cada módulo tem aula, glossário, quiz e uma tarefa prática corrigida automaticamente, rodando em sandbox no navegador — uma estrutura pensada pra ensinar, não só pra listar conteúdo. É esse mesmo desenho que entra na mentoria, adaptado ao currículo da sua instituição.

---

## 4. Quem é Enzo Schitini

**Kicker:** `// sobre o mentor`

**Copy da página:**
> Comecei a programar aos 12 anos, estudando robótica, e desde então acredito que aprendizado de verdade acontece na prática — é esse princípio que guia o Ready To Deploy, o currículo gratuito de programação e IA que criei pra quem não teria acesso a isso de outra forma.
>
> Sou Cientista de Dados e Engenheiro de IA, com 4 anos de experiência em projetos que unem desempenho, escalabilidade e boas práticas. Hoje atuo profissionalmente projetando arquiteturas de IA Generativa — RAG, orquestração de agentes, fine-tuning de LLM — o que mantém o que ensino conectado com o que o mercado realmente usa, não com o que era relevante há alguns anos.

**Foto:** já existe `assets/imgs/profile.jpg` — reaproveitar, mesma imagem usada na seção "idealizador" da home.

---

## 5. Trajetória

**Kicker:** `// trajetória`
**Título:** Experiência que mantém o conteúdo atualizado.

**Experiência**

| Cargo | Empresa | Período |
|---|---|---|
| Data Science & AI Engineer | EcGlobal Business (Grupo Stefanini) | desde abr/2025 · Salvador (BA), híbrido |
| Bubble Developer & AI Solutions Architect | Suportify | dez/2023 – abr/2025 · remoto |

**Copy da página — EcGlobal Business (Grupo Stefanini):**
> Projeto agentes de IA, pipelines de RAG e fine-tuning de LLM aplicados a processos reais — o mesmo tipo de tecnologia que está entrando agora nas discussões de currículo de escolas técnicas e cursos de dados.

**Copy da página — Suportify:**
> Construí do zero uma plataforma de agentes de IA personalizados, da arquitetura ao gerenciamento diário em produção — prova de que o que ensino eu também sei construir de ponta a ponta.

**Formação**

| Instituição | Curso | Período |
|---|---|---|
| Estácio | Tecnólogo em Análise de Sistemas | fev/2023 – dez/2026 *(conclusão prevista)* |
| Asimov Academy | Formação em IA Generativa (LLMs, prompt engineering, RAG, agentes) | jun/2025 – jan/2026 |
| EBAC — Escola Britânica de Artes Criativas e Tecnologia | Formação em Ciência de Dados e Análise de Dados | ago/2023 – set/2024 |

*Detalhe que vale considerar usar: a Asimov Academy é uma das escolas que o próprio Ready To Deploy recomenda na home, na seção "canais que valem a pena seguir" — ou seja, você estudou com uma referência que também indica pra sua comunidade. Bom sinal de coerência pra uma instituição de ensino avaliar.*

---

## 6. O que a mentoria oferece {#como-funciona}

**Kicker:** `// como funciona`

1. **Diagnóstico** — conversa inicial pra entender o nível da turma ou dos professores, o objetivo da instituição e o que já existe de currículo.
2. **Trilha sob medida** — adaptação dos módulos (programação, dados, IA aplicada) ao currículo e ao ritmo da instituição — seja pra formar professores, seja pra ensinar direto aos alunos.
3. **Mentoria prática** — sessões guiadas com exercícios reais — o mesmo formato "aprender fazendo" do Ready To Deploy, não aula expositiva.
4. **Acompanhamento** — checkpoints de progresso e ajuste de rota ao longo do programa.

**Sobre o formato:** hoje trabalho em regime híbrido no meu dia a dia — remoto ou presencial se ajustam conforme o que fizer sentido pra instituição. Carga horária e duração do programa ficam definidas no diagnóstico inicial, porque variam muito entre uma escola técnica e um núcleo de extensão universitária.

---

## 7. Pra quem é

**Kicker:** `// pra quem é`

- Escolas técnicas e cursos livres que precisam atualizar o currículo de programação e IA
- Cursos profissionalizantes e cursinhos técnicos
- Universidades e núcleos de extensão
- Equipes pedagógicas que querem formação para os próprios professores, não só para alunos

*(Tirei "empresas" da lista — o foco real é instituição de ensino. Se quiser reabrir pra capacitação corporativa depois, é só adicionar um bullet à parte, mas não puxando a página inteira pra esse lado de novo.)*

---

## 8. Perguntas frequentes

**Kicker:** `// perguntas frequentes`

**A mentoria é só para iniciantes?**
> Não. O conteúdo do Ready To Deploy vai do primeiro `print()` a projetos aplicados de IA; a trilha da mentoria é ajustada ao nível real da turma.

**Vocês adaptam o conteúdo ao currículo que já temos, ou é preciso substituir tudo?**
> Adapto. O diagnóstico inicial existe justamente pra entender o que já existe e encaixar a trilha em cima — não pra jogar fora o que a instituição já construiu.

**O programa é 100% remoto?**
> Não precisa ser. Trabalho em formato híbrido no meu dia a dia — remoto ou presencial, o formato se adapta ao que fizer sentido pra sua instituição.

**Isso é teoria ou vocês constroem algo de verdade?**
> As duas coisas, com peso maior em prática. É a mesma lógica usada nos projetos do Ready To Deploy: aprender fazendo, com checkpoints reais, não só slide.

**Como funciona o investimento?**
> Cada instituição tem um contexto diferente — o valor é definido depois do diagnóstico inicial, direto na conversa.

**Por que confiar num mentor com uma plataforma gratuita, em vez de contratar um curso pronto de mercado?**
> Porque o trabalho já está público e pode ser conferido antes de qualquer decisão — não é uma promessa, é um currículo no ar, testado e usado agora, criado por quem também aplica isso profissionalmente.

---

## 9. CTA final

| Campo | Copy |
|---|---|
| título | Sua instituição também pode ter isso. |
| corpo | Me chama no LinkedIn e conta o contexto da sua escola, curso ou programa — a gente desenha o formato a partir daí. |
| botão | `Falar com Enzo no LinkedIn →` → `https://www.linkedin.com/in/enzoschitini` (external) |

---

## Anotações estratégicas

- **Por que a prova de currículo (seção 3) vem antes da bio profissional:** quem decide numa escola avalia pedagogia primeiro — se o material ensina de verdade — não pedigree de mercado. Currículo pronto e testado convence mais rápido que um cargo em empresa grande.
- **Por que o Grupo Stefanini ainda aparece, mas depois:** continua sendo um dado real e relevante — mostra que o conteúdo ensinado é o mesmo que se usa em produção agora, não teoria desatualizada. Mas vira reforço de atualidade, não o gancho principal, porque o público não é RH corporativo.
- **"Empresas" removido de "pra quem é":** era o ponto mais claro do desalinhamento — a página falava com dois públicos ao mesmo tempo (escola e empresa) e isso deixa a mensagem menos afiada pra ambos. Focada em instituição de ensino agora.
- **Tom:** mantido o padrão de kicker `// algo` e frases diretas do resto do site, registro um pouco mais formal que a home — mas com vocabulário de educação (coordenador pedagógico, currículo, professores, alunos) em vez de vocabulário corporativo (gestor, arquitetura empresarial, ROI).
- **Um só destino de conversão:** a página inteira empurra pro LinkedIn, igual ao cartão "Contatar agora" do modal atual.
- **Nenhum número de audiência ou depoimento inventado:** seguem as mesmas ressalvas da versão anterior — nada foi estimado ou fabricado.

## O que ainda depende de você (não é falta de dado, é decisão)

1. Escolher a headline (topo do documento) — ou pedir uma variação.
2. Confirmar se quer travar duração/carga horária do programa na própria página, ou manter como "definido no diagnóstico" (como está agora).
3. Depoimento ou caso real de instituição/aluno, se e quando existir.

Com isso dá pra fechar `application_content/pt_br/contact.json` e montar `pages/contact.html` no mesmo padrão das outras telas (fetch de JSON, mesmo header/footer/modal já usados em `bootcamp.html`, `module.html` etc.).
