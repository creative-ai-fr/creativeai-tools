# Charte du projet

## Mission

Créer une base de référence ouverte pour évaluer la fidélité, la vérifiabilité et la gouvernance des assistants IA lorsqu’ils utilisent un Brand Brain.

## Problème

Les évaluations de génération de contenu mesurent souvent la fluidité, la préférence ou la similarité. Elles mesurent moins bien :

- la compréhension du positionnement ;
- la distinction entre règle obligatoire et préférence ;
- la gestion des sources obsolètes ou contradictoires ;
- le respect des droits et des restrictions ;
- la capacité à refuser, signaler une incertitude ou demander un arbitrage.

Une sortie peut donc être élégante, cohérente en apparence et pourtant dangereuse pour la marque.

## Hypothèse

Un protocole ouvert, composé de cas réalistes, de critères observables et de règles d’escalade, permettra de comparer plus utilement :

- plusieurs modèles ;
- plusieurs outils ou agents ;
- plusieurs versions d’un même Brand Brain ;
- plusieurs configurations de récupération de sources ;
- une production assistée par IA et une production humaine de référence.

## Principes

### 1. La fidélité précède la créativité

La créativité est évaluée après la conformité au positionnement, aux preuves et aux contraintes.

### 2. Les tests doivent révéler les erreurs plausibles

Un cas de test doit contenir au moins une ambiguïté, une contrainte ou une décision observable. Les tests trop faciles ne sont pas utiles.

### 3. Les faits et la voix sont séparés

Une sortie peut avoir la bonne voix mais contenir une affirmation fausse. Les deux dimensions doivent recevoir des scores distincts.

### 4. L’incertitude est un comportement attendu

Dans certains cas, la meilleure sortie est une question, un refus partiel ou une demande de validation.

### 5. L’évaluation doit être reproductible sans prétendre être absolue

Chaque résultat doit préciser son contexte : Brand Brain, modèle, date, langue, canal, risque et procédure de notation.

## Objectifs de la version 0.1

- définir un format de Brand Brain lisible en Markdown ;
- fournir huit dimensions d’évaluation ;
- proposer une grille de notation de 0 à 4 ;
- documenter les conditions d’escalade humaine ;
- publier trois cas de test fictifs et réutilisables ;
- rendre chaque résultat lisible par un humain avant toute automatisation.

## Hors périmètre initial

- entraînement ou fine-tuning d’un modèle ;
- comparaison commerciale de fournisseurs ;
- notation automatique de la “beauté” d’une campagne ;
- analyse biométrique ou identification de personnes ;
- validation juridique automatique.

## Critères de réussite

Le projet sera considéré comme utile lorsqu’une équipe externe pourra :

1. charger le Brand Brain en moins de quelques minutes ;
2. exécuter les cas de test avec un assistant de son choix ;
3. comprendre pourquoi une sortie a perdu des points ;
4. repérer les cas qui nécessitent une validation humaine ;
5. proposer un nouveau cas de test sans modifier la structure du dépôt.

