# Tests Brand Guardian

- `brand-guardian/test-cases.md` : 15 scénarios adversariaux et de régression, utilisables comme prompts de test.
- `brand-guardian/expected-results.md` : décision attendue et critères d'acceptation par scénario.
- `brand-guardian/model-evaluation-run-2026-09-26.md` : replay aveugle des 15 cas par un modèle Codex distinct, avec résultat et limites.
- `brand-guardian/challenge-log.md` : trois passes de challenge et corrections intégrées.
- `brand_guardian_cases.json` : manifeste compact lisible par un harness d'évaluation.
- `test_brand_guardian_package.py` : contrôles déterministes du paquet, des métadonnées et des invariants déclarés.

Lancer les contrôles déterministes depuis la racine du dépôt :

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Les contrôles déterministes ne mesurent pas la qualité d'une sortie de modèle. Le replay aveugle par un modèle distinct est consigné dans le rapport ci-dessus. Après installation ou changement important des instructions, rejouer chaque `prompt` du manifeste dans le runtime cible et comparer la réponse au champ `expected` et aux attendus détaillés.
