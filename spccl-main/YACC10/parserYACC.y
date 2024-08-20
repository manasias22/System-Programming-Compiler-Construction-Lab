%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%

calc    : expr '\n'   { printf("Valid expression\n"); }
        ;

expr    : expr '+' term   { }
        | expr '-' term   { }
        | term             { }
        ;

term    : term '*' factor { }
        | term '/' factor { }
        | factor           { }
        ;

factor  : NUMBER          { }
        | '(' expr ')'    { }
        ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter an arithmetic expression:\n");
    yyparse();
    return 0;
}


/*save these 2 files with parser.l and parserYACC.y*/

/*flex parser.l*/

/*bison -dy parserYACC.y*/

/*gcc lex.yy.c y.tab.c*/

/*a.exe*/