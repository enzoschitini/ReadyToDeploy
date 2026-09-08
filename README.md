# ReadyToDeploy
Python do zero ao primeiro deploy. Curso completo para iniciantes que querem colocar código em produção.

https://enzoschitini.github.io/ReadyToDeploy/

index - Na raiz do projeto (Base)
└── pages - Pasta com a estrutura base de todas as máginas (Só vai mudar o conteudo que vem de um json)
    ├── bootcamps - Listagem dos bootcamps
    │   └── bootcamp- Quando seleciona um bootcamp
    │       └── modules - Aquilo que é trilha vai ser módulo é aqui é a listagem deles
    │           └── module - Quando clica em um módulo (atualmente chamado de trilha)
    │               └── lesson - Uma página com um determinado conteúdo de um módulo
    ├── projects - Página que lista todos os projetos
    │   └── project - O projeto em especifico
    └── contact - Hoje chamado de Ranking mas vai mudar e vai ser a página onde o usuário entra em contato.

course_content - Pasta com conteúdos salvos em json
└── pt_br - Pasta dos conteudos em portugues
    ├── bootcamps - Json com os bootcamps (cada um vai ter um id)
    ├── modules - Json com os módulos cada um com um id e um id sendo o id do bootcamp associado
    ├── lessons - Json com os conteúdos dos modulos cada um com um id e um id sendo o id do módulos associado
    ├── projects - Json com os projetos cada um com um id e um id sendo o id do bootcamp associado
    ├── presentations - Json com as apresentações do modulo cada um com um id e um id sendo o id do módulos associado (No momento não vai ter)
    ├── quiz - Json com os quiz cada um com um id e um id sendo o id do módulos associado (No momento não vai ter)
    └── research - Json com as pesquisas cada um com um id e um id sendo o id do módulos associado (No momento não vai ter)

application_content - Pasta com o conteudo real da aplicação (Sem ser o conteudo)
└── pt_br - Pasta da versão em protugues
    └── index
        ├── bootcamps
        │   └── bootcamp
        │       └── modules
        │           └── module
        │               └── lesson
        ├── projects
        │   └── project
        └── contact