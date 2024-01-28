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
        expect = """Invalid statement in function: main"""
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
        expect = """Type mismatch in statement: CallStmt(func, StringLit(1), IntegerLit(2))"""
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
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(1))"""
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
    def test29(self):
        input = """ 
        x: integer;
        main: function void (b: integer, c: string) {
            x: float = 2.0;
            printInteger(2.0);
            z: auto = 2;
        }
        """
        expect = "Type mismatch in statement: CallStmt(printInteger, FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test30(self):
        input = """ 
        foo: function integer (a:auto,b:auto) inherit bar{
                super(1);
                c=1;
                a=1;
                b=1;
            }
            bar:function void (inherit c:auto){
            
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test31(self):
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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test32(self):
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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test33(self):
        input = """ 
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    if(i%2==0){printInteger(i);}
                    else foo(2*i);
                }
            }
        """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test34(self):
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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test35(self):
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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test36(self):
        input = """ 
            a,b,c : float;
            main : function void() {    
                x = y && z && t || c || r;
            }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test37(self):
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
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test38(self):
        input = """ 
            main :function void(a: integer, a:integer) inherit foo{
                
            }
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test39(self):
        input = """ 
            foo:auto = 1;
            main :function void(a: integer, b:integer) inherit foo{
                
            }
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test40(self):
        input = """ 
            foo: function integer(){
            }
            main :function void(a: integer, b:integer) inherit foo{
                foo : integer = 1;
                c : integer = foo();
            }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test41(self):
        input = """ 
            foo: function integer(){
            }
            main :function void(a: integer, b:integer) inherit foo{
                foo : integer = 1;
                c : integer = foo();
            }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test42(self):
        input = """ 
        main: function void(){
            x: integer = foo();
        }
        foo: function auto(){
            return 1;
            return true;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test43(self):
        input = """
        a: array [5] of integer = {1,2,3};
        main: function void(){
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test43(self):
        input = """ 
        a: array [5,2] of integer = {{1,2}, {1,2}};
        main: function void(){
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test44(self):
        input = """ 
        a: array [5,2] of integer = {{1,2}, {1,2}, {1,2}, {1,2}, {1,2}};
        main: function void(){
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test45(self):
        input = """ 
        a: array [5,2] of integer = {{1,2}, {1.1}, {1,2}, {1,2}, {1,2}};
        main: function void(){
        }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([FloatLit(1.1)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test46(self):
        input = """ 
        a: array [5,2] of integer = {{1,2}, {1.1, 2}, {1,2}, {1,2}, {1,2}};
        main: function void(){
        }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([FloatLit(1.1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"""
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test47(self):
        input = """ 
        a: array [5,3] of integer = {{1,2}, {1, 2}, {1,2}, {1,2}, {1,2}};
        main: function void(){
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test48(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in expression: FloatLit(1.0)"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test49(self):
        input = """ 
        fact: function auto (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            return foo(1,1.0,true);
        }
        foo: function integer (x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test50(self):
        input = """ 
        fact: function auto (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            return foo(1,1.0,"true");
        }
        foo: function integer (x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: FuncCall(foo, [IntegerLit(1), FloatLit(1.0), StringLit(true)])"""
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test51(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            return foo(1,1.0,"true");
        }
        foo: function integer (x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: FuncCall(foo, [IntegerLit(1), FloatLit(1.0), StringLit(true)])"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test52(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            x = 1 ;
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test53(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            y = 1 ;
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Undeclared Identifier: y"""
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test54(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            for(m = 0, m < 1.0, m +1){
                if (true) return 1;
                else reurn 2;
            }
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test55(self):
        input = """ 
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            for(m = 0, m < 1.0, m +1){
                if (true) return;
                else return;
            }
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test56(self):
        input = """ 
        fact: function integer (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            for(m = 0, m < 1.0, m +1){
                if (true) return 1;
                else return "1";
            }
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test57(self):
        input = """ 
        fact: function integer (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            for(m = 0, m < 1.0, m +1){
                if (true) return 1;
                else return 1;
                return "3";
            }
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test58(self):
        input = """ 
        fact: function integer (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            for(m = 0, m < 1.0, m +1){
                if (true) return 1;
                else return 1;
                do{
                    
                }
                while(1)
            }
        }
        foo: function integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """Type mismatch in statement: DoWhileStmt(IntegerLit(1), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test59(self):
        input = """ 
        fact: function integer (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            var : array [5] of integer = foo(1, 1, false);
        }
        foo: function array [5] of integer (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test60(self):
        input = """ 
        fact: function integer (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
            var : array [5] of integer = foo(1, 1, false);
        }
        foo: function auto (inherit x:auto, y: auto, z:auto) {}
        main: function void(){
            
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test61(self):
        input = """ 
        foo: function integer(x:integer, y:float){}
        main: function void(){
            foo(t);
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, Id(t))"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test62(self):
        input = """ 
        main:function void(a:integer, a:float) inherit foo{}
        foo : function void(inherit a:integer){}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test63(self):
        input = """ 
        foo:function auto(inherit a:auto,inherit b:auto){
        }
        foo1: function integer(c:auto)inherit foo{
            super(1,3);
            a = 1;
            return c;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test64(self):
        input = """
        a: integer = 1;
        inc : function void (){
            a();
        }
        """
        expect = """Type mismatch in expression: CallStmt(a, )"""
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test65(self):
        input = """
        foo : function integer(){
            if (true) {
                return 1;
                return "2";
            }
            else{
                return 1;
                return "2";
            }
            return 1;
            return "2";
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 465))