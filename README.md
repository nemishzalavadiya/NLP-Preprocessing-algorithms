# NLP-Preprocessing-algorithms
Soundx - Phonetic | Edit Distance - spell currection | PMI - pointwise mutual information [ preserve words ]

> Soundex Algorithms

  - Phonetic Algorithm [ 4 Letters ( 1 character - 3 number ) ]
  
> Spell Checker

  - Edit Dictance
    - Levenshtein Edit Distance [ insert | delete | modify ]
    
      also available in NLTK,
      
      ```python
      from nltk.metrics.distance import edit_distance
      edit_distance("apple", "appel")
      ```
      output - 2
        
    - Damerau levenshtain distance [ insert | delete | modify | transposition ]
      <br/>**transposion means swaping of 2 adjacent characters**
    
      same as levenshatin just pass transposition=False
      ```python
      from nltk.metrics.distance import edit_distance
      edit_distance("apple", "appel", transpositions=False, )
      ```
      output - 2
