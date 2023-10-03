Lorsque vous estimez que votre dépôt est prêt à être partagé, vous pouvez le pousser vers l'amont en utilisant la commande suivante : ```git push [nom-distant] [nom-de-branche]```. Par exemple, si vous souhaitez pousser votre branche master vers le serveur origin (rappel : lors de la clonaison d'un dépôt, ces noms sont généralement configurés pour vous), vous pouvez exécuter la commande suivante pour mettre à jour le serveur distant avec votre travail :

```bash
$ git push origin master
```

Il est important de noter que cette commande fonctionne uniquement si vous avez cloné depuis un serveur sur lequel vous avez les droits d'accès en écriture et si personne n'a poussé de modifications entre-temps. Si vous et une autre personne clonez le même dépôt en même temps, et que cette autre personne pousse ses modifications avant vous, votre tentative de poussée sera rejetée. Dans ce cas, vous devrez d'abord tirer (ou "pull") les modifications de l'autre personne, les fusionner avec les vôtres localement, puis essayer à nouveau de pousser.
