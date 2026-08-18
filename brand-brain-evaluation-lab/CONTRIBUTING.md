# Contribuer

Les contributions peuvent prendre la forme de nouveaux cas de test, de corrections de règles, d’exemples, de traductions ou d’outils d’exécution.

## Ajouter un cas de test

1. Copier [`TEST_CASE_TEMPLATE.md`](TEST_CASE_TEMPLATE.md).
2. Donner un identifiant unique.
3. Décrire le comportement attendu, pas seulement une réponse idéale.
4. Ajouter au moins une assertion observable.
5. Indiquer le niveau de risque et l’escalade attendue.
6. Vérifier que le cas ne contient pas de données personnelles, confidentielles ou sous copyright non autorisé.
7. Ajouter une note de maintenance.

Pour rendre le cas exploitable par un validateur, ajouter également sa représentation structurée dans `evals/cases/`. Le fichier YAML doit conserver le même identifiant et référencer la version Markdown avec `human_reference`.

## Qualité attendue

Un bon cas de test est :

- réaliste ;
- suffisamment difficile pour révéler une erreur plausible ;
- indépendant d’un fournisseur précis ;
- évaluable par plusieurs personnes ;
- explicite sur les règles et les sources concernées.

## Ajouter une règle

Toute nouvelle règle doit comporter :

- un identifiant stable ;
- un périmètre ;
- une priorité ;
- un exemple ;
- un contre-exemple ;
- une question de contrôle ;
- un propriétaire ;
- une source et une date de vérification.

Les règles destinées à être filtrées ou testées doivent aussi être représentées dans `rules/*.yaml`. Le YAML contient les champs structurés ; le Markdown conserve le contexte et le raisonnement.

## Discussion des scores

Une contestation de score doit citer le passage évalué, la dimension concernée et la règle du Brand Brain utilisée. Les jugements de goût non reliés à un critère observable ne suffisent pas.

## Code de conduite éditorial

Les désaccords sont formulés sur les règles, les preuves et les décisions — jamais sur les personnes. Les contributions qui exposent des informations confidentielles ou des assets sans droit doivent être retirées du dépôt.
