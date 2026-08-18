# CreativeAI Tools

Outils, formats et méthodes open source pour concevoir, documenter et évaluer des workflows IA créatifs, éditoriaux et marketing.

L’objectif du repository est de rendre les pratiques IA plus portables : des fichiers lisibles par les humains, exploitables par les assistants et versionnables dans GitHub.

## Outils disponibles

### Brand Brain Evaluation Lab

Un laboratoire open source pour vérifier si un assistant IA respecte réellement une marque — et pas seulement s’il produit un résultat plausible.

Le kit évalue notamment :

- le positionnement et la posture ;
- les publics et les situations ;
- la voix et le style ;
- les preuves et la provenance des sources ;
- le format et le canal ;
- les contraintes visuelles et les droits ;
- la capacité à demander une validation humaine.

Le module comprend un protocole Markdown-first, une couche YAML structurée, des grilles de scoring et des cas de test fictifs.

➡️ [Ouvrir le Brand Brain Evaluation Lab](brand-brain-evaluation-lab/)

## Démarrage rapide

```bash
git clone https://github.com/creative-ai-fr/creativeai-tools.git
cd creativeai-tools/brand-brain-evaluation-lab
```

Pour commencer avec le Brand Brain d’exemple :

1. lisez [`README.md`](brand-brain-evaluation-lab/README.md) ;
2. consultez [`brand.yaml`](brand-brain-evaluation-lab/brand.yaml) ;
3. examinez [`examples/BRAND.md`](brand-brain-evaluation-lab/examples/BRAND.md) ;
4. lancez le cas [`CASE-001.yaml`](brand-brain-evaluation-lab/evals/cases/CASE-001.yaml) ;
5. utilisez les cas 002 et 003 pour tester les demandes nécessitant une escalade humaine.

Le kit peut être utilisé avec un assistant capable de lire des fichiers, notamment ChatGPT Work ou Claude Cowork. Les procédures détaillées figurent dans [`installation-and-test-block.html`](brand-brain-evaluation-lab/article/installation-and-test-block.html).

## Structure du repository

```text
creativeai-tools/
├── README.md
└── brand-brain-evaluation-lab/
    ├── README.md
    ├── brand.yaml
    ├── sources.yaml
    ├── rules/
    ├── examples/
    ├── evals/
    └── article/
```

## Conventions

Chaque outil autonome doit :

- vivre dans son propre sous-dossier ;
- avoir un README local avec un démarrage rapide ;
- séparer la documentation humaine des données structurées ;
- documenter ses sources, versions et licences ;
- fournir des exemples réutilisables ;
- signaler clairement les étapes qui nécessitent un jugement humain.

### Markdown et YAML

- Markdown sert à expliquer les décisions, les exemples, les contre-exemples et les procédures ;
- YAML sert aux métadonnées, règles, assertions, sources et configurations validables ;
- les deux formats doivent conserver des identifiants et des versions cohérents.

## Ajouter un outil

Créer un dossier autonome contenant au minimum :

```text
nouvel-outil/
├── README.md
├── LICENSE.md
└── examples/
```

Ajouter ensuite l’outil dans la section « Outils disponibles » de ce README.

Les nouvelles contributions doivent éviter les données confidentielles, les assets non autorisés et les affirmations non sourcées.

## Licence

Chaque outil précise sa propre licence dans son dossier. Le [Brand Brain Evaluation Lab](brand-brain-evaluation-lab/LICENSE.md) propose une licence Creative Commons Attribution 4.0 pour sa documentation, ses exemples et ses cas de test.

Les marques, logos, personnes, images, textes tiers et assets ajoutés par des contributeurs restent soumis à leurs propres droits.

## Maintien du repository

Les évolutions importantes doivent mettre à jour :

- le README de l’outil concerné ;
- le changelog ;
- les exemples et cas de test concernés ;
- les versions et références croisées ;
- les conditions de licence si le périmètre change.

