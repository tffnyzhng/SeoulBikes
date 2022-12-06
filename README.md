# SeoulBikes

![alt text](https://github.com/tffnyzhng/SeoulBikes/blob/main/images_readme/image_velo.jpg?raw=true)

Il est important de rendre le vélo de location disponible et accessible au public, car il offre de nombreuses alternatives aux navetteurs dans les métropoles. Il y a beaucoup d'avantages à louer un vélo, c'est pratique car cela permet de ne pas garder le vélo toute la journée, que ce soit au travail ou à l'école. De plus, c'est le moyen de transport le plus sain et il présente des avantages pour l'environnement.

**Comment nous est-il possible d’anticiper la demande du nombre de vélos loués en fonction des conditions météorologiques?**

A travers l’etude du data set Seoul Bike Sharing demand nous tenterons de répondre à cette question.

Nous pouvons retrouver le dataset au lien suivant : [https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand#](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand#)
<br>

Le data set Seoul Bike Sharing Demand est un jeu de données contenant le nombre de vélos publics loués à chaque heure dans le système de vélos en libre-service de Séoul, mais également des données météorologiques et les informations sur les vacances correspondantes. Le jeu de donnée contient des données récoltés pendant un an à partir du 1er décembre 2017. 


## Contenu du dépot
Pour cette étude nous travaillerons avec Python, découpée en 3 principales parties :
Data Visualisation : pour explorer et comprendre nos données et leurs liens avec la cible
Machine Learning : pour modéliser une prédiction
Transformation du modèle en une API Flask : pour pouvoir utiliser notre modèle de prédiction sur de nouvelle données, en déploiement.
Cette étude contient donc 
- un Notebook Jupyter (composé du code nécessaire à notre étude), 
- le data set associé,
- une présentation PowerPoint de l’étude 
- et les fichiers nécessaires à la transformation de notre model en une API Flask
 
![alt text](https://github.com/tffnyzhng/SeoulBikes/blob/main/images_readme/image_api.jpg?raw=true)

## Conclusion
Cette étude sur les vélos loués à Séoul a permis de répondre à la problématique en choisissant un modèle approprié pour l’anticipation de la demande du nombre de vélos loués en fonction des conditions météorologiques. Le Random Forest est finalement le modèle sélectionné résoudre notre problème et qu’on déploiera sous forme d’API.

Enfin, une perspective de future est qu’on puisse déployer et adapter ce même modèle à l'échelle internationale et le généraliser aux grandes métropoles comme Paris qui aujourd’hui se transforme de plus en plus en une ville cyclable, pour mieux prévoir la demande. En effet, les vélos de location sont introduits dans de nombreuses villes urbaines pour améliorer le confort de la mobilité. Le but de ce mouvement est de moderniser les villes et d'inciter les gens à se diriger vers un transport vert. Par exemple, à Paris en 2007, les "vélibs" ont été introduits, et à Amsterdam, il y a plus de vélos que de voitures. De plus, avec les JO qui approchent et le fort flux de déplacement, Paris se transforme en une ville beaucoup plus cyclable et verte. Traverser Paris en voiture devient de plus en plus compliqué ainsi ce projet entrainera beaucoup d’enjeux dans le futur concernant la mobilité et la circulation pour mieux prévoir la demande et adapter nos modes de déplacement.
