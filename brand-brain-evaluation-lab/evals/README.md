# Dossier `evals/`

Ce dossier accueille les séries d’évaluation et les rapports d’exécution.

## Convention recommandée

```text
evals/
├── README.md
├── cases/
│   ├── CASE-001.yaml       # données structurées
│   ├── CASE-002.yaml
│   └── CASE-003.yaml
├── runs/
│   └── RUN-001.yaml        # configuration d’une série
├── 2026-08-18-lumen-v0.1/
│   ├── RUN.md
│   ├── CASE-001-OUTPUT.md
│   ├── CASE-002-OUTPUT.md
│   └── SUMMARY.md
└── fixtures/
    └── sources.md
```

Les fichiers `cases/*.yaml` constituent la couche structurée des cas de test. Les fichiers `examples/CASE-*.md` restent leurs versions narratives et pédagogiques.

Les fichiers `runs/*.yaml` décrivent les conditions communes d’une exécution : assistant, modèle, date, langue, outils et cas utilisés.

## `RUN.md`

Documenter l’environnement commun à toute la série :

- Brand Brain et commit ou version ;
- modèle ou assistant ;
- outils et connecteurs ;
- paramètres ;
- langue, marché et fuseau horaire ;
- date d’exécution ;
- évaluateurs ;
- éventuelles limites connues.

## Fichier de sortie d’un cas

Conserver :

1. le prompt exact ;
2. la sortie brute ;
3. les erreurs ou avertissements de l’assistant ;
4. la scorecard complétée ;
5. la décision d’escalade ;
6. les corrections humaines, dans une section séparée.

Les résultats peuvent ensuite être ajoutés au fichier YAML de la série dans `results`, mais la sortie brute et la justification détaillée doivent rester consultables en Markdown.

## `SUMMARY.md`

Présenter les résultats par dimension, pas seulement par moyenne :

| Cas | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Décision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| CASE-001 |  |  |  |  | N/A |  |  |  |  |
| CASE-002 |  | N/A |  |  | N/A | N/A |  |  |  |
| CASE-003 |  | N/A |  |  |  | N/A |  |  |  |

## Confidentialité

Ne jamais committer dans ce dossier :

- prompts ou sources confidentiels ;
- données personnelles ;
- clés API ou journaux contenant des secrets ;
- assets dont les droits ne sont pas documentés ;
- sorties contenant des informations client non anonymisées.
