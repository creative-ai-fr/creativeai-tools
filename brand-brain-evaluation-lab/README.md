# Brand Brain Evaluation Lab

Un laboratoire open source pour mesurer si un assistant IA respecte réellement une marque — et pas seulement s’il produit un résultat plausible.

Ce module est destiné au repository [creative-ai-fr/creativeai-tools](https://github.com/creative-ai-fr/creativeai-tools) et doit être placé dans `brand-brain-evaluation-lab/`.

## Pourquoi ce projet existe

Un Brand Brain utile doit permettre à une équipe de vérifier quatre choses :

1. l’assistant a compris ce que la marque défend ;
2. il s’exprime avec la bonne voix, pour le bon public et le bon canal ;
3. il n’invente pas de preuves, ne mélange pas les versions et respecte les droits ;
4. il sait demander une validation humaine lorsque la décision dépasse son périmètre.

Le laboratoire fournit les formats, cas de test, critères et procédures nécessaires pour comparer des assistants, des modèles ou des versions d’un même Brand Brain.

## Principe fondateur

> Une sortie de marque n’est pas “bonne” parce qu’elle semble professionnelle. Elle est bonne lorsqu’elle est fidèle, vérifiable, contextualisée et correctement escaladée.

## Ce que contient ce dépôt

```text
brand-brain-evaluation-lab/
├── README.md
├── CHARTER.md
├── PROTOCOL.md
├── BRAND_BRAIN_FORMAT.md
├── brand.yaml
├── sources.yaml
├── rules/
│   ├── editorial.yaml
│   └── governance.yaml
├── EVALUATION_DIMENSIONS.md
├── SCORECARD.md
├── HUMAN_ESCALATION.md
├── TEST_CASE_TEMPLATE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── GITHUB_RELEASE.md
├── LICENSE.md
├── .gitignore
├── article/
│   ├── brand-brain-evaluation-lab-block.html
│   ├── brand-brain-evaluation-lab-copy.md
│   ├── installation-and-test-block.html
│   └── creative-memory-sprint-cta-block.html
├── examples/
│   ├── BRAND.md
│   ├── CASE-001.md
│   ├── CASE-002.md
│   └── CASE-003.md
└── evals/
    ├── README.md
    ├── cases/
    │   ├── CASE-001.yaml
    │   ├── CASE-002.yaml
    │   └── CASE-003.yaml
    └── runs/
        └── RUN-001.yaml
```

## Répartition Markdown / YAML

Le dépôt utilise une architecture hybride :

- Markdown contient le raisonnement, les exemples, les contre-exemples et la documentation lisible par les humains ;
- YAML contient les métadonnées, règles, assertions et paramètres destinés à la validation ou à l’automatisation.

Les fichiers YAML font référence aux fichiers Markdown correspondants avec `human_reference`. Le Markdown reste la référence éditoriale ; le YAML est la représentation structurée destinée aux outils.

## Démarrage rapide

### 1. Charger un Brand Brain

Utiliser le Brand Brain fictif fourni dans [`examples/BRAND.md`](examples/BRAND.md) et sa représentation structurée [`brand.yaml`](brand.yaml), ou remplacer ces fichiers par le référentiel d’une marque dont vous avez les droits.

### 2. Choisir un cas de test

Commencer par [`examples/CASE-001.md`](examples/CASE-001.md) et [`evals/cases/CASE-001.yaml`](evals/cases/CASE-001.yaml), qui testent une production éditoriale à risque faible, puis utiliser les cas 002 et 003 pour les situations nécessitant une escalade.

### 3. Produire une sortie

Conserver dans un dossier d’exécution :

- la version exacte du Brand Brain ;
- le cas de test ;
- le modèle ou l’assistant utilisé ;
- les instructions fournies ;
- la sortie brute, sans correction préalable ;
- la date, la langue, le canal et les paramètres importants.

### 4. Évaluer

Appliquer les dimensions décrites dans [`EVALUATION_DIMENSIONS.md`](EVALUATION_DIMENSIONS.md), puis reporter les résultats dans [`SCORECARD.md`](SCORECARD.md).

### 5. Décider

Une note élevée ne remplace pas une décision humaine. Appliquer les règles de [`HUMAN_ESCALATION.md`](HUMAN_ESCALATION.md) avant de déclarer une sortie publiable.

## Périmètre de la version 0.2

La version actuelle conserve une approche Markdown-first et ajoute une couche YAML structurée. Elle couvre :

- le positionnement et la posture ;
- les publics et les situations ;
- la voix et le style ;
- les territoires de contenu ;
- les sources et les preuves ;
- les contraintes, les droits et les interdits ;
- la validation humaine ;
- la reproductibilité des évaluations.

Les extensions prévues sont décrites dans [`CHARTER.md`](CHARTER.md) : visuels, audio, connecteurs MCP, exécution automatisée et tableaux de comparaison.

## Ce que ce projet ne prétend pas faire

- certifier juridiquement une marque ou une campagne ;
- remplacer un directeur de marque, un rédacteur ou un conseil juridique ;
- prouver qu’un modèle est “sûr” dans l’absolu ;
- attribuer une note universelle indépendante du contexte ;
- publier automatiquement un contenu sensible.

## Statut

Prototype de spécification et de corpus de tests. Les règles sont proposées pour discussion et doivent être adaptées au secteur, au marché, au niveau de risque et aux responsabilités de chaque organisation.

## Références de conception

Le projet reprend plusieurs principes désormais visibles dans l’écosystème des Brand Brains : formats lisibles par machine, règles contextualisées, tokens séparés du raisonnement éditorial, provenance des sources et validation structurée.

- [DZNE — AI & Brand Guidelines](https://www.dzne.de/en/ai-brand/)
- [BrandCodex — MRBS Specification](https://brandcodex.org/specification)
- [BRAND.md](https://github.com/caiopizzol/brand.md)
- [DESIGN.md](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md)
- [JSON Schema](https://json-schema.org/specification)
- [Design Tokens Community Group](https://www.designtokens.org/tr/2025.10/)

## Licence proposée

Pour une publication publique :

- documentation, exemples et cas de test : CC BY 4.0 ou CC0 selon le besoin d’attribution ;
- scripts, validateurs et adaptateurs : MIT ou Apache-2.0 ;
- assets de marque : uniquement sous licence explicite ou avec autorisation.
