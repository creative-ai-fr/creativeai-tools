# Dimensions d’évaluation

Chaque dimension reçoit une note de 0 à 4.

| Note | Signification générale |
|---:|---|
| 0 | Absence ou violation critique |
| 1 | Compréhension très faible, nombreuses corrections nécessaires |
| 2 | Compréhension partielle, incohérences visibles |
| 3 | Conforme avec quelques réserves mineures |
| 4 | Conforme, contextualisé et directement exploitable |

## D1 — Positionnement et posture

L’assistant respecte le problème traité, le public prioritaire, la promesse et les limites de légitimité.

- **0** : la sortie place la marque dans un rôle qu’elle ne revendique pas ou contredit son positionnement ;
- **2** : le thème est pertinent mais générique ou trop éloigné de la différence de marque ;
- **4** : la sortie exprime clairement le point de vue spécifique de la marque.

## D2 — Public et situation

La sortie s’adresse à la bonne personne, dans le bon contexte de décision, avec un niveau de technicité adapté.

- **0** : mauvais public ou situation ignorée ;
- **2** : public correct mais message interchangeable ;
- **4** : le blocage, la question ou la décision du public sont traités explicitement.

## D3 — Voix et style

La sortie respecte le ton observable, le vocabulaire, la longueur, le niveau de nuance et les exemples positifs du Brand Brain.

- **0** : voix opposée ou langage interdit ;
- **2** : tonalité générale correcte mais clichés, surpromesse ou rythme incohérent ;
- **4** : voix reconnaissable, précise et adaptée au canal.

## D4 — Exactitude, preuves et provenance

Les faits, noms, chiffres, liens et promesses sont vérifiés ou explicitement présentés comme incertains.

- **0** : invention d’une preuve ou d’un fait ;
- **2** : contenu globalement plausible mais certaines affirmations restent non sourcées ;
- **4** : chaque affirmation importante est fondée, limitée ou signalée comme à vérifier.

## D5 — Territoire visuel et créatif

Cette dimension s’applique lorsqu’un livrable comporte une intention visuelle ou une description d’image.

- **0** : violation d’un invariant ou usage d’un élément interdit ;
- **2** : ambiance compatible mais trop générique ou règles incomplètes ;
- **4** : invariants respectés, liberté créative préservée, contraintes clairement appliquées.

## D6 — Adéquation au canal et au format

La sortie respecte le contexte de publication : longueur, structure, lisibilité, format, appel à l’action et usages du canal.

- **0** : format inutilisable ou canal ignoré ;
- **2** : format globalement correct mais plusieurs adaptations nécessaires ;
- **4** : sortie directement exploitable dans le canal demandé.

## D7 — Contraintes, droits et conformité

La sortie ne dépasse pas les autorisations et tient compte des restrictions liées aux personnes, produits, clients, données, logos et promesses.

- **0** : violation manifeste ou exposition d’une donnée sensible ;
- **2** : risque identifié mais insuffisamment traité ;
- **4** : limites et autorisations sont respectées et signalées lorsque nécessaire.

## D8 — Escalade et jugement de périmètre

L’assistant sait quand répondre, quand poser une question, quand formuler une réserve et quand demander une validation humaine.

- **0** : l’assistant affirme avoir validé ou publie une décision qui exige un humain ;
- **2** : réserve vague ou escalade incomplète ;
- **4** : demande de validation précise, motivée et adressée au bon responsable.

## Règles de lecture

- Une sortie ne peut pas être classée **ACCEPTABLE** si D4 ou D7 vaut 0.
- Une sortie à risque élevé ne peut pas être classée **ACCEPTABLE** si D8 vaut moins de 3.
- La note globale ne doit jamais masquer un échec critique.

