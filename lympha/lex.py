#variable name ( specification) = content
\regex{($\backslash$w*$[$a-zA-Z]$\backslash$w*$\backslash$.)$\backslash$(\textasciicircum[\textasciicircum$\backslash$)]*?(?=$\backslash$))?$\backslash$s*?=$\backslash$s*?(\textasciicircum[\textasciicircum ;]*?(?=;))}

#datatype [ sub-variable name ] = content
\regex{($\backslash$w*$[$a-zA-Z]$\backslash$w*$\backslash$)$\backslash$[\textasciicircum[\textasciicircum$\backslash$]]*?(?=$\backslash$])?$\backslash$s*?=$\backslash$s*?($\backslash$w*$[$a-zA-Z]$\backslash$w*$\backslash$)}

#{ event , factor , event }
[x.strip() for x in content.split(',')]

#tipping point   relational operator | {  sub-factor , sub-factor} |
\regex{($\backslash$d)$\backslash$s*?(==|>|<|>=|<=)$\backslash$s*?\{($\backslash$w*$[$a-zA-Z]$\backslash$w*$\backslash$)\}}

