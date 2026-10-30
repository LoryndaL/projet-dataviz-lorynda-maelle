# Analyse du marché immobilier français

## Objectif

Analyser les transactions immobilières françaises afin d'identifier les zones les plus attractives.

## Dataset

Demandes de Valeurs Foncières (DVF)

## Persona 👤 

### Marie Dupont – Directrice du Développement Territorial

**Organisation :** Réseau national d'agences immobilières présent sur l'ensemble du territoire français.

**Responsabilités :**

Marie est responsable de l'identification des zones géographiques les plus attractives pour le développement de l'entreprise. Son rôle consiste à analyser les évolutions du marché immobilier afin d'orienter les investissements, d'optimiser l'implantation des agences et de soutenir la stratégie commerciale nationale.

**Niveau de décision :** Décision stratégique

**Fréquence d'utilisation du tableau de bord :**

- Hebdomadaire : suivi des tendances du marché.
- Mensuelle : préparation des revues de performance.
- Trimestrielle : aide à la prise de décision concernant les investissements et l'expansion du réseau d'agences.

---

## 🎯 Ce qu'elle décide

Grâce aux indicateurs du tableau de bord, Marie doit être en mesure de :

- Identifier les départements présentant les meilleures opportunités de croissance.
- Déterminer les zones prioritaires pour l'ouverture de nouvelles agences.
- Orienter les investissements marketing et commerciaux.
- Détecter les territoires où l'activité immobilière ralentit.
- Comparer la dynamique du marché entre les différentes régions françaises.
- Identifier les types de biens les plus porteurs selon les territoires.

---

## ❓ Question métier principale

> **Dans quels départements et quelles communes l'entreprise doit-elle concentrer ses investissements afin de maximiser son développement commercial et sa présence sur le marché immobilier ?**

Cette question constitue le principal objectif du tableau de bord.

---

## 🔎 Questions métiers secondaires

### Analyse du marché

- Comment évoluent les prix de l'immobilier au fil des années ?
- Quels territoires affichent les plus fortes hausses de prix ?
- Quels territoires présentent un ralentissement ou une baisse des prix ?

### Activité immobilière

- Quels départements enregistrent le plus grand nombre de transactions ?
- Quelles communes sont les plus dynamiques ?
- Quels territoires connaissent la plus forte croissance du volume des ventes ?

### Opportunités d'investissement

- Quels départements combinent un fort volume de transactions et une croissance des prix soutenue ?
- Quelles zones présentent encore un potentiel de développement ?
- Où les investissements pourraient-ils générer le plus de valeur à moyen terme ?

### Analyse géographique

- Existe-t-il de fortes disparités entre les régions ?
- Quels sont les départements les plus attractifs ?
- Quels territoires émergent comme de futurs pôles de croissance ?

---

## 📊 Indicateurs clés (KPIs)

Le tableau de bord devra permettre de suivre :

- Le nombre total de transactions immobilières.
- Le prix moyen au m².
- Le prix médian au m².
- L'évolution annuelle des prix.
- L'évolution annuelle du volume des ventes.
- La répartition géographique des transactions.
- Le classement des départements les plus dynamiques.
- Le Top 10 des communes présentant le plus fort potentiel de croissance.

---

## 💡 Valeur apportée par le tableau de bord

À l'issue de son analyse, Marie doit pouvoir répondre rapidement à la question suivante :

> **« Si l'entreprise devait ouvrir trois nouvelles agences l'année prochaine, quels seraient les départements les plus pertinents au regard de l'évolution des prix, du volume des transactions et du dynamisme du marché immobilier ? »**

Le tableau de bord a donc pour vocation de transformer les données immobilières en recommandations concrètes d'investissement et de développement territorial.

## Installation des packages

pip install -r requirements.txt

# Analyse du marché immobilier français

## Télécharger les données

Les données proviennent de Data.gouv :

https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/

Puis exécuter :

scripts/download_data.py
