# Publier une version

Ce guide concerne la distribution du Skill depuis `creative-ai-fr/creativeai-tools`.

## Avant chaque version

1. Mettre à jour `skill/promptoscope-camera-variants/`.
2. Vérifier que `SKILL.md` et toutes les références mentionnées existent.
3. Vérifier les schémas source et sidecar avec les exemples.
4. Ajouter une entrée à `CHANGELOG.md` et actualiser la version de ce README.
5. Relire le diff public pour repérer les données privées, les URLs locales et les assets non autorisés.

## Construire le ZIP importable

Depuis `promptoscope-camera-variants-skill/` :

```bash
cd skill
zip -r ../promptoscope-camera-variants-skill-v1.5.0.zip promptoscope-camera-variants
```

L’archive doit avoir un dossier racine `promptoscope-camera-variants/` contenant `SKILL.md`, `references/`, `agents/` et `assets/`. Ne pas inclure les tests, exemples ou documents éditoriaux dans le ZIP importable.

## Créer une GitHub Release

1. Valider le commit sur `main`.
2. Créer le tag `v1.5.0`.
3. Créer une Release GitHub à partir de ce tag.
4. Joindre `promptoscope-camera-variants-skill-v1.5.0.zip` comme asset.
5. Vérifier que l’asset se télécharge et s’importe dans ChatGPT.

Une Release GitHub distribue le Skill source. Une soumission au répertoire public OpenAI suit une procédure séparée.
