##Luxmètre avec Python et OpenCV

Ce projet propose un luxmètre utilisant Python avec la bibliothèque OpenCV pour mesurer la luminosité ambiante en temps réel à l'aide de la webcam de votre ordinateur. Il fournit des informations sur la luminosité moyenne de l'image capturée ainsi que sur la qualité de la caméra en pourcentage sur une échelle de 100. De plus, il permet d'enregistrer une vidéo tout en affichant la luminosité moyenne et les FPS (images par seconde) dans la vidéo enregistrée.


##Pourquoi ce projet ?

La mesure de la luminosité est importante dans de nombreux domaines tels que l'éclairage, la photographie, le cinéma, etc. Ce projet offre une solution simple et pratique pour mesurer la luminosité ambiante en utilisant la webcam de votre ordinateur. Il peut être utile pour les photographes amateurs, les ingénieurs en éclairage, les réalisateurs de films indépendants, et toute personne travaillant dans des conditions où la luminosité est un facteur critique.

##Fonctionnalités

Mesure de la luminosité en temps réel : Affiche la luminosité moyenne de l'image capturée par la webcam en temps réel.
Qualité de la caméra : Affiche la qualité de la caméra en pourcentage sur une échelle de 100, basée sur la résolution de l'image capturée.
Enregistrement vidéo : Permet d'enregistrer une vidéo avec affichage de la luminosité moyenne et des FPS dans la vidéo enregistrée.
Comment l'utiliser ?
Installation des dépendances : Assurez-vous d'avoir Python installé sur votre système. Installez ensuite OpenCV en utilisant la commande suivante :

##Copy code

pip install opencv-python

##Exécution du programme : Exécutez le script luxmeter.py en utilisant Python :

##Copy code

python luxmeter.py

##Interface utilisateur : Une fenêtre s'ouvrira affichant l'image capturée par votre webcam. La luminosité moyenne de l'image ainsi que la qualité de la caméra seront affichées en temps réel sur l'image. Vous pouvez déplacer votre caméra pour observer les changements de luminosité et de qualité.

##Enregistrement vidéo : Si vous souhaitez enregistrer une vidéo, appuyez sur la touche 'q' pour commencer l'enregistrement, et appuyez à nouveau sur 'q' pour arrêter l'enregistrement.

##Contributions
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à créer une issue ou à proposer une pull request.

##Licence
Ce projet est sous licence MIT.