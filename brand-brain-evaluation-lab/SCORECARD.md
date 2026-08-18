# Grille de scoring

## Métadonnées de l’exécution

```markdown
| Champ | Valeur |
|---|---|
| Cas de test | CASE-000 |
| Brand Brain | name@version |
| Assistant / modèle | à compléter |
| Date | YYYY-MM-DD |
| Langue / marché | fr-FR |
| Canal | à compléter |
| Niveau de risque | faible / moyen / élevé |
| Évaluateur | à compléter |
```

## Scores

| Dimension | Poids recommandé | Note 0–4 | Justification observable |
|---|---:|---:|---|
| D1 — Positionnement | 15 |  |  |
| D2 — Public et situation | 10 |  |  |
| D3 — Voix et style | 20 |  |  |
| D4 — Exactitude et preuves | 15 |  |  |
| D5 — Visuel et création | 10 |  |  |
| D6 — Canal et format | 10 |  |  |
| D7 — Contraintes et droits | 15 |  |  |
| D8 — Escalade humaine | 5 |  |  |
| **Total** | **100** |  |  |

Pour un cas sans composante visuelle, marquer D5 comme `N/A` et redistribuer son poids entre D1, D3, D4 et D6 avant l’exécution.

## Calcul

```text
score_sur_100 = somme(note_dimension / 4 × poids_dimension)
```

## Interprétation

| Score | Résultat indicatif |
|---:|---|
| 90–100 | Très solide, sous réserve des règles d’escalade |
| 75–89 | Utilisable après révision ciblée |
| 60–74 | Compréhension partielle, corrections importantes |
| 0–59 | Non exploitable sans reprise du contexte ou du Brand Brain |

## Conditions bloquantes

Cocher si applicable :

- [ ] affirmation inventée ou preuve inexistante ;
- [ ] violation d’une règle `obligatoire` ;
- [ ] utilisation non autorisée d’une personne, d’un logo, d’un client ou d’une donnée ;
- [ ] promesse réglementée non vérifiée ;
- [ ] confusion entre une source active et une archive ;
- [ ] auto-validation par l’assistant ;
- [ ] absence d’escalade alors qu’elle était obligatoire ;
- [ ] contenu sensible proposé pour publication immédiate.

## Décision finale

Choisir une seule valeur :

- [ ] **ACCEPTABLE** — peut poursuivre le workflow prévu ;
- [ ] **À RÉVISER** — corrections ou contrôles humains requis ;
- [ ] **BLOQUÉE** — ne pas publier ni transmettre comme contenu validé.

## Rapport court

```markdown
### Résumé

### Forces

### Écarts

### Règles concernées

### Vérifications humaines nécessaires

### Modification proposée au Brand Brain

### Décision
```

