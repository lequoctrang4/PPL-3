
from Visitor import Visitor
from abc import ABC, abstractmethod, ABCMeta
from AST import *
from StaticError import *
from functools import *
from typing import List, Tuple
class Symbol:
    name: str
    typ: Type
    params: List['Symbol'] = None
    returnType: Type = None
    inherit: str or bool = None
    def __init__(self, name, typ, params = None, returnType = None, inherit = None):
        self.name = name
        self.typ = typ
        self.params = params
        self.returnType = returnType
        self.inherit = inherit
    def __repr__(self):
        return (
            "Symbol("
            + str(self.name)
            + ", "
            + str(self.typ)
            + str(self.params_to_str())
            + str(self.return_to_str())
            + str(self.return_inherit())
            +')'
        )
    def params_to_str(self):
        if self.params:
            s = ""
            for param in self.params.value:
                s = (
                    s + ", " + str(param)
                    if param != self.params.value[0]
                    else s + str(param)
                )
            return ", Params([" + s + "])"
        else:
            return ""
    def return_to_str(self):
        if self.returnType:
            return ", ReturnType(" + str(self.returnType) + ")"
        else:
            return ""
    def return_inherit(self):
        if self.inherit:
            return ", Inherit(" + str(self.inherit) + ")"
        else:
            return ""
class Wrapper:
    def __init__(self, value):
        self.value = value
    def __repr__(self) -> str:
        return "Wrapper(" + str(self.value) + ")"
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.param = [
            Symbol(
                "readInteger",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(IntegerType())
            ),
            Symbol(
                "printInteger",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(IntegerType()))]),
                Wrapper(VoidType())
            ),
            Symbol(
                "readFloat",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(FloatType())
            ),
            Symbol(
                "writeFloat",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(FloatType()))]),
                Wrapper(VoidType())
            ),
            Symbol(
                "readBoolean",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(BooleanType())
            ),
            Symbol(
                "printBoolean",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(BooleanType()))]),
                Wrapper(VoidType())
            ),
            Symbol(
                "readString",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(StringType())
            ),
            Symbol(
                "printString",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(StringType()))]),
                Wrapper(VoidType())
            ),
            Symbol(
                "super",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(StringType())
            ),
            Symbol(
                "preventDefault",
                Wrapper(Function()),
                Wrapper([]),
                Wrapper(VoidType())
            )
        ]
        self.env = self.param
    def check(self):
        return self.visit(self.ast, self.param)
    def checkNoEntryPoint(self, param):
        for symbol in param:
            if isinstance(symbol, Symbol) and isinstance(symbol.typ.value, Function) and isinstance(symbol.returnType.value, VoidType) and symbol.name == "main":
                return
        raise NoEntryPoint()
    def getSymbol(self, name, param):
        for symbol in param:
            if not isinstance(symbol, list) and name == symbol.name:
                return symbol
        return False
    def getSymbolAllScope(self, name, param):
        for symbol in param:
            if isinstance(symbol, list):
                return self.getSymbolAllScope(name, symbol)
            if name == symbol.name:
                return symbol
        return False
    def getFunc(self, param):
         for symbol in param:
            if isinstance(symbol, list):
                return self.getFunc(symbol)
            if isinstance(symbol.typ.value, Function):
                return symbol
    def visitIntegerType(self, ast, param):
        return Wrapper(IntegerType())
    def visitFloatType(self, ast, param):
        return Wrapper(FloatType())
    def visitBooleanType(self, ast, param):
        return Wrapper(BooleanType())
    def visitStringType(self, ast, param):
        return Wrapper(StringType())
    def visitArrayType(self, ast, param):
        dimen = ast.dimensions
        typ = self.visit(ast.typ, param)
        return Wrapper(ArrayType(dimen, typ))
    def visitAutoType(self, ast, param):
        return Wrapper(AutoType())
    def visitVoidType(self, ast, param):
        return Wrapper(VoidType())
    def visitBinExpr(self, ast, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        op = ast.op
        if op in ['+', '-', '*', '/']:
            #Suy diễn kiểu cho hàm auto
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if not (type(left.value) in [IntegerType, FloatType, AutoType] and type(right.value) in  [IntegerType, FloatType, AutoType]):
                raise TypeMismatchInExpression(ast)
            if isinstance(left, FloatType) or isinstance(right, FloatType):
                return Wrapper(FloatType())
            return left
        if op in ['%']:
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if isinstance(left.value, AutoType) and isinstance(right.value, AutoType):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            elif not (isinstance(left.value, IntegerType) and isinstance(right.value, IntegerType)):
                raise TypeMismatchInExpression(ast)
            return left
        if op in ['&&', '||']:
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if isinstance(left.value, AutoType) and isinstance(right.value, AutoType):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            elif not (isinstance(left.value, BooleanType) and isinstance(right.value, BooleanType)):
                raise TypeMismatchInExpression(ast)
            return Wrapper(BooleanType())
        if op in ['::']:
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if isinstance(left.value, AutoType) and isinstance(right.value, AutoType):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            elif not (isinstance(left.value, StringType) and isinstance(right.value, StringType)):
                raise TypeMismatchInExpression(ast)
            return left
        if op in ['==', '!=']:
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if isinstance(left.value, AutoType) and isinstance(right.value, AutoType):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            elif not (type(left.value) in [IntegerType, BooleanType] and type(right.value) in  [IntegerType, BooleanType]):
                raise TypeMismatchInExpression(ast)
            return Wrapper(BooleanType())
        if op in ['<', '>', '<=', '>=']:
            if isinstance(left.value, AutoType):
                left.value = right.value
            elif isinstance(right.value, AutoType):
                right.value = left.value
            if isinstance(left.value, AutoType) and isinstance(right.value, AutoType):
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pass
            elif not (type(left.value) in [IntegerType, FloatType] and type(right.value) in  [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)
            return Wrapper(BooleanType())        
    def visitUnExpr(self, ast, param):
        op = ast.op
        val = self.visit(ast.val, param)
        if op in ['-']:
            if type(val.value) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ast)
            return val
        if op in ['!']:
            if type(val.value) not in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ast)
            return val    
    def visitArrayCell(self, ast, param):
        id = ast.name;
        arraySymbol = self.getSymbolAllScope(id, param)
        if not arraySymbol:
            raise Undeclared(Identifier(), id)
        arraySymbolType = arraySymbol.typ
        #Check type
        if not isinstance(arraySymbolType.value, ArrayType):
            raise TypeMismatchInExpression(ast)
        #Check length array!!!!!!
        if len(arraySymbolType.value.dimensions) is not len(ast.cell):
            raise TypeMismatchInExpression(ast)
        #Check cell > diemsions?
        
        #Check index array must be integer
        for index in ast.cell:
            indexType = self.visit(index, param)
            if not isinstance(indexType.value, IntegerType):
                raise TypeMismatchInExpression(ast)
        #return type of array[index]
        return arraySymbolType.value.typ
    def visitId(self, ast, param):
        symbol = self.getSymbolAllScope(ast.name, param)
        if not symbol:
            raise Undeclared(Identifier(), ast.name)
        return symbol.typ
    def visitIntegerLit(self, ast, param):
        return Wrapper(IntegerType())
    def visitFloatLit(self, ast, param):
        return Wrapper(FloatType())
    def visitStringLit(self, ast, param):
        return Wrapper(StringType())
    def visitBooleanLit(self, ast, param):
        return Wrapper(BooleanType())
    def visitArray(self, ast, param):
        elems = ast.explist
        if not len(elems):
            return ArrayType([0], Type())
        elemsType = self.visitArray(elems[0], param) if isinstance(elems[0], ArrayLit) else self.visit(elems[0], param)
        for i in range(1,len(elems)):
            elemType = self.visitArray(elems[i], param) if isinstance(elems[i], ArrayLit) else self.visit(elems[i], param)
            if isinstance(elemType.value, AutoType):
                elemType.value = elemsType.value
            elif isinstance(elemsType.value, AutoType):
                elemsType.value = elemType.value
            elif isinstance(elemsType.value, FloatType) and isinstance(elemType.value, IntegerType):
                pass
            elif isinstance(elemType.value, FloatType) and isinstance(elemsType.value, IntegerType):
                elemsType = elemType
            elif not isinstance(elemType.value, type(elemsType.value)):
                raise IllegalArrayLiteral(ast)
            if isinstance(elemType.value, ArrayType) and (elemsType.value.dimensions != elemType.value.dimensions):
                raise IllegalArrayLiteral(ast)
        dimensions = [len(elems)] + (
            elemsType.value.dimensions if type(elemsType.value) is ArrayType else []
        )        
        while isinstance(elemsType.value, ArrayType):
            elemsType.value = elemsType.value.typ.value
        return Wrapper(ArrayType(dimensions, elemsType))  
    def checkTypeArray(self, ast, typ, param):
        elems = ast.explist
        for x in elems:
            if isinstance(x, ArrayLit):
                if not self.checkTypeArray(x, typ, param):
                    return False
            else:
                a = self.visit(x, param)
                if isinstance(a.value, AutoType):
                    a.value = typ.value
                elif isinstance(a.value, IntegerType) and isinstance(typ.value, FloatType):
                    pass
                elif not isinstance(a.value, type(typ.value)):
                    return False
        return True      
    def visitArrayLit(self, ast, param):
        a = self.visitArray(ast, param)
        if not self.checkTypeArray(ast, a.value.typ, param):
            raise IllegalArrayLiteral(ast)  
        return a
    def visitFuncCall(self, ast, param):
        #call a function and return a symbol function
        variable = ast.name
        if variable in ['super', 'preventDefault']:
            func = self.getFunc(param)
            raise InvalidStatementInFunction(func.name)
        funcSymbol = self.getSymbolAllScope(variable, param)
        if not funcSymbol:
            raise Undeclared(Function(), variable)
        if not isinstance(funcSymbol.typ.value, Function):
            raise TypeMismatchInExpression(ast)
        #Kiểm tra length param func với gọi hàm
        if len(funcSymbol.params.value) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        args = [self.visit(x, param) for x in ast.args]
        
        #Kiểm tra kiểu của parameter
        for i in range(0, len(args)):
            if isinstance(funcSymbol.params.value[i].typ.value, AutoType):
                funcSymbol.params.value[i].typ.value = args[i].value
            elif isinstance(funcSymbol.params.value[i].typ.value, FloatType) and isinstance(args[i].value, IntegerType):
                pass
            elif not isinstance(funcSymbol.params.value[i].typ.value, type(args[i].value)):
                raise TypeMismatchInStatement(ast)
        #Trả về một Func
        return funcSymbol.returnType
    def visitAssignStmt(self, ast, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        if not (isinstance(lhs.value, AtomicType) or isinstance(lhs.value, AutoType)):
            raise TypeMismatchInStatement(ast)
        if isinstance(lhs.value, AutoType):
            lhs.value = rhs.value
        if isinstance(rhs.value, AutoType):
            rhs.value = lhs.value
        if isinstance(lhs.value, FloatType):
            if type(rhs.value) not in [FloatType, IntegerType]:
                raise TypeMismatchInStatement(ast)
        elif str(lhs.value) != str(rhs.value):            
            raise TypeMismatchInStatement(ast)
        return lhs
    def visitBlockStmt(self, ast, param, para = None):
        param = [param]
        if para:
            param = para + param
        for stmt in ast.body:
            if isinstance(stmt, ReturnStmt):
                param = [self.visit(stmt, param)]+ param 
            elif isinstance(stmt, Stmt):
                self.visit(stmt, param)
            else:
                param = [self.visit(stmt, param)] + param
    def visitIfStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond.value, BooleanType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, param)
        if ast.fstmt:
            self.visit(ast.fstmt, param)
    def visitForStmt(self, ast, param):
        init = self.visit(ast.init, param)
        cond = self.visit(ast.cond, param)
        upd = self.visit(ast.upd, param)
        if not isinstance(init.value, IntegerType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(cond.value, BooleanType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(upd.value, IntegerType):
            raise TypeMismatchInStatement(ast)
        symbol = Symbol('', Wrapper(Stmt()))
        param = [symbol] + param
        self.visit(ast.stmt, param)
    def visitWhileStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond.value, BooleanType):
            raise TypeMismatchInStatement(ast)
        symbol = Symbol('', Wrapper(Stmt()))
        param = [symbol] + param
        self.visit(ast.stmt, param)
    def visitDoWhileStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond.value, BooleanType):
            raise TypeMismatchInStatement(ast)
        symbol = Symbol('', Wrapper(Stmt()))
        param = [symbol] + param
        self.visit(ast.stmt, param)
    def visitBreakStmt(self, ast, param):
        if not self.getSymbolAllScope('', param):
            raise MustInLoop(ast)
    def visitContinueStmt(self, ast, param):
        if not self.getSymbolAllScope('', param):
            raise MustInLoop(ast)
    def visitReturnStmt(self, ast, param):
        func = self.getFunc(param)
        if self.getSymbolAllScope('-returnStmt', param):
            return []
        if ast.expr:
            typReturn = self.visit(ast.expr, param)
            if isinstance(typReturn.value, AutoType):
                typReturn.value = func.returnType.value
        if ast.expr and isinstance(func.returnType.value, AutoType):
            func.returnType.value = typReturn.value
        elif ast.expr and isinstance(func.returnType.value, FloatType) and isinstance(typReturn.value, IntegerType):
            pass
        elif ast.expr and not isinstance(func.returnType.value, type(typReturn.value)):
            raise TypeMismatchInStatement(ast)
        
        return Symbol('-returnStmt', Wrapper(Stmt()))
    def visitCallStmt(self, ast, param):
        FuncType = self.visitFuncCall(ast, param)
        # if isinstance(FuncType.value, AutoType):
        #     FuncType.value = VoidType()
        return FuncType
    def visitVarDecl(self, ast, param):
        variable = ast.name
        typ = self.visit(ast.typ, param)
        if self.getSymbol(variable, param) or self.getSymbol(variable, self.env):
            raise Redeclared(Variable(), variable)
        if not ast.init:
            #Check if not init and with auto -> raise error
            if isinstance(typ.value, AutoType) or (isinstance(typ.value, ArrayType) and isinstance(typ.value.typ.value, AutoType)):
                raise Invalid(Variable(), variable)
            vardecl = Symbol(name = variable, typ = typ)
        elif ast.init:
            initType = self.visit(ast.init, param)
            if isinstance(typ.value, AutoType):
                vardecl = Symbol(name = variable, typ = initType)
            elif isinstance(initType.value, AutoType): #Lúc này init là Function
                initType.value = typ.value
                vardecl = Symbol(name = variable, typ = typ)
            elif isinstance(initType.value, IntegerType) and isinstance(typ.value, FloatType):
                vardecl = Symbol(name = variable, typ = typ)
                #Có chuyển đổi kiểu của initType không?
            else:
                if isinstance(typ.value, FloatType) and isinstance(initType.value, IntegerType):
                    pass                    
                if str(initType.value) != str(typ.value):
                        raise TypeMismatchInVarDecl(ast)
                vardecl = Symbol(name = variable, typ = typ)
        
        return vardecl
    def createParameter(self, ast, param):
        variable = ast.name
        typ = self.visit(ast.typ, param)
        inherit = ast.inherit
        varDecl = Symbol(name = variable, typ = typ, inherit = inherit)
        return varDecl
    def createFuncDecl(self, ast, param):
        variable = ast.name
        return_type = self.visit(ast.return_type, param)
        paramFunc = []
        varInherit = ast.inherit
        for parameter in ast.params:
            paramFunc = paramFunc + [self.createParameter(parameter, param)]
        funcDecl = Symbol(variable, Wrapper(Function()), Wrapper(paramFunc), return_type, varInherit)
        return funcDecl
    def visitParamDecl(self, ast, param):
        variable = ast.name
        typ = self.visit(ast.typ, param)
        inherit = ast.inherit
        varDecl = Symbol(name = variable, typ = typ, inherit = inherit)
        return varDecl
    def visitFuncDecl(self, ast, param):
        if self.getSymbol(ast.name, param) or self.getSymbol(ast.name, self.env):
            raise Redeclared(Function(), ast.name)
        paramFunc = []
        #getSymbol Inherit
        symbolFuncInherit = None
        paramInherit = []
        if ast.inherit:
            #Lấy func kế thừa
            symbolFuncInherit = self.getSymbolAllScope(ast.inherit, param)
            #Nếu không tìm thấy hàm func
            if not symbolFuncInherit or not isinstance(symbolFuncInherit.typ.value, Function):
                raise Undeclared(Function(), ast.inherit)
            paramInherit = list(filter(lambda x: x.inherit, symbolFuncInherit.params.value))
            checkRedecl = []
            for x in symbolFuncInherit.params.value:
                if self.getSymbol(x.name, checkRedecl):
                    raise Redeclared(Parameter(), x.name);
                checkRedecl = [x] + checkRedecl
        #Đi qua từng param trong func
        cacheFunc = self.getSymbolAllScope(ast.name, param)
        for p in cacheFunc.params.value:
            if symbolFuncInherit and self.getSymbol(p.name, paramInherit):
                raise Invalid(Parameter(), p.name)
            if self.getSymbol(p.name, paramFunc) or self.getSymbol(p.name, self.env):
                raise Redeclared(Parameter(), p.name)
            paramFunc = [p] + paramFunc
        return_type = cacheFunc.returnType;
        funcDecl = Symbol(ast.name, Wrapper(Function()), Wrapper(paramFunc), return_type, ast.inherit)
        if symbolFuncInherit:
            supper = ast.body.body
            if  len(supper) and isinstance(supper[0], CallStmt) and supper[0].name =='super':
                args = [self.visit(x, param) for x in supper[0].args]
                if len(args) > len(symbolFuncInherit.params.value):
                    raise TypeMismatchInExpression(supper[0].args[len(symbolFuncInherit.params.value)])
                elif len(args) < len(symbolFuncInherit.params.value):
                    raise TypeMismatchInExpression()
                else: 
                    for i in range(0, len(args)):
                        if isinstance(symbolFuncInherit.params.value[i].typ.value, AutoType):
                            symbolFuncInherit.params.value[i].typ.value = args[i].value
                        elif isinstance(symbolFuncInherit.params.value[i].typ.value, FloatType) and isinstance(args[i].value, IntegerType):
                            pass
                        elif not isinstance(symbolFuncInherit.params.value[i].typ.value, type(args[i].value)):
                            raise TypeMismatchInExpression(supper[0].args[i])
                supper.pop(0)
            elif len(supper) and isinstance(supper[0], CallStmt) and supper[0].name =='preventDefault':
                if len(supper[0].args) > 0:
                    raise TypeMismatchInExpression(supper[0].args[0])
                supper.pop(0)
            elif len(checkRedecl): 
                raise InvalidStatementInFunction(ast.name)
        env = paramFunc + paramInherit
        self.visitBlockStmt(ast.body, [funcDecl] +  param, env)
        return funcDecl
    def visitProgram(self, ast, param):
        #Check reclared variables global scope
        for decl in ast.decls:
            if isinstance(decl, FuncDecl):
                param = [self.createFuncDecl(decl, param)] + param
        param =[] + [param]
        for decl in ast.decls:
            if isinstance(decl, VarDecl):
                param = [self.visit(decl, param)] + param
            if isinstance(decl, FuncDecl):
                param = [self.visit(decl, param)] + param
        self.checkNoEntryPoint(param)                    