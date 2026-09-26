# Publier une version

Ce guide concerne la distribution du Skill Promptoscope ChatGPT depuis creative-ai-fr/creativeai-tools.

## Avant chaque version

1. Mettre à jour les sources sous skill/promptoscope-image-to-prompt/.
2. Vérifier que le nom du Skill correspond au nom de son dossier et que les références mentionnées dans SKILL.md existent.
3. Si le format JSON change, mettre à jour ensemble le schéma, la méthode, les tests, les exemples, la version de schéma et les références de compatibilité.
4. Ajouter une entrée à CHANGELOG.md et actualiser la version dans ce README et la notice de confidentialité si nécessaire.
5. Suivre les cas de tests/test-cases.md, vérifier le ZIP d’import et relire le diff public pour repérer les données privées ou assets non autorisés.

## Construire le ZIP importable

Depuis creativeai-tools/, exécuter :

    cd promptoscope-chatgpt-skill/skill
    zip -r ../promptoscope-chatgpt-skill-v1.0.0.zip promptoscope-image-to-prompt

Remplacer 1.0.0 par la version publiée. L’archive doit avoir un dossier racine promptoscope-image-to-prompt/ contenant SKILL.md et references/. Ne pas inclure les tests, exemples ou documents éditoriaux dans le paquet importable.

## Créer une GitHub Release

1. Créer une Release sur le dépôt à partir du commit validé sur main.
2. Créer le tag correspondant, par exemple v1.0.0.
3. Reprendre les changements pertinents du changelog dans les notes de version.
4. Joindre promptoscope-chatgpt-skill-v1.0.0.zip comme asset.
5. Publier la Release, puis vérifier que son asset se télécharge et que le ZIP peut être importé dans ChatGPT.
6. Pour une nouvelle version majeure ou mineure, mettre à jour le lien de téléchargement si le nom de l’asset ou la route change.

Une Release GitHub distribue le Skill source. Une fiche dans un répertoire public OpenAI nécessite une procédure de soumission distincte et doit suivre les exigences OpenAI en vigueur.
