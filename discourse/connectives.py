PATTERNS = {
    "precedence": {
        "afterward(s)": "^afterwards?",
	    "after that": "^after th(at|is)",
        "eventually": "^eventually",
        "in turn": "^in turn",
	    "later": "^later",
        "next": "^next", # followed by pronoun?
        "thereafter": "^thereafter"
    },
    "succession": {
        "before that": "^before th(at|is)",
        "earlier": "^earlier",
        "previously": "^previously"
    },
    "synchrony": {
        "in the meantime": "^(in the )?meantime",
	    "meanwhile": "^meanwhile",
        "simultaneously": "^simultaneously"
    },
    "result": {
        "accordingly": "^accordingly",
        "as a result": "^as a result(?! of)", # followed by pronoun?
        "consequently": "^consequently",
        "therefore": "^therefore",
        "thus": "^thus"
    },
    "conjunction": {
        "additionally": "^additionally",
        "also": "^also", # followed by a pronoun?
        "besides": "^besides",
        "furthermore": "^furthermore", # followed by pronoun if just "further"?
        "in addition": "^in addition", # followed by , or pronoun?
        "likewise": "^likewise",
        "moreover": "^moreover",
        "similarly": "^similarly"
    },
    "contrast": {
        "by/in comparison": "^(by|in) comparison", # followed by pronoun/noun
        "by/in contrast": "^(by|in) contrast", # followed by pronoun/noun
        "conversely": "^conversely",
        "nevertheless": "^nevertheless",
        "on the other hand": "^on the other hand",
    },
    "instantiation": {
        "for example": "^for example",
        "for instance": "^for instance",
        "in particular": "^in particular",
    },
    "alternative": {
        "instead": "^instead", # followed by pronoun?
        "rather": "^rather" # followed by pronoun
    }
}

INNERS = {
    # TEMPORAL:Asynchronous.precedence
    "afterward(s)": ["and afterwards", "but afterwards", "after which", "then"],
    "after that": ["after that", "after this", "but, after that", "and after this", "after which"],
    "eventually": ["eventually", "and eventually", "and in turn"],
    "in turn": ["in turn", "which, in turn", "and then", "and so", "leaving"],
    "later": ["later", "and later", "but later"],
    "next": ["next", "before", "followed by", "when"],
    "thereafter": ["thereafter", "and thereafter", "after which"],
    # TEMPORAL:Asynchronous.succession
    "before that": ["before that", "but before that", "although before that", "prior to this"],
    "earlier": ["earlier", "and earlier", "formerly", "previously", "after"],
    "previously": ["and previously", "previously", "recently"],
    # TEMPORAL:Synchrony
    "in the meantime": ["in the meantime", "but in the meantime", "whilst", "meanwhile", "while in the meantime", "while",],
    "meanwhile": ["meanwhile", "meanwhile", "while"],
    "simultaneously": ["simultaneously", "and simultaneously", "while",],
    # CONTINGENCY:Cause.result
    "accordingly": ["accordingly", "so", "as such", "and as such"],
    "as a result": ["as a result", "and as a result", "however", "so that", "resulting in", "so"], # <REV> as a result of?
    "consequently": ["consequently", "and therefore", "and so", "so"],
    "therefore": ["therefore", "and so", "which means", "which means that"],
    "thus": ["thus", "and thus", "thusly"],
    # COMPARISON:Contrast
    "by/in comparison": ["by comparison", "in comparison", "while", "compared to", "whilst"],
    "by/in contrast": ["by contrast", "in contrast", "and in contrast", "while", "although"],
    "conversely": ["conversely", "and conversely"],
    "on the other hand": ["on the other hand", "and on the other hand", "but on the other hand", "but", "whereas", "however", "while"],
    "nevertheless": ["nevertheless", "but", "none the less", "yet", "however"],
    # EXPANSION:Conjunction
    "additionally": ["additionally", "and additionally"],
    "also": ["and also", "and is also"],
    "in addition": ["in addition to", "and additionally"],
    "furthermore": ["further", "furthermore", "and furthermore", "and further"],
    "moreover": ["moreover", "indeed"],
    "besides": ["besides", "besides this", "and also", "aside from"],
    "likewise": ["likewise", "and likewise", "and also"],
    "similarly": ["similarly", "and similarly", "while"],
    # EXPANSION:Instantiation
    "for example": ["for example", "such as"],
    "for instance": ["for instance", "such as"],
    "in particular": ["in particular"],
    # EXPANSION:Alternative
    "instead": ["instead", "but instead", "though"],
    "rather": ["but rather", "though"],
}

FORWARDS = {
    # TEMPORAL:Asynchronous.precedence
    "afterward(s)": [],
    "after that": [],
    "eventually": [],
    "in turn": [],
    "later": [],
    "next": ["before"],
    "thereafter": [],
    # TEMPORAL:Asynchronous.succession
    "before that": [],
    "earlier": ["after"],
    "previously": [],
    # TEMPORAL:Synchrony
    "in the meantime": ["while"],
    "meanwhile": ["while"],
    "simultaneously": ["while"],
    # CONTINGENCY:Cause.result
    "accordingly": ["<REV>because",],
    "as a result": ["<REV>because",],
    "consequently": ["<REV>because",],
    "therefore": ["<REV>because",],
    "thus": ["<REV>because",],
    # COMPARISON:Contrast
    "by/in comparison": ["while"],
    "by/in contrast": ["although", "while"],
    "conversely": [],
    "on the other hand": [],
    "nevertheless": ["<REV>although", "<REV>even though"],
    # EXPANSION:Conjunction
    "additionally": [],
    "also": [],
    "in addition": ["in addition to"],
    "furthermore": [],
    "moreover": [],
    "besides": ["besides"],
    "likewise": [],
    "similarly": ["while"],
    # EXPANSION:Instantiation
    "for example": [],
    "for instance": [],
    "in particular": [],
    # EXPANSION:Alternative
    "instead": [],
    "rather": [],
}