from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce


class ASTGeneration(MT22Visitor):
    def flatten(self, lst: list):
        return reduce(lambda prev, curr: prev + (self.flatten(curr) if type(curr) is list else [curr]), lst, [])
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        size = len(ctx.decVar() + ctx.func())
        rs = [self.visit(ctx.getChild(i)) for i in range(size)]
        return Program(self.flatten(rs))
    # def visitProgram(self, ctx: MT22Parser.ProgramContext):             
    #     return Program(self.flatten(self.visit(ctx.trang())))
    # def visitTrang(self, ctx: MT22Parser.TrangContext):             
    #     if ctx.getChildCount() == 2:
    #         rs =  [self.visit(ctx.decVar())] if ctx.decVar() else  [self.visit(ctx.func())]
    #         return rs + self.visit(ctx.trang())
    #     return [self.visit(ctx.decVar())] if ctx.decVar() else  [self.visit(ctx.func())]
    
    def visitDecVar(self, ctx: MT22Parser):
        if ctx.decVar1() and ctx.SM():
            arr = self.visit(ctx.decVar1())
            type = arr[-1]
            arr.pop(len(arr) - 1)
            for x in range(int(len(arr) / 2)):
                value = arr[x][1]
                arr[x] = ( arr[x][0], arr[len(arr) - x - 1][1])
                arr[len(arr) - x - 1] = (arr[len(arr) - x - 1][0],value)
            listdec = [VarDecl(x[0], type, x[1]) for x in arr]
            return listdec
        elif ctx.decVar2():
            return self.visit(ctx.decVar2())

    def visitDecVar1(self, ctx: MT22Parser.DecVar1Context):
        if ctx.decVar1():
            return [(ctx.IDENTIFIER().getText(), self.visit(ctx.expr()))] + self.visit(ctx.decVar1())
        else:
            return [(ctx.IDENTIFIER().getText(), self.visit(ctx.expr())), self.visit(ctx.typeAssign())];

    def visitTypeAssign(self, ctx: MT22Parser.TypeAssignContext):
        if ctx.getChildCount() > 1:
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.elementType()))
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.elementType())
    
    def visitDimen(self, ctx: MT22Parser.DimenContext):
        return [x.getText() for x in ctx.INTEGER()]

    def visitElementType(self, ctx: MT22Parser.ElementTypeContext):
        if ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BooleanType()

    def visitDecVar2(self, ctx: MT22Parser.DecVar2Context):
        listvar = self.visit(ctx.varList())
        typeassign = self.visit(ctx.typeAssign())
        return [VarDecl(name, typeassign, None) for name in listvar]

    def visitVarList(self, ctx: MT22Parser.VarListContext):
        if ctx.varList():
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.varList())
        return [ctx.IDENTIFIER().getText()]

    def visitFunc(self, ctx: MT22Parser.FuncContext):
        lhs = self.visit(ctx.decFunc())
        rs = self.visit(ctx.bodyFunction())
        return FuncDecl(lhs[0], lhs[1], lhs[2], lhs[3], rs)

    def visitDecFunc(self, ctx: MT22Parser.DecFuncContext):
        name = ctx.IDENTIFIER(0).getText()
        return_type = self.visit(ctx.typeAssign()) if ctx.typeAssign() else VoidType()
        params = self.visit(ctx.parameter()) if ctx.parameter() else []
        inherit = None if not ctx.INHERIT() else ctx.IDENTIFIER(1).getText()
        return [name, return_type, params, inherit]

    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        name = ctx.IDENTIFIER().getText()
        type = self.visit(ctx.typeAssign())
        if ctx.parameter():
            return [ParamDecl(name, type, out, inherit)] + self.visit(ctx.parameter())
        return [ParamDecl(name, type, out, inherit)]

    def visitBodyFunction(self, ctx: MT22Parser.BodyFunctionContext):
        return self.visit(ctx.blockStmt())

    def visitStmtList(self, ctx: MT22Parser.StmtListContext):
        size = len(ctx.stmt() + ctx.decVar())
        rs = [self.visit(ctx.getChild(i)) for i in range(size)]
        return self.flatten(rs)

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.blockStmt():
            return self.visit(ctx.blockStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.doWhileStmt():
            return self.visit(ctx.doWhileStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        return BlockStmt(self.visit(ctx.stmtList()))
             
    def visitAssignStmt(self, ctx: MT22Parser.AssignStmtContext):
        if ctx.indexArray():
             lhs = ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.indexArray()))
        else : lhs = Id(ctx.IDENTIFIER().getText())
        rhs = self.visit(ctx.expr()) if ctx.expr() else ''
        return AssignStmt(lhs, rhs)
        

    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        expr = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt())
        if ctx.elseIfStmt():
            fstmt = self.visit(ctx.elseIfStmt())
        elif ctx.elseStmt():
            fstmt = self.visit(ctx.elseStmt())
        else : fstmt = None
        return IfStmt(expr, tstmt, fstmt)
    
    def visitElseIfStmt(self, ctx: MT22Parser.ElseIfStmtContext):
        return self.visit(ctx.ifStmt())
        
    def visitElseStmt(self, ctx: MT22Parser.ElseStmtContext):
        return self.visit(ctx.stmt())

    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        id =  ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.indexArray())) if ctx.indexArray() else Id(ctx.IDENTIFIER().getText())
        return ForStmt(AssignStmt(id, self.visit(ctx.expr(0))),
                           self.visit(ctx.expr(1)), 
                           self.visit(ctx.expr(2)),
                           self.visit(ctx.stmt()))

    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockStmt())
        return DoWhileStmt(expr, stmt)

    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        func_call = self.visit(ctx.funcCall())
        return CallStmt(func_call.name, func_call.args)

    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return BreakStmt();

    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        return ContinueStmt();

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.expr0(0))
            right = self.visit(ctx.expr0(1))
            op = ctx.CONCAT().getText()
            return BinExpr(op, left, right)
        return self.visit(ctx.expr0(0))

    def visitExpr0(self, ctx: MT22Parser.Expr0Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            op = self.visit(ctx.relationOp())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr1(0))
    
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.expr1():
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            op = self.visit(ctx.logicalOp())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr2())

    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.expr2():
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            op = self.visit(ctx.addingOp())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr3())

    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.expr3():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            op = self.visit(ctx.muldivOp())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr4())

    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            body = self.visit(ctx.expr4())
            return UnExpr(op, body)
        return self.visit(ctx.expr5())

    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.signOp():
            return UnExpr(self.visit(ctx.signOp()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.IDENTIFIER():
            return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.indexArray()))
        return self.visit(ctx.expr7())

    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.expr8())

    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.funcCall():
            return self.visit(ctx.funcCall())
    
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.INTEGER():
            return IntegerLit(ctx.INTEGER().getText())
        if ctx.FLOATLITERAL():
            return FloatLit(float('0' + ctx.FLOATLITERAL().getText()))
        if ctx.STRINGLITERAL():
            return StringLit(ctx.STRINGLITERAL().getText())
        if ctx.BOOLEAN():
            return BooleanLit(1 if ctx.BOOLEAN().getText() == "true" else 0)
        return self.visit(ctx.array())
    
    def visitArray(self, ctx: MT22Parser.ArrayContext):
        if ctx.getChildCount() == 3:
            return ArrayLit(self.visit(ctx.literals()))
        return ArrayLit([])

    def visitLiterals(self, ctx: MT22Parser.LiteralsContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitRelationOp(self, ctx: MT22Parser.DecVarContext):
        return  ctx.getChild(0).getText()

    def visitLogicalOp(self, ctx: MT22Parser.LogicalOpContext):
        return ctx.getChild(0).getText()

    def visitAddingOp(self, ctx: MT22Parser.AddingOpContext):
        return ctx.getChild(0).getText()

    def visitMuldivOp(self, ctx: MT22Parser.MuldivOpContext):
        return ctx.getChild(0).getText() 

    def visitSignOp(self, ctx: MT22Parser.SignOpContext):
        return ctx.SUB().getText()

    def visitIndexArray(self, ctx: MT22Parser.IndexArrayContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitFuncCall(self, ctx: MT22Parser.FuncCallContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprList()) if ctx.exprList() else []
        return FuncCall(id, expr)

    def visitExprList(self, ctx: MT22Parser.ExprListContext):
        if ctx.getChildCount() > 1:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprList())
        return [self.visit(ctx.expr())]

