Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite

Nếu param trong func 
suy diễn kiểu cho biến 

Khi gọi super không có cùng tham số với hàm cha: typemissmatchinexpression


func1: function void (inherit a: integer){}

func2 : function void () inherit func1{
    super(1);
}
func3 : function void () inherit func2{
    super();
    a = 1;
}

import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test1(self):
        input = """
        i:auto = 0;
        a: array [5] of integer;
        main: function void(){
            main:integer = 1;
        }
        sum : function auto(c: auto) inherit sum1{
           supper(1,2,3);
            
        }
        sum1 : function integer(inherit a:integer, inherit b:integer){
           
            
        }
        """
        expect = """Invalid statement in function: sum"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test2(self):
        input = """
        i:auto = 0;
        a: array [5] of integer;
        main: function void(){
            main:integer = 1;
        }
        a: function void() {
            //a:integer
        } 
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test3(self):
        input = """
        a: array [5] of integer;
        main: function void(){
        }
        x: function auto(){
            
        } 

        foo:function void() {
            //x: integer = x();
            a1: auto = x() + x();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test4(self):
        input = """
        a: array [5] of integer;
        main: function void(){
            main:integer = 1;
        }
        foo: function void (inherit a: integer, a: float) inherit bar {
            
        }
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test5(self):
        input = """
        main: function void(){
            main:integer = 1;
            bar(1);
        }
        bar: function void (inherit c: integer){

        }
        foo: function void (a: integer) inherit bar {
            preventDefault();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test6(self):
        input = """
        main: function void(){
        }
        foo: function void (a: auto, c: auto){
            a: float = 1;
            foo(1.2, 1.2);
            foo(1.2, 1);
        }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test7(self):
        input = """
        main: function void() inherit foo{
            //Case 1:
            {
                supper(2,3); 
            }
            
            //Case 2:
            //a = 1;
            //supper(a, 1);
            
            //Case 3:
            //a = supper(1,2);
            
            //Case 4:
            //supper(1, 2);
            //supper("1", 3);
        }
        
        foo: function integer (inherit a: auto, inherit b: auto){
            
        }
        """
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test8(self):
        input = """
        main: function void(a: integer) inherit func{
            
        }
        func :function auto (inherit a: auto, inherit b :auto){
            
        }
        
        
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test9(self):
        input = """
        main: function void(c: integer) inherit func{
            super(1,2);
            super(1,2);
        }
        func :function auto (inherit a: auto, inherit b :auto){
            
        }
        """
        expect = """Invalid statement in function: CallStmt(super, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test10(self):
        input = """
        main: function void(c: integer) inherit func{
            preventDefault();
            func(1,2);
            d:integer = func(1,2);
        }
        func :function auto (inherit a: auto, inherit b :auto){
            
        
        }
        func1 :function auto (inherit a: auto, inherit b :auto){
            func("1",2);
        }
        
        """
        expect = """Type mismatch in expression: StringLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test11(self):
        input = """
        main: function void() {

        }
        func :function float (){
            if (true){
                return 1;
            }
            else if (false){
                return 3;
            }
            return "12";
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit(12))"""
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test12(self):
        input = """
        main: function void() {
        }
        arr : auto = {{{1,2,3.0},{1,2,3}},{{1,2,3},{1,2,3}},{{1,2,3},{1,2,3}}};
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test13(self):
        input = """
        inc : function void (out n : integer, a:float) inherit foo{
            } //1
        foo : function auto (inherit n: float, n: integer){
            } //2
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test13(self):
        input = """
        inc : function void (out b : integer, n:float) inherit foo{
            
            }
        fooo2 : function void (out b : integer, b:float){
            
            }
        foo : function auto (inherit n: float, c: integer){
            }
        """
        expect = """Invalid Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test14(self):
        input = """
        inc : function void (){
                i:integer = a[1];
            }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test15(self):
        input = """
        inc : function void () inherit foo{
                
        }
        foo: function integer(inherit a :integer){
            
        }
        """
        expect = """Invalid statement in function: inc"""
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test16(self):
        input = """
        a: integer = 1;
        inc : function void (){
            a();
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test16(self):
        input = """
        inc : function void (){
            if (1 < 1.5){
                
            }
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 416))    
    def test17(self):
        input = """
        inc : function void (){
            a: array [2,3] of integer;
            a[1,2,3];
        }
        """
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test18(self):
        input = """
        inc : function void (){
             a: array[2] of integer = {{1}, {2}};
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test19(self):
        input = """
        inc : function void (){
             a: array[2,2] of integer = {{1, 2}, {1, 1.5}}
        }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), FloatLit(1.5)])])"""
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test20(self):
        input = """
        inc : function void () inherit foo{
            preventDefault(1);
        }
        foo: function void(){
            
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test21(self):
        input = """
        inc : function void (){
            foo(1);
        }
        foo: function void(){
            
        }
        """
        expect = """Type mismatch in expression: CallStmt(foo, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test22(self):
        input = """
        inc : function void () inherit foo{
            super(1);
        }
        foo: function void(a:integer){
            
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test23(self):
        input = """
        inc : function void () inherit foo{
            super();
        }
        foo: function void(a:integer){
            
        }
        """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test24(self):
        input = """
        inc : function void () inherit foo{
            super(1,2);
        }
        foo: function void(a:integer){
            
        }
        """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test25(self):
        input = """
        inc : function void () inherit foo{
            super(1,2,3);
        }
        foo: function void(a:integer){
            
        }
        """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test26(self):
        input = """
        inc : function void () inherit foo{
        }
        foo: function void(){
            
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test27(self):
        input = """
        inc : function void () inherit foo{
            preventDefault(1);
        }
        foo: function void(){
            
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test28(self):
        input = """
        inc : function void () inherit foo{
            preventDefault(1,2,3);
        }
        foo: function void(){
            
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 428))