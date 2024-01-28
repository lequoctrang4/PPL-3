grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: (decVar | func)+ EOF;

// program: trang EOF;
// trang: (decVar | func) trang | (decVar | func);

//Keywords

AUTO: 'auto';
INT: 'integer';
STRING: 'string';
BOOL: 'boolean';
FLOAT: 'float';
ARR: 'array';
BREAK: 'break';
DO: 'do';
ELSE: 'else';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
RETURN: 'return';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
//Operators

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
DIF: '!=';
LESS: '<';
BIGGER: '>';
LESSEQUAL: '<=';
MOREEQUAL: '>=';
CONCAT: '::';

//Separators

LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
POINT: '.';
CM: ',';
SM: ';';
CL: ':';
LPB: '{';
RPB: '}';
EQB: '=';

//Comment
COMMENT: '//' ~[\r\n]* -> skip;
COMMENTS: '/*' .*? '*/' -> skip;
// //Literals

BOOLEAN: 'true' | 'false';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INTEGER:
	'0'
	| [1-9] [0-9]* ('_' [0-9]+)* {
	self.text = self.text.replace('_','')
};

FLOATLITERAL: (
		INTPART THAPPHAN
		| INTPART MU
		| THAPPHAN MU
		| INTPART THAPPHAN MU
	) {
    self.text = self.text.replace('_','')
};

fragment INTPART: '0' | [1-9] [0-9]* ('_' [0-9]+)*;
fragment THAPPHAN: ('.' [0-9]*);
fragment MU: [eE][+-]? ( '0' | [1-9] [0-9]*);

fragment CHAR_STR: (~[\n"'\\] | '\\"' CHAR_STR* '\\"' | ESC_CHAR);
fragment ESC_CHAR: '\\' [btnfr'\\];
STRINGLITERAL:
	'"' CHAR_STR* '"' {
    self.text = self.text[1:-1]
};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_TOKEN:
	.{
	raise ErrorToken(self.text)
};
UNCLOSE_STRING:
	'"' CHAR_STR* ('\n' | EOF) {
    y = str(self.text)
    if y[-1] == '\n':
        raise UncloseString(y[1:-1])
    else:
        raise UncloseString(y[1:])
};

fragment ILL_CHAR: '\\' ~[btnfr'\\]| '\\';
ILLEGAL_ESCAPE:
	'"' CHAR_STR* ILL_CHAR {
    y = str(self.text)
    raise IllegalEscape(y[1:])
};

decVar: (decVar1 | decVar2) SM;
//Phép gán có đối số bằng nhau
decVar1:
	IDENTIFIER CL typeAssign EQB expr
	| IDENTIFIER CM decVar1 CM expr;
typeAssign: elementType | AUTO | ARR dimen OF elementType;
dimen: LSB INTEGER (CM INTEGER)* RSB;
elementType: INT | BOOL | STRING | FLOAT;
//Phép gán không gán đối số
decVar2: varList CL typeAssign;
varList: IDENTIFIER | IDENTIFIER CM varList; //

//function
func: decFunc bodyFunction; //
decFunc:
	IDENTIFIER CL FUNCTION (typeAssign | VOID) LRB parameter? RRB (
		INHERIT IDENTIFIER
	)?;
parameter: //
	INHERIT? OUT? IDENTIFIER CL typeAssign
	| INHERIT? OUT? IDENTIFIER CL typeAssign CM parameter;

bodyFunction: blockStmt; //
stmt:
	assignStmt
	| blockStmt
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt
	| callStmt
	| returnStmt
	| breakStmt
	| continueStmt;
blockStmt: LPB stmtList RPB;
stmtList: (stmt | decVar)*; //
assignStmt: IDENTIFIER indexArray? (EQB expr)? SM;
ifStmt: IF LRB expr RRB stmt (elseIfStmt | elseStmt)?;
elseStmt: ELSE stmt;
elseIfStmt: ELSE ifStmt;
forStmt: //
	FOR LRB IDENTIFIER indexArray? EQB expr CM expr CM expr RRB stmt;
whileStmt: WHILE LRB expr RRB stmt; //
doWhileStmt: DO blockStmt WHILE LRB expr RRB SM; //
continueStmt: CONTINUE SM; //
breakStmt: BREAK SM; //
callStmt: funcCall SM; //
returnStmt: RETURN expr? SM; //

expr: expr0 CONCAT expr0 | expr0; //
expr0: expr1 relationOp expr1 | expr1; //
expr1: expr1 logicalOp expr2 | expr2; //
expr2: expr2 addingOp expr3 | expr3; //
expr3: expr3 muldivOp expr4 | expr4; //
expr4: NOT expr4 | expr5; //
expr5: signOp expr5 | expr6; //
expr6: IDENTIFIER indexArray | expr7; //
expr7: LRB expr RRB | expr8; //
expr8: //
	literal
	| IDENTIFIER
	| funcCall;

literal:
	INTEGER
	| FLOATLITERAL
	| STRINGLITERAL
	| BOOLEAN
	| array; //

//array type
array: LPB literals RPB | LPB RPB; //
literals: expr (CM expr)*; //

relationOp:
	EQUAL
	| DIF
	| LESS
	| BIGGER
	| LESSEQUAL
	| MOREEQUAL; //
logicalOp: AND | OR; //
addingOp: ADD | SUB; //
muldivOp: MUL | DIV | MOD; //
signOp: SUB; //
indexArray: LSB expr (CM expr)* RSB; //
funcCall: IDENTIFIER LRB exprList? RRB; //
exprList: expr | expr CM exprList;