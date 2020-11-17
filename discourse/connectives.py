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
        "further(more)": "^furthermore", # followed by pronoun if just "further"?
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