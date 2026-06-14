# 🏎️ Assetto Corsa Evo — Vehicle Physics Reference Documentation

Bienvenue sur le dépôt central de la documentation communautaire dédiée à l'architecture physique et structurelle d'**Assetto Corsa Evo (v0.7.1)**. 

Ce projet a pour but de fournir une base de connaissances standardisée, claire et technique pour aider les moddeurs, les ingénieurs en dynamique de véhicule et les passionnés de simulation à comprendre, concevoir et modifier proprement les fichiers physiques du jeu.

---

## 📖 Contenu de la Documentation

Chaque ressource analysée suit une structure de documentation rigoureuse pour garantir une clarté maximale :
1. **Description Générale :** Rôle global de l'asset au sein du moteur de physique.
2. **Zones d'Influence :** Impact concret du fichier sur le comportement dynamique en piste.
3. **Architecture Clé & Paramètres :** Explications détaillées des variables, types de données et unités.
4. **Stratégies d'Implémentation :** Exemples concrets de profils mécaniques (Série, GT3, Prototypes, etc.).

### 🗂️ Les Assets Physiques Cartographiés

| Asset Module | Extension de Fichier | Domaine d'Application & Impact Dynamique |
| :--- | :---: | :--- |
| **Brake System** | `.brakesystem` | Couple maximal, balance de freinage statique, modules électroniques d'aide (EBB, Steer-Brake) et logiques algorithmiques associées. |
| **Brakes Hardware** | `.brakes` | Modélisation thermique locale, coefficients de friction dynamiques (Courbe d'efficacité selon la température), taux d'usure des disques/plaquettes et refroidissement (vitesse, pluie). |
| **Car Data** | `.cardata` | Masse totale à sec, vecteurs d'inertie (Pitch, Roll, Yaw), hauteur du centre de gravité, répartition des masses et coordonnées physiques du réservoir de carburant. |
| **Car Engine** | `.carengine` | Génération de puissance (courbes de couple/RPM), inertie de l'équipage mobile (volant moteur), traînée de frein moteur et cartographies de suralimentation (turbo). |
| **Car Setup** | `.setup` / `.ini` | Interface des réglages du garage : pressions de pneus, géométrie d'alignement (carrossage, parallélisme), raideur des ressorts/barres, et clapets d'amortisseurs à 4 voies. |
| **Car Setup Limits** | `.carsetuplimits` | Encadrement administratif et technique : valeurs Min/Max, pas d'incrémentation (Steps), visibilité dans les menus et brides réglementaires (BOP). |

---

## 💾 Accéder au Guide PDF Complet

Pour une lecture confortable sur un second écran ou une tablette pendant vos sessions de modding, le guide technique complet est disponible au format PDF compilé :

👉 **[Télécharger / Consulter le Guide Complet des Assets Physiques (PDF)](./README_Physics_Documentation.pdf)**

*(La visionneuse native de GitHub vous permet de naviguer et d'effectuer des recherches textuelles via `Ctrl + F` directement dans le fichier).*

---

## 🤝 Contribuer au Projet

Les découvertes collaboratives sont les bienvenues ! Si vous identifiez de nouveaux paramètres physiques via de l'ingénierie inverse, l'analyse de télémétrie ou des tests en jeu :
1. **Forkez** ce dépôt.
2. Ajoutez ou ajustez les descriptions en conservant la structure unifiée du projet.
3. Soumettez une **Pull Request** détaillée expliquant vos conclusions ou les données vérifiées.

---

## 📄 Licence

Ce projet est distribué sous la licence **Creative Commons Attribution 4.0 International (CC BY 4.0)**. 
Vous êtes libre de partager, copier, distribuer et modifier ce contenu, y compris pour des projets tiers, à la seule condition de **créditer les auteurs originaux** et de mentionner la communauté.

---
*Mentions légales : Ce projet est une initiative bénévole et indépendante de la communauté. Assetto Corsa Evo est une marque déposée de Kunos Simulazioni. Les informations fournies ici le sont à titre éducatif pour l'aide au modding.*
