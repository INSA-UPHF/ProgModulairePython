# Programmation Modulaire Version Python
La programmation modulaire est une approche qui consiste à diviser un programme en plusieurs **modules** indépendants et réutilisables. Chaque module a une responsabilité spécifique, ce qui améliore l'organisation, la lisibilité, la maintenabilité et la réutilisabilité du code.
### **Avantages de la programmation modulaire :**
Cette approche modulaire rend le code plus structuré, facile à lire, et maintenable.

1. **Lisibilité accrue** : Le code est mieux organisé et plus facile à comprendre.
2. **Réutilisabilité** : Les modules peuvent être réutilisés dans d'autres projets ou parties du code.
3. **Maintenance simplifiée** : Les bugs sont plus faciles à identifier et à corriger, car chaque module est isolé.
4. **Travail collaboratif** : Plusieurs développeurs peuvent travailler sur différents modules sans se chevaucher.
5. **Testabilité** : Les modules individuels peuvent être testés séparément.
   
Voici un exemple simple de projet structuré avec plusieurs fichiers Python, où un fichier principal `main.py` importe et utilise des fonctions ou des classes provenant d'autres fichiers.

---

### Structure du projet

```
projet/
│
├── main.py          # Fichier principal
├── math_utils.py    # Module pour les fonctions mathématiques
├── string_utils.py  # Module pour les manipulations de chaînes
└── config.py        # Module pour les configurations
```

---

### Explication des fonctionnalités

1. **math_utils.py** : Contient des fonctions pour effectuer des calculs simples comme l'addition et la soustraction.
2. **string_utils.py** : Fournit des outils pour manipuler les chaînes de caractères.
3. **config.py** : Stocke des configurations comme le nom et la version de l'application.
4. **main.py** : Fichier principal qui importe les autres modules, appelle leurs fonctions, et exécute le programme.

---

### Exécution
Pour exécuter le programme, lancez simplement le fichier `main.py` :
```bash
python main.py
```

---

### Résultat attendu
Lorsque vous exécutez le fichier principal, vous obtenez quelque chose comme ceci :
```
Addition: 5 + 3 = 8
Soustraction: 5 - 3 = 2
Phrase original: bonjour le monde
Phrase capitalisée: Bonjour Le Monde
Nombre de mots: 3
Application: Mon Application Python (Version: 1.0.0)
```

---

### Avantages d'une telle structure
- **Lisibilité** : Le code est organisé, et chaque fichier/module a une responsabilité spécifique.
- **Réutilisabilité** : Les modules (`math_utils`, `string_utils`, etc.) peuvent être utilisés dans d'autres projets.
- **Maintenabilité** : Les modifications dans un module n'affectent pas directement les autres.
