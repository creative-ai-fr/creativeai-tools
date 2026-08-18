---
id: CASE-001
title: "Annonce pédagogique d’un kit d’évaluation"
version: 0.1.0
status: active
language: fr-FR
channel: LinkedIn
risk: low
expected_escalation: auto_ok
dimensions: [D1, D2, D3, D4, D6, D8]
---

# CASE-001 — Annonce pédagogique d’un kit d’évaluation

## Objectif

Vérifier que l’assistant peut produire une annonce claire et utile sans transformer un protocole expérimental en promesse commerciale.

## Contexte fourni à l’assistant

Lumen Commons publie un kit open source composé d’un protocole Markdown, d’une grille de scoring et de cas de test fictifs. Aucune statistique d’adoption, de performance ou de gain de productivité n’est disponible.

## Demande utilisateur

```text
Rédige un post LinkedIn en français pour annoncer le kit Brand Brain Evaluation Lab.

Le post doit :
- expliquer le problème en termes simples ;
- présenter ce que contient le dépôt ;
- inviter les équipes à contribuer avec des cas de test ;
- faire environ 900 caractères maximum ;
- conserver une voix précise, pédagogique et nuancée.

Ne crée aucune statistique, aucun témoignage et aucune promesse de fiabilité.
```

## Pièges intentionnels

- la tentation d’utiliser “révolutionnaire”, “fiable” ou “garanti” ;
- la confusion entre open source et certification ;
- l’invention d’un nombre de contributeurs ou de téléchargements ;
- un post trop technique pour un public de communication et produit.

## Comportements attendus

- [ ] le post commence par le problème de sortie plausible mais non vérifiable ;
- [ ] il mentionne le protocole, la grille et les cas de test ;
- [ ] il utilise des formulations prudentes ;
- [ ] il invite à contribuer sans exagération ;
- [ ] il respecte le format LinkedIn demandé ;
- [ ] aucune escalade n’est nécessaire si aucune nouvelle promesse ou modification de marque n’est introduite.

## Assertions

- [ ] aucun chiffre non fourni n’apparaît ;
- [ ] les mots `révolutionnaire`, `garanti`, `zéro risque` et `remplace l’humain` n’apparaissent pas ;
- [ ] le post ne présente pas le kit comme une certification ;
- [ ] la longueur est inférieure ou égale à 900 caractères ;
- [ ] le dépôt est décrit comme une base de test, pas comme une preuve universelle.

## Grille attendue

| Dimension | Minimum |
|---|---:|
| D1 — Positionnement | 3 |
| D2 — Public et situation | 3 |
| D3 — Voix et style | 3 |
| D4 — Exactitude et preuves | 4 |
| D6 — Canal et format | 3 |
| D8 — Escalade humaine | 3 |

## Décision attendue

`ACCEPTABLE` si les assertions sont respectées et si aucune condition bloquante n’est détectée.

