Ce travail est basé sur l'article : Insertion, Deletion, or Substitution? Normalizing Text Messages without
Pre-categorization nor Supervision (F Liu, F Weng, B Wang, Y Liu)

Outils utilisés:

- l'agorithme letter-to-letter alignment proposé par l'article
- CRF++ (https://taku910.github.io/crfpp/) pour le modèle qui a généré ressources utilisées
- CMUDICT (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- l'algorithme many-to-many letter phoneme alignment(Jiampojamarn et al., 2007)/(https://github.com/letter-to-phoneme/m2m-aligner)
- Hindson hyphenation dictionnary(http://hindson.com.au)
- Corpus of Contemporary American English (COCA) pour le corpus (https://corpus.byu.edu/coca/)

Le but du travail est de proposer la meilleure correspondance d'un oov (out-of-vocabulary).


---------------------------------------------

Utilisation

1. avoir un fichier contenant une liste de oov par ligne
2. Dans le fichier main.py, renseigner le fichier oov et un fichier de sortie pour les résultats. 
Si l'utilisation se fait par ligne de commande :

python main.py oovfile outputfile

------------------------------------------------
Ressources
Le dossier ressources contient toutes les ressources utilisées par le système
- corpus.json : le corpus utilisé
- dictionary.json : le dictionnaire contenant les prédictions du midèles

le dossier tn(text normalization) contient les scripts utilisés pour les différents changements de format des données