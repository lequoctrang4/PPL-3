import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """main:function void(){
                        if (x == 1){
                                
                        }
                        else{
                                
                        }
                }"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 1))
    def test2(self):
        input = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 2))
    
    def test3(self):
        input = """x,y,z: integer = 1,2,3;
        a,b: float;
        c: string;
        d: boolean;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, StringType)
	VarDecl(d, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 3))
    
    def test4(self):
        input = """x,y,z: integer = 1,2,3;
        a,b: float = 1.2, 1.3;
        c: string = "Hello, world";
        d: boolean = true;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, FloatType, FloatLit(1.3))
	VarDecl(c, StringType, StringLit(Hello, world))
	VarDecl(d, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 4))
    
    def test5(self):
        input = """
        arr : array [5] of float;
        arr : array [5] of integer;
        arr : array [5] of string;
        arr : array [5] of boolean;
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5], FloatType))
	VarDecl(arr, ArrayType([5], IntegerType))
	VarDecl(arr, ArrayType([5], StringType))
	VarDecl(arr, ArrayType([5], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 5))
    
    def test6(self):
        input = """
        arr : array [5] of float = {1,2,3};
        arr : array [5] of integer = {{1,2,3}, {1,2,3}};
        arr : array [5] of string = {};
        arr : array [5] of boolean = {"123"};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	VarDecl(arr, ArrayType([5], StringType), ArrayLit([]))
	VarDecl(arr, ArrayType([5], BooleanType), ArrayLit([StringLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 6))
    
    def test7(self):
        input = """
        arr : array [5] of float = {1,2,3};
        arr : array [5] of integer = {{1,2,3}, {1,2,3}};
        arr : array [5] of string = {};
        arr : array [5] of boolean = {"123"};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	VarDecl(arr, ArrayType([5], StringType), ArrayLit([]))
	VarDecl(arr, ArrayType([5], BooleanType), ArrayLit([StringLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 7))
    
    def test8(self):
        input = """
        arr : array [5] of integer = {1,2,3};
        arr : array [5] of integer = {{1,2,3}, {1,2,3}};
        arr : array [5] of string = {1.2, 3.9, true};
        arr : array [5] of boolean = {"123"};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	VarDecl(arr, ArrayType([5], StringType), ArrayLit([FloatLit(1.2), FloatLit(3.9), BooleanLit(True)]))
	VarDecl(arr, ArrayType([5], BooleanType), ArrayLit([StringLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 8))
    
    def test9(self):
        input = """
        arr : array [5,1,2,4] of integer = {1,2,3};
        arr : array [554] of integer = {{1,2,3}, {1,2,3}};
        arr : array [2,3,5] of string = {};
        arr : array [5,5] of boolean = {"123"};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5, 1, 2, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(arr, ArrayType([554], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	VarDecl(arr, ArrayType([2, 3, 5], StringType), ArrayLit([]))
	VarDecl(arr, ArrayType([5, 5], BooleanType), ArrayLit([StringLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 9))
                
    def test10(self):
        input = """
        a : integer = a;
        a : integer = c[f];
        a : integer = d[f[c[f]]];
        a: integer = func(func(func));
        arr : array [5] of integer = {{a,b[5],3 + 1}, {1,2,3}};
        arr : array [5] of integer = {a,f(), f(a+c)};
            """
        expect = """Program([
	VarDecl(a, IntegerType, Id(a))
	VarDecl(a, IntegerType, ArrayCell(c, [Id(f)]))
	VarDecl(a, IntegerType, ArrayCell(d, [ArrayCell(f, [ArrayCell(c, [Id(f)])])]))
	VarDecl(a, IntegerType, FuncCall(func, [FuncCall(func, [Id(func)])]))
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([ArrayLit([Id(a), ArrayCell(b, [IntegerLit(5)]), BinExpr(+, IntegerLit(3), IntegerLit(1))]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([Id(a), FuncCall(f, []), FuncCall(f, [BinExpr(+, Id(a), Id(c))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 10))
    
    def test11(self):
        input = """
                main: function void(){
                    
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 11))
    
    def test12(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 12))
        
    def test13(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 13))
    
    def test14(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a = 1;
                    a = "123";
                    a = 1.23;
                    a = {1,2,3,4};
                    a = true;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), StringLit(123)), AssignStmt(Id(a), FloatLit(1.23)), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), AssignStmt(Id(a), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 14))
    
    def test15(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    {
                        
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 15))
    
    
    def test16(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    {
                        {
                            {
                                
                            }
                        }
                    }
                    {
                        {
                            
                        }
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])]), BlockStmt([BlockStmt([])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 16))

    def test17(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    x,y,z: integer;
                    a,b: float;
                    c: string;
                    d: boolean;
                    a : auto;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, StringType), VarDecl(d, BooleanType), VarDecl(a, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 17))

    def test18(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    x,y,z: integer;
                    a,b: float;
                    {
                        c: string;  
                    }
                    d: boolean;
                    a : auto;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType), VarDecl(b, FloatType), BlockStmt([VarDecl(c, StringType)]), VarDecl(d, BooleanType), VarDecl(a, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 18))
    
    def test19(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    x,y,z: integer = 1,2,3;
                    a,b: float = 1.2, 1.3;
                    c: string = "Hello, world";
                    d: boolean = true;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, IntegerLit(3)), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, FloatType, FloatLit(1.3)), VarDecl(c, StringType, StringLit(Hello, world)), VarDecl(d, BooleanType, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 19))

    def test20(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    arr : array [5,1,2,4] of integer = {1,2,3};
                    arr : array [554] of integer = {{1,2,3}, {1,2,3}};
                    arr : array [2,3,5] of string = {};
                    arr : array [5,5] of boolean = {"123"};
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(arr, ArrayType([5, 1, 2, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(arr, ArrayType([554], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), VarDecl(arr, ArrayType([2, 3, 5], StringType), ArrayLit([])), VarDecl(arr, ArrayType([5, 5], BooleanType), ArrayLit([StringLit(123)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 20))
    
    def test21(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = a;
                    a : integer = c[f];
                    a : integer = d[f[c[f]]];
                    a: integer = func(func(func));
                    arr : array [5] of integer = {{a,b[5],3 + 1}, {1,2,3}};
                    arr : array [5] of integer = {a,f(), f(a+c)};
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, Id(a)), VarDecl(a, IntegerType, ArrayCell(c, [Id(f)])), VarDecl(a, IntegerType, ArrayCell(d, [ArrayCell(f, [ArrayCell(c, [Id(f)])])])), VarDecl(a, IntegerType, FuncCall(func, [FuncCall(func, [Id(func)])])), VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([ArrayLit([Id(a), ArrayCell(b, [IntegerLit(5)]), BinExpr(+, IntegerLit(3), IntegerLit(1))]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([Id(a), FuncCall(f, []), FuncCall(f, [BinExpr(+, Id(a), Id(c))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 21))

    def test22(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    if(true) return 1;
                    if(a == 2) return 3;
                    else if(a == 1) return 2;
                    else return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(3)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(2)), ReturnStmt(IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 22))
    
    def test23(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    if(true) {
                        a = 1;
                        a,b,c: integer;
                        a,b,c: integer = 1,2,3; 
                    }
                    if(a == 2) return 3;
                    else if(a == 1) return 2;
                    else return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))])), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(3)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(2)), ReturnStmt(IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 23))
    
    def test24(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    if(true) {
                        if(a){
                            
                        }
                        a = 1;
                        a,b,c: integer;
                        a,b,c: integer = 1,2,3; 
                    }
                    if(a == 2) return 3;
                    else if(a == 1) return 2;
                    else return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(Id(a), BlockStmt([])), AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))])), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(3)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(2)), ReturnStmt(IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 24))
        
    def test25(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    for(i = 2, i < 5, i + 1){
                        
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 25))
    
    def test26(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    for(i = 2, i < 5, i + 1){
                        for(j =0, j < 5 , j + 1){
                            print(x);
                        }
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, Id(x))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 26))
    
    def test27(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    for(i = 2, i < 5, i + 1){
                        for(j =0, j < 5 , j + 1){
                            {
                                a : integer;
                            }
                            a : integer = 1;
                            
                        }
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([BlockStmt([VarDecl(a, IntegerType)]), VarDecl(a, IntegerType, IntegerLit(1))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 27))
    
    def test28(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    while (true){
                        
                    }
                    while (true) return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([])), WhileStmt(BooleanLit(True), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 28))
    
    def test29(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    while (true){
                        
                    }
                    while (true){
                        a = 1;
                        a : integer = 1;
                        if ((a == 2) || (a == 3)){
                            return 0;
                        }
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([])), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(2)), BinExpr(==, Id(a), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 29))
    
    def test30(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    for(i = 2, i >5, i + 1){
                        a = 1;
                        a : integer = 1;
                        if ((a == 2) || (a == 3)){
                            return 0;
                        }
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(2)), BinExpr(==, Id(a), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 30))
    
    def test31(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = 0;
                    do{
                        if(a == 5) break;
                        f(a);
                        a = a + 1;
                    }while(a != 10);
                    return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BreakStmt()), CallStmt(f, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 31))
    
    def test32(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = 0;
                    do{
                        if(a == 5) break;
                        f(a);
                         for(i = 2, i >5, i + 1){
                            a = 1;
                            a : integer = 1;
                            if ((a == 2) || (a == 3)){
                                return 0;
                            }
                            {
                                
                            }
                        }
                        a = a + 1;
                    }while(a != 10);
                    return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BreakStmt()), CallStmt(f, Id(a)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(2)), BinExpr(==, Id(a), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(0))])), BlockStmt([])])), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 32))
    def test33(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = 0;
                    do{
                        if(a == 5) break;
                        f(a);
                         for(i = 2, i >5, i + 1){
                            a = 1;
                            a : integer = 1;
                            if ((a == 2) || (a == 3)){
                                return 0;
                            }
                            {
                                
                            }
                        }
                        for(i = 2, i >5, i + 1){
                            a = 1;
                            a : integer = 1;
                            if ((a == 2) || (a == 3)){
                                return 0;
                            }
                            {
                                
                            }
                        }
                        a = a + 1;
                    }while(a != 10);
                    return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BreakStmt()), CallStmt(f, Id(a)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(2)), BinExpr(==, Id(a), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(0))])), BlockStmt([])])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(2)), BinExpr(==, Id(a), IntegerLit(3))), BlockStmt([ReturnStmt(IntegerLit(0))])), BlockStmt([])])), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 33))
    
    def test34(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = 0;
                    do{
                        break;
                        a,b : float = 1, d;
                    }while(a != 10);
                    
                    return 0;
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([BreakStmt(), VarDecl(a, FloatType, IntegerLit(1)), VarDecl(b, FloatType, Id(d))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 34))
    
    def test35(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    f();
                    f(a,b,c,d);
                    f(f(f(f(a))));
                    return f(a);
                    f(a[5]);
                    f(a[1,2,3]);
                    f(1,2,3,-5,a);
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([CallStmt(f, ), CallStmt(f, Id(a), Id(b), Id(c), Id(d)), CallStmt(f, FuncCall(f, [FuncCall(f, [FuncCall(f, [Id(a)])])])), ReturnStmt(FuncCall(f, [Id(a)])), CallStmt(f, ArrayCell(a, [IntegerLit(5)])), CallStmt(f, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), CallStmt(f, IntegerLit(1), IntegerLit(2), IntegerLit(3), UnExpr(-, IntegerLit(5)), Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 35))
    
    def test36(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    f(5-4, a>b, a*b, {1,23,4,5,{}});
                    f(a>=b, a<=b, a == b, a != c);
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([CallStmt(f, BinExpr(-, IntegerLit(5), IntegerLit(4)), BinExpr(>, Id(a), Id(b)), BinExpr(*, Id(a), Id(b)), ArrayLit([IntegerLit(1), IntegerLit(23), IntegerLit(4), IntegerLit(5), ArrayLit([])])), CallStmt(f, BinExpr(>=, Id(a), Id(b)), BinExpr(<=, Id(a), Id(b)), BinExpr(==, Id(a), Id(b)), BinExpr(!=, Id(a), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 36))
    
    def test37(self):
        input = """
                sum: function integer(a : integer, b: integer){
                    return a + b;
                }
                main: function void(inherit out a : integer, b : float) inherit a{
                    a: integer = 1;
                    b : integer = 2;
                    print(a + b);
                }
            """
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(print, BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 37))
    
    def test38(self):
        input = """
                giaithua: function integer(n: integer){
                    if (n <= 0) return 1;
                    else return giaithua(n - 1) *n;
                }
                main: function void(inherit out a : integer, b : float) inherit a{
                    a: integer = giaithua(5);
                    b : integer = 2;
                }
            """
        expect = """Program([
	FuncDecl(giaithua, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, FuncCall(giaithua, [BinExpr(-, Id(n), IntegerLit(1))]), Id(n))))]))
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, FuncCall(giaithua, [IntegerLit(5)])), VarDecl(b, IntegerType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 38))
    
    def test39(self):
        input = """
                a : integer = 1;
                giaithua: function integer(n: integer){
                    if (n <= 0) return 1;
                    else return giaithua(n - 1) *n;
                }
                a : integer = 1;
                a : integer = 1;

                main: function void(inherit out a : integer, b : float) inherit a{
                    a: integer = giaithua(5);
                    b : integer = 2;
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(giaithua, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, FuncCall(giaithua, [BinExpr(-, Id(n), IntegerLit(1))]), Id(n))))]))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, FuncCall(giaithua, [IntegerLit(5)])), VarDecl(b, IntegerType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 39))
    
    def test40(self):
        input = """
                a : integer = 1;
                checkSoNguyenTo: function boolean(a: integer){
                    for (i = 2, i < sqrt(a), i + 1 ){
                        if (a % i == 0) return false;
                    }
                    return true;
                }
                main: function void(inherit out a : integer, b : float) inherit a{
                    a: integer = giaithua(5);
                    if(checkSoNguyenTo(a)) print("Day la so nguyen to!!!");
                    else print("Day khong phai la so nguyen to!!!");
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(checkSoNguyenTo, BooleanType, [Param(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, FuncCall(giaithua, [IntegerLit(5)])), IfStmt(FuncCall(checkSoNguyenTo, [Id(a)]), CallStmt(print, StringLit(Day la so nguyen to!!!)), CallStmt(print, StringLit(Day khong phai la so nguyen to!!!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 40))
    
    def test41(self):
        input = """
                a : integer = 1;
                checkSoNguyenTo: function boolean(a: integer){
                    for (i = 2, i < sqrt(a), i + 1 ){
                        if (a % i == 0) return false;
                    }
                    return true;
                }
                checkList : function array [10] of integer(a: array [5] of integer){
                    return a;
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(checkSoNguyenTo, BooleanType, [Param(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(checkList, ArrayType([10], IntegerType), [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 41))
    
    def test42(self):
        input = """
                a : integer = 1;
                checkSoNguyenTo: function boolean(a: integer){
                    for (i = 2, i < sqrt(a), i + 1 ){
                        if (a % i == 0) return false;
                    }
                    return true;
                }
                checkList : function array [10] of integer(a: array [5] of integer){
                    a = a + 1;
                    a = a / 1;
                    a = a* 1;
                    a = a -----1;
                    a = 1111;
                    a = f();
                    a  = a :: b;
                    if (!a){
                        return 1;
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(checkSoNguyenTo, BooleanType, [Param(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(checkList, ArrayType([10], IntegerType), [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(*, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(-, Id(a), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(1))))))), AssignStmt(Id(a), IntegerLit(1111)), AssignStmt(Id(a), FuncCall(f, [])), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b))), IfStmt(UnExpr(!, Id(a)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 42))
    def test43(self):
        input = """
                a : integer = 1;
                checkSoNguyenTo: function boolean(a: integer){
                    for (i = 2, i < sqrt(a), i + 1 ){
                        if (a % i == 0) return false;
                    }
                    return true;
                }
                checkList : function array [10,5,4,34,2] of integer(a: array [5] of integer){
                    a = a + 1;
                    a = a / 1;
                    a = a* 1;
                    a = a -----1;
                    a = 1111;
                    a = f();
                    a  = a :: b;
                    if (!a){
                        return 1;
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(checkSoNguyenTo, BooleanType, [Param(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(checkList, ArrayType([10, 5, 4, 34, 2], IntegerType), [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(*, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(-, Id(a), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(1))))))), AssignStmt(Id(a), IntegerLit(1111)), AssignStmt(Id(a), FuncCall(f, [])), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b))), IfStmt(UnExpr(!, Id(a)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 43))
    
    def test44(self):
        input = """
                a : integer = 1;
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || (a != c)){
                        
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(!=, Id(a), Id(c))), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 44))
    
    def test45(self):
        input = """
                a : integer = 1;
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 45))
        
    def test46(self):
        input = """
                a,b,c : integer = 1,2,3;
                a,b,c : auto = 1,2,3;
                a,b,c : array [10] of integer = {1,2,3,4,5,56}, {5,4,3,56}, {224234,234234,234234,23424};
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(c, AutoType, IntegerLit(3))
	VarDecl(a, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(56)]))
	VarDecl(b, ArrayType([10], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(4), IntegerLit(3), IntegerLit(56)]))
	VarDecl(c, ArrayType([10], IntegerType), ArrayLit([IntegerLit(224234), IntegerLit(234234), IntegerLit(234234), IntegerLit(23424)]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 46))
    
    def test47(self):
        input = """
                a,b,c : integer = 1,2,3;
                a,b,c : auto = 1,2,3;
                a,b,c : array [10] of integer = {1,2,3,4,5,56}, {5,4,3,56}, {224234,234234,234234,23424};
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
                main : function void(a: array [5] of integer){
                    if (a){
                        
                    }
                    else if ((a == b) || ((a != c) && !a)){
                        
                    }
                    
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(c, AutoType, IntegerLit(3))
	VarDecl(a, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(56)]))
	VarDecl(b, ArrayType([10], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(4), IntegerLit(3), IntegerLit(56)]))
	VarDecl(c, ArrayType([10], IntegerType), ArrayLit([IntegerLit(224234), IntegerLit(234234), IntegerLit(234234), IntegerLit(23424)]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(&&, BinExpr(!=, Id(a), Id(c)), UnExpr(!, Id(a)))), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 47))
    def test48(self):
        input = """
            main: function void(inherit out a : integer, b : float) inherit a{
                    while (true){
                        
                    }
                    while (true){
                        a = 1;
                        a : integer = 1;
                        a = c*c + b;
                    }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([])), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, BinExpr(*, Id(c), Id(c)), Id(b)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 48))
    def test49(self):
        input = """
            main: function void(inherit out a : integer, b : float) inherit a{
                    a : integer = 1;
                    f : integer = 1;
                    b : integer = 5;
                    while(a <= b){
                        f = a;
                        a = a + 1;
                    }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(f, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(<=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(f), Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 49))
    def test50(self):
        input = """
            sum: function integer(x:integer, y:integer,z:integer){
                return x + y + z;
            } 
            main : function void() {    
                printInteger(sum(1,2,3));
            }
            """
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(x, IntegerType), Param(y, IntegerType), Param(z, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(sum, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 50))
    def test51(self):
        input = """
            test : function integer(x:integer,y:integer,z:integer) {    
                if (x + y + z >= 2) {
                    return x+y+z;
                }
                else {
                    return 0;
                }
            }
            main : function void() {    
                a: integer = test(1,2,3);
                printInteger(a);
            }
            """
        expect = """Program([
	FuncDecl(test, IntegerType, [Param(x, IntegerType), Param(y, IntegerType), Param(z, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)), IntegerLit(2)), BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(test, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 51))
    def test52(self):
        input = """
            getString: function string(x: string) {
                return x;
            }
            upperCase: function string(y: string) {
                    return y;
                }
            main : function void() {    
                a:string = getString("QA")::upperCase("cute");
            }
            """
        expect = """Program([
	FuncDecl(getString, StringType, [Param(x, StringType)], None, BlockStmt([ReturnStmt(Id(x))]))
	FuncDecl(upperCase, StringType, [Param(y, StringType)], None, BlockStmt([ReturnStmt(Id(y))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, BinExpr(::, FuncCall(getString, [StringLit(QA)]), FuncCall(upperCase, [StringLit(cute)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 52))
    def test53(self):
        input = """
            foo: function integer(x:integer,y:integer) {
                if(x + 2 == 3){
                    break;
                }
                else{
                    x = x*2;
                    y = y*2;
                }
                return x + y;
            }
            main : function void() {    
                printInteger(foo(2,3));
            }
            """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(3)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(x), BinExpr(*, Id(x), IntegerLit(2))), AssignStmt(Id(y), BinExpr(*, Id(y), IntegerLit(2)))])), ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(foo, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 53))
    def test54(self):
        input = """
            main : function void(args: string) {}
            foo: function boolean(a:string, b: string){
                return a == b;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(args, StringType)], None, BlockStmt([]))
	FuncDecl(foo, BooleanType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 54))
    def test55(self):
        input = """
            main : function void() {    
                x = !y - z[86,1_2_3] + t[1,2] * m[0,a+b+c];
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, UnExpr(!, Id(y)), ArrayCell(z, [IntegerLit(86), IntegerLit(123)])), BinExpr(*, ArrayCell(t, [IntegerLit(1), IntegerLit(2)]), ArrayCell(m, [IntegerLit(0), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 55))
    def test56(self):
        input = """
            a,b,c : float;
            main : function void() {    
                x = y && z && t || c || r;
            }
            """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(y), Id(z)), Id(t)), Id(c)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 56))
    def test57(self):
        input = """
            test : function integer (num:integer)  {
                if( num == 1){
                    return 1;
                }
                else {
                    return 0;
                }
            }
            main : function void() {
                printInteger(test(5));
            }
            """
        expect = """Program([
	FuncDecl(test, IntegerType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(num), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(test, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 57))
    def test58(self):
        input = """
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    if(i%2==0){printInteger(i);}
                    else foo(2*i);
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i))]), CallStmt(foo, BinExpr(*, IntegerLit(2), Id(i))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 58))
    def test59(self):
        input = """
            x: integer = 65;
                fact: function integer (n:integer){
                    if (n == 0) return 1;
                    else return n * fact(n-1);
                }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 59))
    def test60(self):
        input = """
            x: integer = 65;
                fact: function integer (n:integer){
                    if (n == 0) return 1;
                    else return n * fact(n-1);
                }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 60))
    def test61(self):
        input = """
            a: integer;
            main: function void(){
            }
            b:float;
            """
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 61))
    def test62(self):
        input = """
            main: function void(){
                for(i[0] = 1, i < 5, i + 1){
                    
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 62))
    def test63(self):
        input = """
            main: function void(inherit out a : integer, b : float) inherit a{
                    if(true) a = 1; 
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 63))
    def test64(self):
        input = """
             main: function void() {arr[2,2] = true;}
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(2), IntegerLit(2)]), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 64))
    def test65(self):
        input = """
            main: function void() {
                        if (a == true && b) {}
                        return 0;
                    }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(&&, BooleanLit(True), Id(b))), BlockStmt([])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 65))
    def test66(self):
        input = """
            main: function void() {
                        if (a == true && b) {return 0;}
                        else return 1;
                    }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(&&, BooleanLit(True), Id(b))), BlockStmt([ReturnStmt(IntegerLit(0))]), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 66))
    def test67(self):
        input = """
            main: function void (){
                        for(i = 1, i < 4, i + 1) {
                            while(str1::str2 != true * 3) {}
                        }
                    }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(::, Id(str1), BinExpr(!=, Id(str2), BinExpr(*, BooleanLit(True), IntegerLit(3)))), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 67))
    def test68(self):
        input = """
            x : array [2,2] of float ;
                    y : auto = "Hello World!";
            """
        expect = """Program([
	VarDecl(x, ArrayType([2, 2], FloatType))
	VarDecl(y, AutoType, StringLit(Hello World!))
])"""
        self.assertTrue(TestAST.test(input, expect, 68))
    def test69(self):
        input = """
            a, b : integer = "" :: 2, true && false;
            """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(::, StringLit(), IntegerLit(2)))
	VarDecl(b, IntegerType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 69))
    def test70(self):
        input = """
            a, b, x : integer = "" :: 2, true && .e2, k;
            """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(::, StringLit(), IntegerLit(2)))
	VarDecl(b, IntegerType, BinExpr(&&, BooleanLit(True), FloatLit(0.0)))
	VarDecl(x, IntegerType, Id(k))
])"""
        self.assertTrue(TestAST.test(input, expect, 70))
    def test71(self):
        input = """
            a: integer = 1;
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 71))
    def test72(self):
        input = """
            a,b,c: integer = 1,2,3;
            
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 72))
    def test73(self):
        input = """
            main:function void(){
                print;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(print), )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 73))
    def test74(self):
        input = """
            main:function void(){
                if(a) a= 1;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), AssignStmt(Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 74))
    def test75(self):
        input = """
            main:function void(){
                //if(a) a = 1;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 75))
    def test76(self):
        input = """
            main:function void(){
                //if(a) a = 1;
                /* 124*/
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 76))
    def test77(self):
        input = """
            main:function void(){
                a = 1;
                a = true;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 77))
    def test78(self):
        input = """
            main:function void(){
                if (a){
                    if(c){
                        
                    }
                }
                else if(b){
                    if(d){
                        
                    }
                }
                else{
                    {
                        
                    }
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), BlockStmt([IfStmt(Id(c), BlockStmt([]))]), IfStmt(Id(b), BlockStmt([IfStmt(Id(d), BlockStmt([]))]), BlockStmt([BlockStmt([])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 78))
    def test79(self):
        input = """
            main:function void(){
                if (a){
                    if(c){
                        for(i = 2, i < 5, i /2){
                            
                        }
                    }
                }
                else if(b){
                    if(d){
                        
                    }
                }
                else{
                    {
                        
                    }
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), BlockStmt([IfStmt(Id(c), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([]))]))]), IfStmt(Id(b), BlockStmt([IfStmt(Id(d), BlockStmt([]))]), BlockStmt([BlockStmt([])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 79))
    def test80(self):
        input = """
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
])"""
        self.assertTrue(TestAST.test(input, expect, 80))
    def test81(self):
        input = """
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
])"""
        self.assertTrue(TestAST.test(input, expect, 81))
    def test82(self):
        input = """
            a,b,c,d : integer = {1,2,3,4},true, "23133", 0.5;
            main : function void(){
                a1;
            }
            """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, IntegerType, BooleanLit(True))
	VarDecl(c, IntegerType, StringLit(23133))
	VarDecl(d, IntegerType, FloatLit(0.5))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a1), )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 82))
    def test83(self):
        input = """
            main:function void(){\ndo {{i = 1; \n i = 2;}}while(a == 2);}
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(i), IntegerLit(2))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 83))
    def test84(self):
        input = """
             a, b : array [5] of integer= {1,2,3} , 3;
            """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([5], IntegerType), IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 84))
    def test85(self):
        input = """
                a, b : array [5] of integer/*= {1,2,3} , 3*/;

            """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType))
	VarDecl(b, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 85))
    def test86(self):
        input = """
            gram : function integer(out a : integer) inherit func{}
            """
        expect = """Program([
	FuncDecl(gram, IntegerType, [OutParam(a, IntegerType)], func, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 86))
    def test87(self):
        input = """
            main : function void () {
                false1 : integer = arr[1,2];
                a = a[2];
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(false1, IntegerType, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])), AssignStmt(Id(a), ArrayCell(a, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 87))
    def test88(self):
        input = """
            main : function void () {
                    a = {{1,2,3}};
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 88))
    def test89(self):
        input = """
            main : function void () {
                    a = {{1,2,3}, {}};
                } 
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 89))
    def test90(self):
        input = """
            func1 : function integer(a : array [5] of integer){
                    return 1;
                }
            """
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 90))
    def test91(self):
        input = """
            a : integer = {1,2,3};
            """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 91))
    def test92(self):
        input = """
            main: function void(inherit out a : integer, b : float) inherit a{
                    while (true){
                        
                    }
                    if(true){a:integer = 1;} a:integer = 1;
                    while (true){
                        a = 1;
                        a : integer = 1;
                        a = c*c + b;
                    }
                }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))])), VarDecl(a, IntegerType, IntegerLit(1)), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, BinExpr(*, Id(c), Id(c)), Id(b)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 92))
    def test93(self):
        input = """
            foo: function integer(x:integer,y:integer) {
                if(x + 2 == 3){
                    break;
                }
                else{
                    x = x*2;
                    y = y*2;
                }
                return x + y;
            }
            main : function void() {    
                printInteger(foo(2,3));
            }
            """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(3)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(x), BinExpr(*, Id(x), IntegerLit(2))), AssignStmt(Id(y), BinExpr(*, Id(y), IntegerLit(2)))])), ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(foo, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 93))
    def test94(self):
        input = """
            main : function void(args: string) {}
            foo: function boolean(a:string, b: string){
                return a == b;
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(args, StringType)], None, BlockStmt([]))
	FuncDecl(foo, BooleanType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 94))
    def test95(self):
        input = """
            main : function void() {    
                x = !y - z[86,1_2_3] + t[1,2] * m[0,a+b+c];
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, UnExpr(!, Id(y)), ArrayCell(z, [IntegerLit(86), IntegerLit(123)])), BinExpr(*, ArrayCell(t, [IntegerLit(1), IntegerLit(2)]), ArrayCell(m, [IntegerLit(0), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 95))
    def test96(self):
        input = """
            a,b,c : float;
            main : function void() {    
                x = y && z && t || c || r;
            }
            """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(y), Id(z)), Id(t)), Id(c)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 96))
    def test97(self):
        input = """
            test : function integer (num:integer)  {
                if( num == 1){
                    return 1;
                }
                else {
                    return 0;
                }
            }
            main : function void() {
                printInteger(test(5));
            }
            """
        expect = """Program([
	FuncDecl(test, IntegerType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(num), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(test, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 97))
    def test98(self):
        input = """
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    if(i%2==0){printInteger(i);}
                    else foo(2*i);
                }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i))]), CallStmt(foo, BinExpr(*, IntegerLit(2), Id(i))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 98))
    def test99(self):
        input = """
            x: integer = 65;
                fact: function integer (n:integer){
                    if (n == 0) return 1;
                    else return n * fact(n-1);
                }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 99))
    def test100(self):
        input = """
            x: integer = 65;
                fact: function integer (n:integer){
                    if (n == 0) return 1;
                    else return n * fact(n-1);
                }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
            """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 100))