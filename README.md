## Company Case

`companycase` lets you format raw company names into a neat title case while capitalising words which appear to be abbreviations. 

| string | companycase(string)|
|-------| -------|
| hsbc uk bank plc | HSBC UK Bank PLC |
| cloudera (uk) limited | Cloudera (UK) Limited
| kfc restaurants limited | KFC Restaurants Limited|
| a&g holdings ltd | A&G Holdings Ltd |
| jp morgan | JP Morgan |
| axa insurance co.| AXA Insurance Co. |
    
`companycase` uses n-grams to distinguish words that *are or look like dictionary words* (bank, limited, cloudera, deliveroo) from words that do not (HSBC, JP, HJHJ). Words that do not tend to be acronyms in the context of a company name, and are thus capitalised.

### Installation

No external packages are required. Install with

    python setup.py install

or using `pip` with

    pip install git+git://github.com/duedil-ltd/companycase.git#egg=companycase

### Quickstart
    
    from companycase import CompanyCase
    ccase = CompanyCase(language='en')
    
    print ccase.apply("foo bar ltd")

### Tuning the model

By default, the model uses n-grams of length 2 (bigrams) over the english wordlist. These two options can be changed during initialization.

A word's score is the mean transition score for all the n-grams contained within it. If the score exceeds the threshold, the word returned title cased, or capitalized if not. The `apply()` method takes an additional optional argument to use a custom threshold.

    >>> print ccase.apply("hello there nk")
    'Hello There NK'
    >>> print ccase.apply("hello there nk", threshold=0.5)
    'HELLO THERE NK'
    
The defaults (`ngram_length=2` and `threshold=0.001`) were chosen by evaluating the performance over a small dataset using the `companycase.util.evaluate()` method.

#### Handling case for specific words
You can also force the case for some special words using the `force_case_for_words()` method.

    >>> ccase.force_case_for_words(['fOO'])
    >>> ccase.apply('foo bar ltd')
    'fOO Bar LTD'

### Todo

- Support additional languages/wordlists beyond English
- Index on PyPI

