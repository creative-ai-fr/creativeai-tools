# Préparer la publication GitHub

## Nom recommandé du dépôt

```text
brand-brain-evaluation-lab
```

## Description courte

> Open-source protocol, Markdown/YAML test cases and scorecards for evaluating whether AI assistants follow a brand brain.

## Topics recommandés

```text
brand-brain
brand-guidelines
ai-evaluation
llm-evals
human-in-the-loop
open-source
content-governance
brand-identity
markdown
yaml
```

## Intégration dans `creativeai-tools`

```bash
git clone https://github.com/creative-ai-fr/creativeai-tools.git
cd creativeai-tools

# Copier le dossier brand-brain-evaluation-lab/ à la racine de ce repository.
git add README.md brand-brain-evaluation-lab
git commit -m "Add Brand Brain Evaluation Lab"
git push origin main
```

Le package est conçu pour être placé ici :

```text
creativeai-tools/brand-brain-evaluation-lab/
```

## Release recommandée

### Version

`v0.2.3`

### Titre

`Brand Brain Evaluation Lab v0.2.3 — creativeai-tools repository integration`

### Notes de release

Cette première release publique fournit :

- un protocole d’évaluation de Brand Brain ;
- huit dimensions de scoring ;
- une politique d’escalade humaine ;
- un format hybride Markdown/YAML ;
- un registre de sources et de règles ;
- trois cas de test fictifs ;
- une configuration de série d’exécution.
- un bloc d’article expliquant l’installation et l’exécution dans ChatGPT Work et Claude Cowork.
- un bloc CTA vers le Creative Memory Sprint pour prolonger le travail de structuration de la mémoire IA.
- une intégration documentée dans le repository `creative-ai-fr/creativeai-tools`.

Le dépôt ne constitue pas une certification de modèle ou de marque. Les exemples doivent être remplacés par des contenus dont les droits sont documentés.

## Vérifications avant publication

- [ ] vérifier que les liens GitHub pointent vers `creative-ai-fr/creativeai-tools` ;
- [ ] choisir et confirmer la licence ;
- [ ] vérifier que les exemples ne contiennent aucune donnée confidentielle ;
- [ ] vérifier les droits des logos, images et références ;
- [ ] exécuter les cas YAML avec un assistant ;
- [ ] ajouter un rapport d’exécution dans `evals/` ;
- [ ] créer la release GitHub avec le changelog associé.

## Intégration dans l’article

Les blocs Gutenberg prêts à copier se trouvent dans [`article/brand-brain-evaluation-lab-block.html`](article/brand-brain-evaluation-lab-block.html), [`article/installation-and-test-block.html`](article/installation-and-test-block.html) et [`article/creative-memory-sprint-cta-block.html`](article/creative-memory-sprint-cta-block.html). Le bouton pointe vers le sous-dossier public du repository.
