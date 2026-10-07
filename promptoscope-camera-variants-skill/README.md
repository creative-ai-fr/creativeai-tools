# Promptoscope Camera Variants Skill

**Version : 1.5.0** · **Schéma source : Promptoscope v1.0** · **Format : Skill ChatGPT autonome**

Promptoscope Camera Variants crée des vues alternatives à partir d’une image jointe à ChatGPT. Le Skill conserve l’analyse Promptoscope source et produit un sidecar JSON distinct pour chaque angle demandé.

## Télécharger et installer

1. Téléchargez [le ZIP Promptoscope Camera Variants v1.5.0](https://github.com/creative-ai-fr/creativeai-tools/releases/latest/download/promptoscope-camera-variants-skill-v1.5.0.zip).
2. Dans ChatGPT, ouvrez la gestion des Skills et choisissez l’import depuis un fichier.
3. Sélectionnez le ZIP, puis joignez une image que vous êtes autorisé à partager.
4. Demandez par exemple : **« Génère trois vues : face, trois-quarts gauche et plongée, avec un JSON sidecar pour chaque vue. »**

La disponibilité de l’import dépend de l’offre ChatGPT, du déploiement du produit et des réglages de l’espace de travail.

## Ce que le Skill produit

- le JSON Promptoscope source conservé inchangé ;
- un sidecar JSON par point de vue ;
- trois paramètres caméra : `azimuth_deg`, `elevation_deg`, `distance` ;
- un prompt de variante en anglais ;
- une note sur les surfaces nouvellement visibles qui restent des hypothèses.

Le Skill ne remplace pas `promptoscope-image-to-prompt`. Il s’active uniquement lorsqu’un changement de caméra ou de point de vue est demandé.

## Architecture et limites

Image jointe dans ChatGPT → vision native de ChatGPT → analyse source Promptoscope → sidecars Camera Variants.

Le paquet contient des instructions, des références et deux schémas JSON. Il n’utilise ni Gemini, ni API externe, ni serveur MCP, ni backend Promptoscope, ni clé API, ni quota dédié. CreativeAI ne reçoit pas l’image par l’intermédiaire du Skill.

Une variante exprime une hypothèse de cadrage ; elle ne constitue pas une reconstruction 3D mesurée et ne garantit pas la fidélité des surfaces cachées.

## Schémas et références

- [SKILL.md](skill/promptoscope-camera-variants/SKILL.md)
- [Schéma source Promptoscope](skill/promptoscope-camera-variants/references/output-schema.json)
- [Schéma sidecar caméra](skill/promptoscope-camera-variants/references/camera-variant-schema.json)
- [Conventions azimut, élévation et distance](skill/promptoscope-camera-variants/references/camera-variants.md)
- [Exemple JSON](examples/sample-output.json)
- [Cas de test](tests/test-cases.md)

## Publication

Le ZIP importable est construit depuis `skill/promptoscope-camera-variants/` et joint à une GitHub Release. La procédure est documentée dans [RELEASING.md](RELEASING.md). La page produit est [Promptoscope — variantes de point de vue en JSON caméra](https://creativeai.fr/promptoscope-variantes-point-de-vue-json-camera/).

La notice de flux de données se trouve dans [PRIVACY.md](PRIVACY.md) et les contenus originaux sont proposés sous [CC BY 4.0](LICENSE.md).
