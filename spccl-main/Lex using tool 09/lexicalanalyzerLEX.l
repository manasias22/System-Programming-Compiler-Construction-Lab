%{
#include<stdio.h>
int yylineno = 1;
%}


letter[a-zA-Z]
digit[0-9]

%%
\n                                                   yylineno++;
#include<{letter}+(\.{letter}*)?>                    printf("%d\t%s\t\tPREPROCESSOR\n",yylineno,yytext);
return|main|for|while|case|switch|if|else            printf("%d\t%s\t\t\t\tKEYWORD\n",yylineno,yytext);
int|float|char|struct                                printf("%d\t%s\t\t\t\tDATATYPE\n",yylineno,yytext);
\(                                                   printf("%d\t%s\t\t\t\tOPEN BRACKET\n",yylineno,yytext);
\)                                                   printf("%d\t%s\t\t\t\tCLOSE BRACKET\n",yylineno,yytext);
{letter}({letter}|{digit})*                          printf("%d\t%s\t\t\t\tIDENTIFIER\n",yylineno,yytext);
{digit}+                                             printf("%d\t%s\t\t\t\tINTEGERn",yylineno,yytext);
\{                                                   printf("%d\t%s\t\t\t\tOPEN BRACE\n",yylineno,yytext);
\}                                                   printf("%d\t%s\t\t\t\tCLOSE BRACE\n",yylineno,yytext);
{digit}+"E"(\+|\-)?{digit}+                          printf("%d\t%s\t\t\t\tREAL NUMBER\n",yylineno,yytext);
{digit}+\.{digit}+(E(\+|\-)?{digit}+)?               printf("%d\t%s\t\t\t\tFLOATING NUMBER\n",yylineno,yytext);
=                                                    printf("%d\t%s\t\t\t\tASSIGNMENT\n",yylineno,yytext);
;                                                    printf("%d\t%s\t\t\t\tTERMINATOR\n",yylineno,yytext);
\t                                                   ;
" "                                                  ;
\"({letter}|{digit}|" ")*\"                          printf("%d\t%s\t\t\tSTRING CONSTANT\n",yylineno,yytext);




%%

int yywrap(){
return 1;
}

int main(int argc, char * argv[]){
   yyin=fopen(argv[1],"r");
   printf("LINE\tLEXME\t\t\t\tTOKEN\n");
   yylex();
   fclose(yyin);
   return 0;
}


#save this above file as lexicalanalyzerLEX.l 



