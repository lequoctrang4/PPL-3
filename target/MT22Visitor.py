# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decVar.
    def visitDecVar(self, ctx:MT22Parser.DecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decVar1.
    def visitDecVar1(self, ctx:MT22Parser.DecVar1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeAssign.
    def visitTypeAssign(self, ctx:MT22Parser.TypeAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimen.
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elementType.
    def visitElementType(self, ctx:MT22Parser.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decVar2.
    def visitDecVar2(self, ctx:MT22Parser.DecVar2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varList.
    def visitVarList(self, ctx:MT22Parser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func.
    def visitFunc(self, ctx:MT22Parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decFunc.
    def visitDecFunc(self, ctx:MT22Parser.DecFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodyFunction.
    def visitBodyFunction(self, ctx:MT22Parser.BodyFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtList.
    def visitStmtList(self, ctx:MT22Parser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignStmt.
    def visitAssignStmt(self, ctx:MT22Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elseStmt.
    def visitElseStmt(self, ctx:MT22Parser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elseIfStmt.
    def visitElseIfStmt(self, ctx:MT22Parser.ElseIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx:MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr0.
    def visitExpr0(self, ctx:MT22Parser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literals.
    def visitLiterals(self, ctx:MT22Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationOp.
    def visitRelationOp(self, ctx:MT22Parser.RelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalOp.
    def visitLogicalOp(self, ctx:MT22Parser.LogicalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addingOp.
    def visitAddingOp(self, ctx:MT22Parser.AddingOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#muldivOp.
    def visitMuldivOp(self, ctx:MT22Parser.MuldivOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signOp.
    def visitSignOp(self, ctx:MT22Parser.SignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexArray.
    def visitIndexArray(self, ctx:MT22Parser.IndexArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcCall.
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprList.
    def visitExprList(self, ctx:MT22Parser.ExprListContext):
        return self.visitChildren(ctx)



del MT22Parser