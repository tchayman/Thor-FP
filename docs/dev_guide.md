# Developer Guide — THOR-FP

Ce guide fournit des instructions pour contribuer, maintenir et étendre le code du projet *THOR-FP*.

---

## 1. Structure du code

•⁠  ⁠⁠ src/thor_fp/ ⁠ : modules Python principaux (⁠ model.py ⁠, ⁠ harmonics.py ⁠, ⁠ encoder.py ⁠, ⁠ decoder.py ⁠, ⁠ utils.py ⁠, ⁠ config.py ⁠, ⁠ metrics.py ⁠)
•⁠  ⁠⁠ notebooks/ ⁠ : notebooks de démonstration/reproductibilité
•⁠  ⁠⁠ benchmarks/ ⁠ : scripts & tableaux de benchmark
•⁠  ⁠⁠ tests/ ⁠ : tests unitaires
•⁠  ⁠⁠ docs/ ⁠ : documentation utilisateur et développeur
•⁠  ⁠⁠ arxiv/ ⁠ : structure pour la soumission scientifique

---

## 2. Bonnes pratiques

•⁠  ⁠*Un module = une responsabilité* (évitez les scripts “fourre-tout”)
•⁠  ⁠*Docstrings systématiques* pour chaque fonction/classe
•⁠  ⁠*Respect du PEP8* (conventions de nommage Python)
•⁠  ⁠*Tests unitaires* pour chaque nouveau composant
•⁠  ⁠*Gardez le code modulaire* et évitez les dépendances circulaires

---

## 3. Ajouter un module ou une fonctionnalité

•⁠  ⁠Placez le code dans le module concerné de ⁠ src/thor_fp/ ⁠
•⁠  ⁠Ajoutez un test unitaire associé dans ⁠ tests/ ⁠
•⁠  ⁠Documentez le module et la fonctionnalité dans ce guide si besoin

---

## 4. Ajout d’un notebook

•⁠  ⁠Placez le notebook dans ⁠ notebooks/ ⁠
•⁠  ⁠Nommez-le ⁠ demo_<fonctionnalité>.ipynb ⁠
•⁠  ⁠Commentez clairement chaque cellule importante

---

## 5. Gestion de la configuration

•⁠  ⁠Centralisez les paramètres dans un fichier YAML (ex : ⁠ config.yaml ⁠)
•⁠  ⁠Utilisez la fonction ⁠ load_config ⁠ du module ⁠ config.py ⁠

---

## 6. Standards pour les PR / Issues

•⁠  ⁠*Pull Requests* : inclure description claire + lien vers l’issue associée
•⁠  ⁠*Issues* : donner contexte, étape pour reproduire, logs éventuels

---

## 7. Extensions possibles

•⁠  ⁠Ajouter des tests automatisés (GitHub Actions, pytest…)
•⁠  ⁠Intégrer de nouveaux modules harmoniques, fractals, etc.
•⁠  ⁠Ajouter de la documentation technique avancée

---

Bon développement sur THOR-FP !
