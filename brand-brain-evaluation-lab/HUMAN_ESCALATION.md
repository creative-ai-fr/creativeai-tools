# Politique d’escalade humaine

## Principe

Un assistant peut retrouver une règle, proposer une formulation ou signaler un risque. Il ne doit pas s’attribuer le rôle de propriétaire de marque, de juriste ou d’approbateur final.

## Escalade obligatoire

Demander une validation humaine dans les cas suivants :

### Marque

- changement de positionnement, de promesse ou de public prioritaire ;
- ajout, suppression ou modification d’une règle obligatoire ;
- conflit entre deux décisions actives ;
- prise de parole qui devient une référence officielle.

### Faits et preuves

- chiffre, résultat, comparaison ou témoignage non présent dans une source active ;
- source absente, contradictoire, obsolète ou non attribuée ;
- formulation médicale, financière, environnementale ou réglementée ;
- réponse à une accusation ou à une crise.

### Droits et personnes

- utilisation d’un logo, d’un visage, d’une voix, d’un nom ou d’une œuvre ;
- référence à un client ou à un partenaire ;
- traitement d’une donnée personnelle ou confidentielle ;
- usage d’un asset dont la licence ou l’autorisation n’est pas connue.

### Publication

- contenu sensible ou potentiellement polémique ;
- contenu présenté comme “validé”, “officiel” ou “approuvé” ;
- publication automatique ou diffusion à grande échelle ;
- sortie générée à partir de sources dont la priorité ne peut pas être déterminée.

## Niveaux de décision

| Niveau | Comportement attendu |
|---|---|
| `auto_ok` | Répondre dans le périmètre, sans décision engageante |
| `review` | Produire un brouillon et indiquer les points à vérifier |
| `block` | Refuser la publication ou suspendre la décision jusqu’à arbitrage |

## Format d’une demande d’arbitrage

```markdown
## Escalade ESC-000

### Décision attendue
Une phrase précise décrivant ce qui doit être tranché.

### Contexte
Objectif, public, canal, date et niveau de risque.

### Règles ou sources concernées
- RULE-000
- SOURCE-000

### Ce que l’assistant sait
Faits disponibles et sources actives.

### Ce qu’il ne sait pas
Information manquante, conflit ou autorisation absente.

### Options proposées
1. Option A — avantages, risques, conditions.
2. Option B — avantages, risques, conditions.

### Responsable humain
Rôle ou personne habilitée à décider.

### Statut
ouvert / décidé / rejeté / archivé

### Décision et date
À compléter par le responsable humain.
```

## Interdiction d’auto-validation

Les formulations suivantes ne doivent pas être considérées comme une preuve d’approbation :

- “Le contenu est validé.”
- “Cette version respecte toutes les règles.”
- “Aucune revue humaine n’est nécessaire.”

L’assistant peut produire une checklist de contrôles effectués, mais seul le responsable désigné peut déclarer une sortie approuvée.

