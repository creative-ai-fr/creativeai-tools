# Modèle de cas de test

Copier ce fichier dans `examples/` ou `evals/`, puis remplacer les valeurs entre crochets.

Pour un cas pédagogique, conserver ce modèle en Markdown dans `examples/`. Pour un cas destiné à une exécution automatisée, reporter ses champs structurés dans `evals/cases/CASE-000.yaml` et conserver ce fichier comme documentation humaine si nécessaire.

## Métadonnées

```yaml
---
id: CASE-000
title: "Titre court"
version: 0.1.0
status: draft
language: fr-FR
channel: article / social / email / visual / support
risk: low / medium / high
expected_escalation: auto_ok / review / block
dimensions: [D1, D2, D3, D4, D6, D7, D8]
---
```

## Objectif

Décrire le comportement que le cas doit mesurer. Un seul cas peut mesurer plusieurs dimensions, mais son objectif principal doit rester lisible.

## Contexte fourni à l’assistant

Décrire le brief accessible à l’assistant : objectif, public, canal, longueur, contraintes et sources autorisées.

## Demande utilisateur

```text
[Insérer ici le prompt exact soumis à l’assistant.]
```

## Pièges intentionnels

Documenter ce qui rend le cas intéressant :

- source absente ;
- règle en conflit ;
- mot interdit mais tentant ;
- preuve trop ancienne ;
- demande de publication immédiate ;
- contrainte de droits ;
- ambiguïté sur le public ou le canal.

## Comportements attendus

- [ ] l’assistant identifie le bon public ;
- [ ] l’assistant applique les règles pertinentes ;
- [ ] l’assistant ne fabrique pas de preuve ;
- [ ] l’assistant distingue une recommandation d’une obligation ;
- [ ] l’assistant respecte le format ;
- [ ] l’assistant demande une validation si nécessaire.

## Assertions

Écrire des assertions vérifiables, par exemple :

- le mot `révolutionnaire` n’apparaît pas ;
- aucune statistique n’est ajoutée sans source ;
- la sortie contient une demande de validation humaine ;
- le texte ne dépasse pas 600 caractères ;
- la source `SOURCE-003` est citée ou explicitement déclarée manquante.

## Grille attendue

| Dimension | Attente minimale | Motif |
|---|---:|---|
| D1 | 3 | Le positionnement doit rester identifiable |
| D3 | 3 | La voix est le principal objet du test |
| D4 | 4 | Aucune invention tolérée |
| D7 | 3 | Les restrictions doivent être respectées |
| D8 | 3 | L’escalade doit être explicite si nécessaire |

## Sortie de référence

Décrire le comportement attendu sans imposer une formulation unique. Le laboratoire évalue une décision et ses propriétés, pas une phrase exacte.

## Notes de maintenance

- Pourquoi ce cas existe-t-il ?
- Quelle erreur réelle ou plausible couvre-t-il ?
- Quelle règle du Brand Brain le cas met-il à l’épreuve ?
- Quand faudra-t-il le revoir ?
