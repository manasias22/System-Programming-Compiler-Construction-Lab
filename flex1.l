%{
#include<stdio.h>
%}

%%
int | float | 
printf { printf("%s : Keyword\n", yytext); }
[+*-/=] { printf("%s : Operator\n", yytext); }
[0-9]+ { printf("%s : Number\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("%s : Identifier\n", yytext); }
.|\n {ECHO;}
%%

int main()
{

	printf("\nEnter the string: ");
	yylex();


}

int yywrap()
{
	return 1;
}