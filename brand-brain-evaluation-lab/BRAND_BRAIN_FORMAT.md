# Format Markdown d’un Brand Brain

## Intention

Ce format donne une structure commune à un Brand Brain sans imposer une base de données, un outil propriétaire ou un modèle particulier.

Le Markdown est la source lisible par les humains. La couche YAML fournie dans ce dépôt et les futurs adaptateurs JSON ou MCP ne doivent pas supprimer le raisonnement et les exemples visibles dans le fichier source.

Dans ce dépôt, [`brand.yaml`](brand.yaml) est la représentation structurée du Brand Brain fictif. [`examples/BRAND.md`](examples/BRAND.md) conserve la version narrative et les exemples détaillés.

## Règle de séparation

Utiliser Markdown pour :

- expliquer une décision ;
- donner du contexte ;
- montrer un exemple ou un contre-exemple ;
- documenter une exception ;
- guider une contribution humaine.

Utiliser YAML pour :

- les identifiants, versions et statuts ;
- les règles qui doivent être filtrées ou testées ;
- les sources et leurs dates ;
- les assertions d’un cas de test ;
- les configurations d’exécution ;
- les seuils de score et les décisions attendues.

Éviter de maintenir deux textes narratifs différents. Le YAML doit pointer vers le Markdown avec `human_reference` ou `reference` lorsqu’une explication complète est nécessaire.

## En-tête recommandé

```yaml
---
name: Lumen Commons
id: lumen-commons
version: 0.1.0
status: active
language: fr-FR
owner: brand@example.org
last_verified: 2026-08-18
effective_from: 2026-08-18
---
```

## Sections obligatoires

Un Brand Brain doit contenir :

1. posture et positionnement ;
2. publics et situations ;
3. voix et style ;
4. territoires et formats ;
5. invariants visuels ;
6. contraintes, droits et interdits ;
7. sources et versions ;
8. validation humaine.

## Fichiers structurés associés

| Fichier | Rôle |
|---|---|
| `brand.yaml` | identité, publics, voix, territoires, gouvernance et validation |
| `sources.yaml` | registre versionné des sources |
| `rules/editorial.yaml` | règles de voix et de vocabulaire |
| `rules/governance.yaml` | règles de publication, droits et escalade |
| `evals/cases/*.yaml` | prompts, assertions, risques et scores minimaux |
| `evals/runs/*.yaml` | configuration d’une série d’exécution |

## Format d’une règle

Chaque règle importante doit suivre ce modèle :

```markdown
## RULE-001 — Expliquer avant de convaincre

| Champ | Valeur |
|---|---|
| Type | éditoriale |
| Périmètre | articles pédagogiques, posts LinkedIn |
| Priorité | obligatoire |
| Statut | active |
| Propriétaire | équipe éditoriale |
| Vérifiée le | 2026-08-18 |
| Source | DEC-004 |

### Règle
Présenter le problème ou la situation avant la promesse.

### Exemple validé
Décrire d’abord la difficulté rencontrée par l’équipe, puis expliquer comment la méthode proposée réduit cette difficulté.

### Contre-exemple
Commencer par « La solution la plus puissante du marché » sans preuve ni contexte.

### Contrôle
Le lecteur comprend-il le problème avant de recevoir la promesse ?

### Escalade
Demander une validation humaine si la promesse implique un résultat chiffré ou réglementé.
```

## Priorités

Utiliser trois niveaux :

- **obligatoire** : la violation rend la sortie non conforme ;
- **recommandé** : la règle améliore la cohérence mais peut être adaptée ;
- **exploratoire** : piste créative, à ne pas confondre avec une contrainte.

## Statuts de source

Chaque source doit être marquée :

- **active** : applicable à la date du test ;
- **à_revoir** : utilisable avec prudence, vérification requise ;
- **archivée** : conservée pour l’historique, non applicable par défaut.

## Registre des sources

```markdown
| ID | Source | Propriétaire | Version | Vérifiée le | Effet le | Statut | Périmètre |
|---|---|---|---|---|---|---|---|
| DEC-004 | Décision éditoriale | Équipe éditoriale | 2 | 2026-08-18 | 2026-08-18 | active | contenu FR |
| LEG-002 | Note juridique | Juridique | 1 | 2026-08-10 | 2026-08-10 | à_revoir | claims produit |
```

## Gestion des contradictions

Lorsqu’une contradiction est détectée :

1. comparer le périmètre ;
2. comparer le statut ;
3. comparer la date d’effet ;
4. comparer la priorité ;
5. si le conflit persiste, demander un arbitrage.

L’assistant ne doit pas inventer une règle de résolution absente du Brand Brain.
