""" The program will define a BNF syntax and read records from a file """

# Grammer attributes    
SEP = ':='
DELIMITER = '\n'

# Open file
def open_file(file_path):
    try:
        f = open("records.txt" , "r")
        return f
    except Exception as error:
        print(f"Error while opening the file {error=}")
        return error
    
def bnf_grammar(grammar, sep=SEP, delimiter=DELIMITER, main=None):
        """ Generate a series of rules from a grammar. Grammars should
        be given as a series of lines delineated by a newline, or
        whatever is passed as delimiter. Each line should contain a rule
        name and a definition separated by the ":=", or whatever
        is passed as the separator.
        Rules obey the same rules as the new_rule method of the parser.
        In short, give a space-delimited series of rule names or 
        literals, which must be surrounded by quote marks. See the
        new_rule function for more information.
        
        Use the main parameter to specify one function as the main for
        the parser, i.e. the first function called when parsing.
        """
        for rule in grammar.strip().split(delimiter):
            name, parts = rule.split(SEP)
            name = name.strip()
            new_rule(name, parts.strip())


            
rules_data = open_file("rules.txt")
bnf_grammar(rules_data)