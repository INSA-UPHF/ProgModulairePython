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

### Contenu des fichiers

#### **1. math_utils.py**
```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

#### **2. string_utils.py**
```python
# string_utils.py

def capitalize_words(sentence):
    """Met en majuscule chaque mot dans une phrase."""
    return ' '.join(word.capitalize() for word in sentence.split())

def count_words(sentence):
    """Compte le nombre de mots dans une phrase."""
    return len(sentence.split())
```

---

#### **3. config.py**
```python
# config.py

APP_NAME = "Mon Application Python"
VERSION = "1.0.0"
```

---

#### **4. main.py**
```python
# main.py

# Importation des modules
from math_utils import add, subtract
from string_utils import capitalize_words, count_words
import config

def main():
    # Utilisation des fonctions mathématiques
    num1, num2 = 5, 3
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Soustraction: {num1} - {num2} = {subtract(num1, num2)}")

    # Utilisation des fonctions de manipulation de chaînes
    sentence = "bonjour le monde"
    print(f"Phrase original: {sentence}")
    print(f"Phrase capitalisée: {capitalize_words(sentence)}")
    print(f"Nombre de mots: {count_words(sentence)}")

    # Utilisation des paramètres de configuration
    print(f"Application: {config.APP_NAME} (Version: {config.VERSION})")

if __name__ == "__main__":
    main()
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
