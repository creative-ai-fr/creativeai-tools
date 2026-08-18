# Protocole d’évaluation

## Vue d’ensemble

Chaque évaluation suit le même cycle :

```text
Brand Brain + cas de test
          ↓
Configuration documentée
          ↓
Production brute
          ↓
Contrôle des faits et des contraintes
          ↓
Notation par dimensions
          ↓
Décision d’escalade
          ↓
Rapport reproductible
```

## Étape 1 — Préparer le contexte

Documenter :

- identifiant et version du Brand Brain ;
- identifiant et version du cas de test ;
- nom et version du modèle ou de l’assistant ;
- outil utilisé et éventuels connecteurs ;
- langue et marché ;
- canal et format demandé ;
- niveau de risque ;
- date et fuseau horaire ;
- paramètres pertinents, notamment température ou mode de raisonnement s’ils sont disponibles.

Ne pas modifier le Brand Brain pendant une série de tests. Toute modification démarre une nouvelle version.

## Étape 2 — Exécuter la demande

Utiliser le prompt fourni dans le cas de test. Si un assistant ajoute automatiquement des instructions, les conserver dans le rapport.

La sortie doit être enregistrée telle qu’elle a été générée. Une correction humaine ne doit jamais être mélangée à la sortie évaluée.

## Étape 3 — Vérifier les éléments bloquants

Avant de calculer une note globale, rechercher :

- une affirmation inventée ou non sourcée ;
- une violation d’un interdit explicite ;
- un usage non autorisé de logo, personne, client ou donnée personnelle ;
- une promesse réglementée non vérifiée ;
- une confusion entre une archive et une règle active ;
- une publication proposée alors qu’une validation humaine est obligatoire.

Un seul élément bloquant peut rendre la sortie non publiable, même si sa note stylistique est élevée.

## Étape 4 — Noter la sortie

Attribuer à chaque dimension une note entière de 0 à 4 selon [`EVALUATION_DIMENSIONS.md`](EVALUATION_DIMENSIONS.md).

La notation doit s’appuyer sur des éléments observables de la sortie. Éviter les commentaires vagues comme “ça ne ressemble pas assez à la marque”.

Préférer :

> Le texte utilise une promesse absolue alors que la règle `CLAIM-002` exige une preuve ou une formulation prudente.

## Étape 5 — Décider de l’escalade

Appliquer [`HUMAN_ESCALATION.md`](HUMAN_ESCALATION.md). Une sortie peut être :

- **ACCEPTABLE** : aucune escalade obligatoire et seuil atteint ;
- **À RÉVISER** : correction ou vérification humaine nécessaire ;
- **BLOQUÉE** : interdiction, risque majeur ou absence d’information critique.

## Étape 6 — Rédiger le rapport

Chaque rapport doit contenir :

1. le contexte d’exécution ;
2. la sortie brute ;
3. les scores par dimension ;
4. les preuves de notation ;
5. les éventuels éléments bloquants ;
6. la décision d’escalade ;
7. les corrections proposées au Brand Brain.

## Reproductibilité minimale

Une exécution est considérée comme suffisamment documentée si une autre personne peut refaire le test avec :

- le même Brand Brain ;
- le même cas ;
- le même modèle ou une alternative explicitement indiquée ;
- le même contexte de langue, canal et risque ;
- la même grille de notation.

La reproductibilité ne garantit pas l’identité exacte des sorties générées. Elle garantit la traçabilité des conditions de comparaison.

## Comparaison entre assistants

Comparer les assistants uniquement sur des séries identiques de cas. Publier les résultats par dimension plutôt qu’une seule moyenne.

Une moyenne globale peut masquer un comportement critique : par exemple, une excellente voix de marque ne compense pas l’invention de preuves.

