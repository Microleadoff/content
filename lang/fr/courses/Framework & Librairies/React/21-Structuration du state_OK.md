## Structuration du state

La structure du state est un élément crucial dans la conception de composants React. Une organisation réfléchie simplifie la gestion et la mise à jour du state, tandis qu’une structure mal pensée peut rendre le code difficile à maintenir et source de bugs. Ce cours explore les principes clés pour structurer efficacement le state.

### Pourquoi structurer le state correctement ?

Une structure bien pensée permet de :
- **Améliorer la lisibilité** : Un code bien structuré est plus intuitif, ce qui facilite son adaptation ou son débogage.
- **Faciliter la maintenance** : En réduisant les incohérences entre les données, les sources de bugs sont limitées.
- **Optimiser les performances** : Les modifications du state sont ciblées, réduisant les rerenderings inutiles.

Ces avantages rendent vos composants plus robustes, plus clairs et plus prévisibles.

## Principes essentiels pour structurer le state

### **1. Regrouper les états associés**

Si plusieurs variables d’état partagent une logique commune ou changent ensemble, il est judicieux de les regrouper en une seule variable. Cela assure leur cohérence et simplifie leur gestion.

**Exemple : Gestion d'une position**

```javascript
const [position, setPosition] = useState({ x: 0, y: 0 });

function updatePosition(newX, newY) {
  setPosition({ x: newX, y: newY });
}
```

Regrouper les variables `x` et `y` garantit qu'elles restent synchronisées, évitant ainsi des bugs où une seule coordonnée serait mise à jour.

### **2. Éviter les contradictions**

Les états contradictoires compliquent la gestion d’un composant et augmentent le risque d’erreurs. Utilisez une seule variable pour représenter des états mutuellement exclusifs, plutôt que plusieurs variables booléennes.

**Exemple : Gestion d’un formulaire**

```javascript
const [isSubmitting, setIsSubmitting] = useState(false);

function handleSubmit() {
  setIsSubmitting(true);
  setTimeout(() => setIsSubmitting(false), 2000); // Simule une requête réseau
}

return (
  <>
    {isSubmitting ? (
      <p>Merci pour votre soumission !</p>
    ) : (
      <form onSubmit={handleSubmit}>
        <button disabled={isSubmitting}>Envoyer</button>
      </form>
    )}
  </>
);
```

Utiliser une seule variable (`isSubmitting`) simplifie la gestion des transitions d'état et garantit qu'il n'y ait pas de conflits (par exemple, un état simultanément "envoyé" et "en cours d'envoi").

### **3. Éviter les états dupliqués**

Stocker plusieurs fois la même information dans le state complique la gestion des données. Si possible, utilisez des identifiants pour éviter la duplication et calculer les informations nécessaires lors du rendu.

**Exemple : Liste d’articles avec sélection**

```javascript
const [items, setItems] = useState([
  { id: 1, title: 'Article 1' },
  { id: 2, title: 'Article 2' },
]);
const [selectedItemId, setSelectedItemId] = useState(null);

const selectedItem = items.find(item => item.id === selectedItemId);

function handleSelect(id) {
  setSelectedItemId(id);
}
```

Stocker uniquement l’identifiant sélectionné (`selectedItemId`) élimine les redondances et facilite la synchronisation. Tout changement dans `items` sera automatiquement reflété dans `selectedItem`.


### **4. Réduire les redondances**

Les données dérivables, c’est-à-dire calculables à partir des variables d’état ou des props, ne doivent pas être stockées dans l’état. Cela réduit les risques d’incohérences et allège la gestion.

**Exemple : nom complet**

```javascript
const [firstName, setFirstName] = useState('');
const [lastName, setLastName] = useState('');

const fullName = `${firstName} ${lastName}`;
```

Calculer `fullName` à partir de `firstName` et `lastName` pendant le rendu évite de maintenir une troisième variable inutilement.

### **5. Limiter l’imbrication**

Des structures trop imbriquées rendent les mises à jour complexes et augmentent les risques de bugs. Adoptez une structure plate lorsque cela est possible.

**Exemple : Structure plate pour une liste hiérarchique**

Une **structure plate** consiste à organiser les données de manière à ce qu'elles soient toutes stockées à un même niveau, sans imbrication excessive. Au lieu d'avoir des objets ou tableaux imbriqués les uns dans les autres, chaque élément est représenté individuellement, avec des références pour indiquer les relations entre eux. Cela simplifie grandement la gestion des données en rendant leur accès, leur mise à jour et leur parcours beaucoup plus efficaces.

```javascript
const [data, setData] = useState({
  itemsById: {
    1: { id: 1, title: 'Section 1' },
    2: { id: 2, title: 'Section 2' },
  },
  itemOrder: [1, 2],
});

function updateItemTitle(id, newTitle) {
  setData(prevData => ({
    ...prevData,
    itemsById: {
      ...prevData.itemsById,
      [id]: { ...prevData.itemsById[id], title: newTitle },
    },
  }));
}
```

Une structure plate simplifie les mises à jour ciblées et limite les copies inutiles lors de la modification d’un élément.


### Conclusion

Structurer efficacement le state repose sur des principes simples :
- **Regrouper les états liés** pour assurer leur cohérence.
- **Réduire la duplication et les redondances** pour simplifier les mises à jour.
- **Adopter une structure plate** pour éviter des imbrications inutiles.

Ces bonnes pratiques améliorent la maintenabilité de votre code et réduisent les erreurs, rendant vos composants plus robustes et réactifs.