grammar OrdenesServicios;

script         : (command SEMICOLON)* EOF;

command
    : loadCmd
    | filterCmd
    | aggregateCmd
    | printCmd
    ;

loadCmd        : LOAD STRING;
filterCmd      : FILTER COLUMN STRING OPERATOR value (LOGIC_OP filterCmd)?;
aggregateCmd   : AGGREGATE aggFunc COLUMN STRING;
printCmd       : PRINT;

aggFunc        : COUNT | SUM | AVERAGE | BETWEEN;

value          : NUMBER | STRING;

LOAD           : 'load';
FILTER         : 'filter';
COLUMN         : 'column';
AGGREGATE      : 'aggregate';
PRINT          : 'print';
COUNT          : 'count';
SUM            : 'sum';
AVERAGE        : 'average';
BETWEEN        : 'between';

OPERATOR       : '>=' | '<=' | '>' | '<' | '==' | '!=';
LOGIC_OP       : 'AND' | 'OR';

STRING         : '"' (~["\r\n])* '"';
NUMBER         : [0-9]+;

SEMICOLON      : ';';

WS             : [ \t\r\n]+ -> skip;
