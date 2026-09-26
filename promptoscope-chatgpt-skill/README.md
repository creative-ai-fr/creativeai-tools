# Promptoscope ChatGPT Skill

**Version : 1.0.0** · **Schéma JSON : 1.0** · **Première version distribuable**

Promptoscope transforme une image jointe à ChatGPT en recette visuelle, prompt d’image réutilisable en anglais et JSON conforme au schéma Promptoscope v1.0. Il reprend les catégories et le format de l’extension dans une expérience conversationnelle.

## Télécharger et installer

1. Téléchargez [le ZIP Promptoscope ChatGPT Skill v1.0.0](https://github.com/creative-ai-fr/creativeai-tools/releases/latest/download/promptoscope-chatgpt-skill-v1.0.0.zip).
2. Dans ChatGPT, ouvrez la gestion des Skills et choisissez l’import d’un Skill depuis un fichier.
3. Sélectionnez le ZIP, puis démarrez une conversation avec le Skill.
4. Joignez une image que vous êtes autorisé à partager et demandez, par exemple : **« Analyse cette image avec Promptoscope. »**

La disponibilité de l’import et du partage dépend de l’offre ChatGPT, du déploiement du produit et des réglages de l’espace de travail. Une Release GitHub distribue le paquet source ; elle ne constitue pas une fiche dans un répertoire public OpenAI.

## Résultat

Par défaut, le Skill fournit une **recette visuelle** dans la langue de la conversation, un **Prompt (EN)** réutilisable, puis un JSON valide contenant exactement les 13 clés du schéma v1.0.

Catégories JSON : subject, setting, composition, lighting, style, color_palette, camera, details et text_detected, avec schema_version, language, prompt et negative_prompt.

Le contrat complet est dans [output-schema.json](skill/promptoscope-image-to-prompt/references/output-schema.json) ; les définitions et règles d’interprétation sont dans [analysis-method.md](skill/promptoscope-image-to-prompt/references/analysis-method.md).

## Architecture et limites

Image jointe dans ChatGPT → vision native de ChatGPT → Skill Promptoscope et références → recette visuelle, prompt anglais et JSON v1.0.

Le paquet contient des instructions et des références. Il n’utilise ni Gemini, ni clé API externe, ni serveur MCP, ni compte CreativeAI, ni backend ou compteur de quota Promptoscope. CreativeAI ne reçoit pas l’image ou le résultat par l’intermédiaire de ce Skill. L’accès, les modèles et les limites d’usage de ChatGPT restent applicables.

L’extension Chrome Promptoscope reste une implémentation distincte. Voir la [page Promptoscope de CreativeAI.fr](https://creativeai.fr/promptoscope-extension-chrome-image-prompt-json/).

## Tests manuels

Suivez les [cas de test](tests/test-cases.md) avec des images que vous êtes autorisé à partager. Ils couvrent les images claires, le texte lisible, l’incertitude, l’adaptation, plusieurs images, l’absence de pièce jointe et le texte hostile représenté dans une image.

Exemple de sortie JSON fictive : [sample-output.json](examples/sample-output.json).

## Publication et maintenance

- Les sources du Skill et son schéma sont conservés dans skill/promptoscope-image-to-prompt/.
- Chaque version met à jour ce README, CHANGELOG.md, les tests et les références de version.
- Le ZIP importable contient le dossier promptoscope-image-to-prompt/ et est joint à une GitHub Release ; il n’est pas commité dans le repository.
- Le guide de publication est dans [RELEASING.md](RELEASING.md) et la notice de flux de données dans [PRIVACY.md](PRIVACY.md).
- La documentation et les exemples sont sous licence [CC BY 4.0](LICENSE.md).
