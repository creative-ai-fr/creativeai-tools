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

### Promptoscope ChatGPT Skill

Un Skill conversationnel qui transforme une image jointe à ChatGPT en **recette visuelle**, **prompt de génération en anglais** et **JSON Promptoscope v1.0**. Il s’appuie sur la vision native de ChatGPT et la méthode Promptoscope ; il ne requiert ni Gemini, ni API externe, ni serveur MCP, ni backend Promptoscope.

➡️ [Découvrir, installer et tester le Promptoscope ChatGPT Skill](promptoscope-chatgpt-skill/)

### Brand Guardian Skills

Deux Skills composables construisent un profil de marque sourcé puis auditent un contenu à partir de ce profil. Le `brand-profile-builder` distingue règles explicites, principes inférés, patterns, exemples isolés et inconnues. Le `brand-guardian` cite les écarts confirmés, signale les conflits non résolus et propose des corrections minimales sans attribuer de score global.

➡️ [Découvrir, installer et tester les Brand Guardian Skills](brand-guardian-skills/)

### Creative Director Skill

Un Skill de direction créative pour analyser une idée de campagne à partir d’un brief, la challenger sur les plans stratégique, créatif et production/réception, puis proposer des pistes d’amélioration concrètes.

➡️ [Lire le guide et télécharger l’archive Creative Director](creative-director-skill/) · [ZIP v0.1.0](creative-director-skill/creative-director-skill-v0.1.0.zip)

### Visual Consistency Skill

Un Skill qui compare plusieurs visuels, distingue les invariants des variations intentionnelles et formule des corrections ciblées pour chaque image.

➡️ [Lire le guide et télécharger l’archive Visual Consistency](visual-consistency-skill/) · [ZIP v0.1.0](visual-consistency-skill/visual-consistency-skill-v0.1.0.zip)

## Démarrage rapide

```bash
git clone https://github.com/creative-ai-fr/creativeai-tools.git
cd creativeai-tools
```

Pour le Brand Brain Evaluation Lab :

1. lisez [`README.md`](brand-brain-evaluation-lab/README.md) ;
2. consultez [`brand.yaml`](brand-brain-evaluation-lab/brand.yaml) ;
3. examinez [`examples/BRAND.md`](brand-brain-evaluation-lab/examples/BRAND.md) ;
4. lancez le cas [`CASE-001.yaml`](brand-brain-evaluation-lab/evals/cases/CASE-001.yaml) ;
5. utilisez les cas 002 et 003 pour tester les demandes nécessitant une escalade humaine.

Pour les Brand Guardian Skills, consultez [`brand-guardian-skills/README.md`](brand-guardian-skills/README.md), copiez les deux dossiers sous `brand-guardian-skills/skills/` dans le répertoire `skills/` de votre environnement, puis lancez la suite déterministe indiquée dans ce README. Les 15 scénarios comportementaux et leur replay aveugle sont documentés dans `brand-guardian-skills/tests/`.

Pour Promptoscope, téléchargez l’archive Skill depuis la [dernière Release](https://github.com/creative-ai-fr/creativeai-tools/releases/latest), puis importez-la dans la gestion des Skills de ChatGPT. Les essais manuels sont décrits dans [`test-cases.md`](promptoscope-chatgpt-skill/tests/test-cases.md).

Pour Creative Director et Visual Consistency, téléchargez l’archive liée dans chaque dossier, décompressez-la puis copiez le dossier du Skill (`creative-director/` ou `visual-consistency/`) dans le répertoire `skills/` de votre environnement.

Le Brand Brain peut être utilisé avec un assistant capable de lire des fichiers, notamment ChatGPT Work ou Claude Cowork. Les procédures détaillées figurent dans [`installation-and-test-block.html`](brand-brain-evaluation-lab/article/installation-and-test-block.html).

## Structure du repository

```text
creativeai-tools/
├── README.md
├── brand-brain-evaluation-lab/
├── brand-guardian-skills/
│   ├── README.md
│   ├── LICENSE.md
│   ├── CHANGELOG.md
│   ├── skills/
│   ├── examples/
│   └── tests/
├── creative-director-skill/
│   ├── README.md
│   ├── creative-director-skill-v0.1.0.zip
│   └── skill/creative-director/SKILL.md
├── promptoscope-chatgpt-skill/
│   ├── README.md
│   ├── LICENSE.md
│   ├── CHANGELOG.md
│   ├── PRIVACY.md
│   ├── skill/promptoscope-image-to-prompt/
│   ├── examples/
│   └── tests/
└── visual-consistency-skill/
    ├── README.md
    ├── visual-consistency-skill-v0.1.0.zip
    └── skill/visual-consistency/SKILL.md
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

Chaque outil précise sa propre licence dans son dossier. Le [Brand Brain Evaluation Lab](brand-brain-evaluation-lab/LICENSE.md), le [Promptoscope ChatGPT Skill](promptoscope-chatgpt-skill/LICENSE.md) et les [Brand Guardian Skills](brand-guardian-skills/LICENSE.md) proposent une licence Creative Commons Attribution 4.0 pour leurs contenus documentaires et exemples.

Les fichiers source fournis pour [Creative Director](creative-director-skill/) et [Visual Consistency](visual-consistency-skill/) ne précisent pas de licence ; aucune licence n’est déduite par défaut.

Les marques, logos, personnes, images, textes tiers et assets ajoutés par des contributeurs restent soumis à leurs propres droits.

## Maintien du repository

Les évolutions importantes doivent mettre à jour :

- le README de l’outil concerné ;
- le changelog ;
- les exemples et cas de test concernés ;
- les versions et références croisées ;
- les conditions de licence si le périmètre change.
