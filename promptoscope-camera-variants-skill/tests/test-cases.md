# Cas de test — Promptoscope Camera Variants

Utiliser uniquement des images autorisées. Le Skill doit fonctionner avec la vision native de ChatGPT et ne doit jamais récupérer une URL d’image.

## Cas positifs

1. **Trois vues par défaut** — joindre une image et demander une vue source, une vue trois-quarts gauche et une vue élevée. Attendu : source inchangée et trois sidecars A/B/C avec `0/0/medium`, `-45/0/medium` et `0/+45/medium`.
2. **Coordonnées explicites** — demander `azimut +90°`, `élévation -15°`, `distance wide`. Attendu : les valeurs sont recopiées exactement dans le sidecar.
3. **Préservation** — demander de garder le sujet, la lumière et la palette tout en changeant l’angle. Attendu : les invariants apparaissent dans `preserve` et le JSON source n’est pas modifié.
4. **Plusieurs variantes** — demander quatre points de vue nommés. Attendu : un `variant_id` distinct par sidecar et aucun mélange des objets.
5. **Limites valides** — demander `azimut -180°`, `élévation +90°`, `distance close`. Attendu : les bornes sont acceptées et les trois champs restent typés correctement.

## Cas négatifs

1. **Aucune image** — demander une variante sans pièce jointe. Attendu : demander l’image et ne produire aucun JSON inventé.
2. **Demande image-to-prompt générique** — demander uniquement un prompt et un JSON sans changement de caméra. Attendu : laisser cette demande au Skill `promptoscope-image-to-prompt`.
3. **Certitude 3D** — demander une reconstruction exacte d’une face cachée. Attendu : expliquer que les surfaces invisibles sont inférées et ne sont pas mesurées.

## Contrôles

- Le JSON source conserve ses 13 clés et son ordre.
- Chaque sidecar conserve ses 6 clés et son ordre.
- `azimuth_deg` est compris entre -180 et 180.
- `elevation_deg` est compris entre -90 et 90.
- `distance` vaut uniquement `close`, `medium` ou `wide`.
- Aucune image n’est récupérée depuis une URL.
