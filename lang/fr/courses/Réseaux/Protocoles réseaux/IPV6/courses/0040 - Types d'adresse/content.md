## Système numérique hexadécimal

Avant de présenter le format d'adresse IPv6, nous allons examiner le système numérique hexadécimal. L'hexadécimal est un système numérique positionnel qui utilise un radix (base) de 16. Pour représenter les valeurs dans un format lisible, ce système utilise les symboles 0-9 pour représenter les valeurs de zéro à neuf et A-F pour représenter les valeurs de dix à quinze. Chaque chiffre en hexadécimal peut représenter des valeurs de 0 à 15.

| **Décimal** | **Binaire** | **Hexadécimal** |
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |

## Structure de l'adresse

Une adresse IPv6 est constituée de 128 bits divisés en huit blocs de 16 bits. Chaque bloc est ensuite converti en nombres hexadécimaux à 4 chiffres séparés par des symboles deux-points.

Par exemple, voici une adresse IPv6 de 128 bits représentée au format binaire et divisée en huit blocs de 16 bits :

```
0010000000000001 0000000000000000 0011001000111000 1101111111100001 0000000001100011 0000000000000000 0000000000000000 1111111011111011
```

Chaque bloc est ensuite converti en hexadécimal et séparé par le symbole ':' :

```
2001:0000:3238:DFE1:0063:0000:0000:FEFB
```

Même après avoir été convertie au format hexadécimal, l'adresse IPv6 reste longue. IPv6 fournit quelques règles pour raccourcir l'adresse. Ces règles sont les suivantes :

### Règle 1 : écartez le(s) zéro(s) de tête

Dans le bloc 5, 0063, les deux premiers 0 peuvent être omis, par exemple (5e bloc) :

```
2001:0000:3238:DFE1:63:0000:0000:FEFB
```

### Règle 2

Si deux blocs ou plus contiennent des zéros consécutifs, omettez-les tous et remplacez-les par le double signe deux-points : :, par exemple (6e et 7e blocs) :

```
2001:0000:3238:DFE1:63::FEFB
```

Les blocs de zéros consécutifs ne peuvent être remplacés qu'une seule fois par : : donc, s'il reste des blocs de zéros dans l'adresse, ils peuvent être réduits à un seul zéro, comme (2e bloc) :

```
2001:0:3238:DFE1:63::FEFB
```

## ID d'interface

L'IPv6 a trois types différents de schéma d'adresse de diffusion individuelle. La seconde moitié de l'adresse (les 64 derniers bits) est toujours utilisée pour l'ID d'interface. L'adresse MAC d'un système est composée de 48 bits et représentée en hexadécimal. Les adresses MAC sont considérées comme étant attribuées de manière unique dans le monde entier. L'ID d'interface tire parti de cette unicité des adresses MAC. Un hôte peut auto-configurer son ID d'interface en utilisant le format EUI-64 (Extended Unique Identifier) de l'IEEE. Tout d'abord, un hôte divise sa propre adresse MAC en deux moitiés de 24 bits. Ensuite, la valeur hexagonale de 16 bits 0xFFFE est insérée dans ces deux moitiés de l'adresse MAC, ce qui donne l'ID d'interface EUI-64.

![ID d'interface EUI-64](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image5.jpg)

### Conversion de l'ID EUI-64 en identifiant d'interface IPv6

Pour convertir l'identifiant EUI-64 en identifiant d'interface IPv6, le 7ème bit le plus significatif de l'identifiant EUI-64 est complété. Par exemple :

![convertissage de l'identifiant EUI-64 en identifiant d'interface IPv6](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image2.png)

## Adresse de monodiffusion globale

Ce type d'adresse est équivalent à l'adresse publique d'IPv4. Les adresses Global Unicast d'IPv6 sont identifiables et adressables de manière unique au niveau mondial.

![Adresse de monodiffusion globale](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image6.jpg)

Préfixe de routage global : Les 48 bits les plus significatifs sont désignés comme le préfixe de routage global qui est attribué à un système autonome spécifique. Les trois bits les plus significatifs du préfixe de routage global ont toujours la valeur 001.

## Adresse Link-Local

L'adresse IPv6 auto-configurée est connue sous le nom d'**adresse Link-Local**. Cette adresse commence toujours par FE80. Les 16 premiers bits de l'adresse locale de liaison sont toujours définis comme 1111 1110 1000 0000 (FE80). Les 48 bits suivants sont définis sur 0, donc :

![Adresse Link-Local](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image4.jpg)

Les adresses locales de lien sont utilisées pour la communication entre les hôtes IPv6 sur un lien (segment de diffusion) uniquement. Ces adresses ne sont pas routables, de sorte qu'un routeur ne transmet jamais ces adresses en dehors du lien.

## Adresse locale unique

Ce type d'adresse IPv6 est unique au niveau mondial, mais il doit être utilisé pour les communications locales. La seconde moitié de cette adresse contient l'ID de l'interface et la première moitié est divisée entre le préfixe, le bit local, l'ID global et l'ID du sous-réseau.

![Adresse locale unique](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image3.jpg)

Le préfixe est toujours fixé à 1111 110. Le bit L est mis à 1 si l'adresse est attribuée localement. Jusqu'à présent, la signification du bit L à 0 n'est pas définie. Par conséquent, l'adresse IPv6 locale unique commence toujours par 'FD'.

### Portée des adresses unicast IPv6

![Portée des adresses unicast IPv6](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/courses/R%C3%A9seaux/Protocoles%20r%C3%A9seaux/IPV6/courses/0040%20-%20Types%20d'adresse/images/image1.jpg)

La portée de l'adresse Link-local est limitée au segment. Les adresses locales uniques sont localement globales, mais ne sont pas acheminées sur Internet, ce qui limite leur portée à la frontière d'une organisation. Les adresses Unicast globales sont uniques et reconnaissables au niveau mondial. Elles constituent l'essence de l'adressage Internet v2.