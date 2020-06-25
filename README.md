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
      
      output: 2
      ```      
        
    - Damerau levenshtain distance [ insert | delete | modify | transposition ]
      <br/>**transposition means swaping of 2 adjacent characters**
    
      same as levenshatin just pass transposition=False
      ```python
      from nltk.metrics.distance import edit_distance
      edit_distance("apple", "appel", transpositions=False, )
      
      output: 2
      ```
      
> Spell Corrector
  
  - Simple spell corrector 
      - Using a book as reference. To Use, import spell_corrector.py file and use rectify() function whose syntax is,<br/>
         **string rectify( word )**<br/>

          ```python
          from spell_corrector import rectify
          word = "monney"
          print(rectify(word))

          output: did you mean 'money'?
          ```
    
      
