---
title: "Remove stopwords (remote stopword list)"
description: "Removes stopwords from all values. The stopword list is retrieved via a http connection (e.g. https://sites.google.com/site/kevinbouge/stopwords-lists/stopwords_de.txt). Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Remove stopwords (remote stopword list)
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes stopwords from all values. The stopword list is retrieved via a http connection (e.g. https://sites.google.com/site/kevinbouge/stopwords-lists/stopwords_de.txt). Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words.


## Parameter

### Stop word list url

No description

- Datatype: `string`
- Default Value: `None`



### Separator

No description

- Datatype: `string`
- Default Value: `[\s-]+`



