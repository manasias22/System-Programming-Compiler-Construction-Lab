%{
#include "y.tab.h"
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[-+*/\n]    { return *yytext; }
[ \t]       ; // Ignore whitespace

.           { return yytext[0]; } // Any other character is returned as is

%%

int yywrap() {
    return 1;
}