# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01e7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\3/\7/\u012f\n/\f/\16/\u0132\13/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u013a\n\60\f\60\16\60\u013d\13\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u014d\n\61\3\62\3\62\7\62\u0151\n\62\f")
        buf.write("\62\16\62\u0154\13\62\3\63\3\63\3\63\7\63\u0159\n\63\f")
        buf.write("\63\16\63\u015c\13\63\3\63\3\63\6\63\u0160\n\63\r\63\16")
        buf.write("\63\u0161\7\63\u0164\n\63\f\63\16\63\u0167\13\63\3\63")
        buf.write("\5\63\u016a\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\5\64\u0179\n\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\7\65\u0180\n\65\f\65\16\65\u0183\13\65")
        buf.write("\3\65\3\65\6\65\u0187\n\65\r\65\16\65\u0188\7\65\u018b")
        buf.write("\n\65\f\65\16\65\u018e\13\65\5\65\u0190\n\65\3\66\3\66")
        buf.write("\7\66\u0194\n\66\f\66\16\66\u0197\13\66\3\67\3\67\5\67")
        buf.write("\u019b\n\67\3\67\3\67\3\67\7\67\u01a0\n\67\f\67\16\67")
        buf.write("\u01a3\13\67\5\67\u01a5\n\67\38\38\38\38\38\78\u01ac\n")
        buf.write("8\f8\168\u01af\138\38\38\38\58\u01b4\n8\39\39\39\3:\3")
        buf.write(":\7:\u01bb\n:\f:\16:\u01be\13:\3:\3:\3:\3;\6;\u01c4\n")
        buf.write(";\r;\16;\u01c5\3;\3;\3<\3<\3<\3=\3=\7=\u01cf\n=\f=\16")
        buf.write("=\u01d2\13=\3=\5=\u01d5\n=\3=\3=\3>\3>\3>\5>\u01dc\n>")
        buf.write("\3?\3?\7?\u01e0\n?\f?\16?\u01e3\13?\3?\3?\3?\3\u013b\2")
        buf.write("@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s")
        buf.write("\66u\67w8y9{\2}:\3\2\r\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f$$))^")
        buf.write("^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\3\3\f\f\2\u01fb")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2}")
        buf.write("\3\2\2\2\3\177\3\2\2\2\5\u0084\3\2\2\2\7\u008c\3\2\2\2")
        buf.write("\t\u0093\3\2\2\2\13\u009b\3\2\2\2\r\u00a1\3\2\2\2\17\u00a7")
        buf.write("\3\2\2\2\21\u00ad\3\2\2\2\23\u00b0\3\2\2\2\25\u00b5\3")
        buf.write("\2\2\2\27\u00b9\3\2\2\2\31\u00c2\3\2\2\2\33\u00c5\3\2")
        buf.write("\2\2\35\u00cc\3\2\2\2\37\u00d2\3\2\2\2!\u00d7\3\2\2\2")
        buf.write("#\u00db\3\2\2\2%\u00e4\3\2\2\2\'\u00e7\3\2\2\2)\u00ef")
        buf.write("\3\2\2\2+\u00f1\3\2\2\2-\u00f3\3\2\2\2/\u00f5\3\2\2\2")
        buf.write("\61\u00f7\3\2\2\2\63\u00f9\3\2\2\2\65\u00fb\3\2\2\2\67")
        buf.write("\u00fe\3\2\2\29\u0101\3\2\2\2;\u0104\3\2\2\2=\u0107\3")
        buf.write("\2\2\2?\u0109\3\2\2\2A\u010b\3\2\2\2C\u010e\3\2\2\2E\u0111")
        buf.write("\3\2\2\2G\u0114\3\2\2\2I\u0116\3\2\2\2K\u0118\3\2\2\2")
        buf.write("M\u011a\3\2\2\2O\u011c\3\2\2\2Q\u011e\3\2\2\2S\u0120\3")
        buf.write("\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2Y\u0126\3\2\2\2[\u0128")
        buf.write("\3\2\2\2]\u012a\3\2\2\2_\u0135\3\2\2\2a\u014c\3\2\2\2")
        buf.write("c\u014e\3\2\2\2e\u0169\3\2\2\2g\u0178\3\2\2\2i\u018f\3")
        buf.write("\2\2\2k\u0191\3\2\2\2m\u0198\3\2\2\2o\u01b3\3\2\2\2q\u01b5")
        buf.write("\3\2\2\2s\u01b8\3\2\2\2u\u01c3\3\2\2\2w\u01c9\3\2\2\2")
        buf.write("y\u01cc\3\2\2\2{\u01db\3\2\2\2}\u01dd\3\2\2\2\177\u0080")
        buf.write("\7c\2\2\u0080\u0081\7w\2\2\u0081\u0082\7v\2\2\u0082\u0083")
        buf.write("\7q\2\2\u0083\4\3\2\2\2\u0084\u0085\7k\2\2\u0085\u0086")
        buf.write("\7p\2\2\u0086\u0087\7v\2\2\u0087\u0088\7g\2\2\u0088\u0089")
        buf.write("\7i\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b\6")
        buf.write("\3\2\2\2\u008c\u008d\7u\2\2\u008d\u008e\7v\2\2\u008e\u008f")
        buf.write("\7t\2\2\u008f\u0090\7k\2\2\u0090\u0091\7p\2\2\u0091\u0092")
        buf.write("\7i\2\2\u0092\b\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095")
        buf.write("\7q\2\2\u0095\u0096\7q\2\2\u0096\u0097\7n\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7c\2\2\u0099\u009a\7p\2\2\u009a\n")
        buf.write("\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d\7n\2\2\u009d\u009e")
        buf.write("\7q\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7v\2\2\u00a0\f")
        buf.write("\3\2\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7{\2\2\u00a6\16")
        buf.write("\3\2\2\2\u00a7\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\20")
        buf.write("\3\2\2\2\u00ad\u00ae\7f\2\2\u00ae\u00af\7q\2\2\u00af\22")
        buf.write("\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\24\3\2\2\2\u00b5\u00b6")
        buf.write("\7h\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7t\2\2\u00b8\26")
        buf.write("\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\30")
        buf.write("\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7h\2\2\u00c4\32")
        buf.write("\3\2\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\34\3\2\2\2\u00cc\u00cd\7y\2\2\u00cd\u00ce")
        buf.write("\7j\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\36\3\2\2\2\u00d2\u00d3\7x\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7f\2\2\u00d6 \3")
        buf.write("\2\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\"\3\2\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7h\2\2\u00e6&\3\2\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7v\2\2\u00ee(\3")
        buf.write("\2\2\2\u00ef\u00f0\7-\2\2\u00f0*\3\2\2\2\u00f1\u00f2\7")
        buf.write("/\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7,\2\2\u00f4.\3\2\2\2")
        buf.write("\u00f5\u00f6\7\61\2\2\u00f6\60\3\2\2\2\u00f7\u00f8\7\'")
        buf.write("\2\2\u00f8\62\3\2\2\2\u00f9\u00fa\7#\2\2\u00fa\64\3\2")
        buf.write("\2\2\u00fb\u00fc\7(\2\2\u00fc\u00fd\7(\2\2\u00fd\66\3")
        buf.write("\2\2\2\u00fe\u00ff\7~\2\2\u00ff\u0100\7~\2\2\u01008\3")
        buf.write("\2\2\2\u0101\u0102\7?\2\2\u0102\u0103\7?\2\2\u0103:\3")
        buf.write("\2\2\2\u0104\u0105\7#\2\2\u0105\u0106\7?\2\2\u0106<\3")
        buf.write("\2\2\2\u0107\u0108\7>\2\2\u0108>\3\2\2\2\u0109\u010a\7")
        buf.write("@\2\2\u010a@\3\2\2\2\u010b\u010c\7>\2\2\u010c\u010d\7")
        buf.write("?\2\2\u010dB\3\2\2\2\u010e\u010f\7@\2\2\u010f\u0110\7")
        buf.write("?\2\2\u0110D\3\2\2\2\u0111\u0112\7<\2\2\u0112\u0113\7")
        buf.write("<\2\2\u0113F\3\2\2\2\u0114\u0115\7*\2\2\u0115H\3\2\2\2")
        buf.write("\u0116\u0117\7+\2\2\u0117J\3\2\2\2\u0118\u0119\7]\2\2")
        buf.write("\u0119L\3\2\2\2\u011a\u011b\7_\2\2\u011bN\3\2\2\2\u011c")
        buf.write("\u011d\7\60\2\2\u011dP\3\2\2\2\u011e\u011f\7.\2\2\u011f")
        buf.write("R\3\2\2\2\u0120\u0121\7=\2\2\u0121T\3\2\2\2\u0122\u0123")
        buf.write("\7<\2\2\u0123V\3\2\2\2\u0124\u0125\7}\2\2\u0125X\3\2\2")
        buf.write("\2\u0126\u0127\7\177\2\2\u0127Z\3\2\2\2\u0128\u0129\7")
        buf.write("?\2\2\u0129\\\3\2\2\2\u012a\u012b\7\61\2\2\u012b\u012c")
        buf.write("\7\61\2\2\u012c\u0130\3\2\2\2\u012d\u012f\n\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0133\u0134\b/\2\2\u0134^\3\2\2\2\u0135\u0136\7")
        buf.write("\61\2\2\u0136\u0137\7,\2\2\u0137\u013b\3\2\2\2\u0138\u013a")
        buf.write("\13\2\2\2\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013e\u013f\7,\2\2\u013f\u0140\7")
        buf.write("\61\2\2\u0140\u0141\3\2\2\2\u0141\u0142\b\60\2\2\u0142")
        buf.write("`\3\2\2\2\u0143\u0144\7v\2\2\u0144\u0145\7t\2\2\u0145")
        buf.write("\u0146\7w\2\2\u0146\u014d\7g\2\2\u0147\u0148\7h\2\2\u0148")
        buf.write("\u0149\7c\2\2\u0149\u014a\7n\2\2\u014a\u014b\7u\2\2\u014b")
        buf.write("\u014d\7g\2\2\u014c\u0143\3\2\2\2\u014c\u0147\3\2\2\2")
        buf.write("\u014db\3\2\2\2\u014e\u0152\t\3\2\2\u014f\u0151\t\4\2")
        buf.write("\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153d\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0155\u016a\7\62\2\2\u0156\u015a\t\5\2\2\u0157")
        buf.write("\u0159\t\6\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0165\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015d\u015f\7a\2\2\u015e\u0160")
        buf.write("\t\6\2\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2")
        buf.write("\u0163\u015d\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0168\u016a\b\63\3\2\u0169\u0155\3\2\2\2\u0169")
        buf.write("\u0156\3\2\2\2\u016af\3\2\2\2\u016b\u016c\5i\65\2\u016c")
        buf.write("\u016d\5k\66\2\u016d\u0179\3\2\2\2\u016e\u016f\5i\65\2")
        buf.write("\u016f\u0170\5m\67\2\u0170\u0179\3\2\2\2\u0171\u0172\5")
        buf.write("k\66\2\u0172\u0173\5m\67\2\u0173\u0179\3\2\2\2\u0174\u0175")
        buf.write("\5i\65\2\u0175\u0176\5k\66\2\u0176\u0177\5m\67\2\u0177")
        buf.write("\u0179\3\2\2\2\u0178\u016b\3\2\2\2\u0178\u016e\3\2\2\2")
        buf.write("\u0178\u0171\3\2\2\2\u0178\u0174\3\2\2\2\u0179\u017a\3")
        buf.write("\2\2\2\u017a\u017b\b\64\4\2\u017bh\3\2\2\2\u017c\u0190")
        buf.write("\7\62\2\2\u017d\u0181\t\5\2\2\u017e\u0180\t\6\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u018c\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0184\u0186\7a\2\2\u0185\u0187\t\6\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u0184\3\2\2\2")
        buf.write("\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u017c")
        buf.write("\3\2\2\2\u018f\u017d\3\2\2\2\u0190j\3\2\2\2\u0191\u0195")
        buf.write("\7\60\2\2\u0192\u0194\t\6\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196l\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019a\t\7\2")
        buf.write("\2\u0199\u019b\t\b\2\2\u019a\u0199\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u01a4\3\2\2\2\u019c\u01a5\7\62\2\2\u019d")
        buf.write("\u01a1\t\5\2\2\u019e\u01a0\t\6\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u019c")
        buf.write("\3\2\2\2\u01a4\u019d\3\2\2\2\u01a5n\3\2\2\2\u01a6\u01b4")
        buf.write("\n\t\2\2\u01a7\u01a8\7^\2\2\u01a8\u01a9\7$\2\2\u01a9\u01ad")
        buf.write("\3\2\2\2\u01aa\u01ac\5o8\2\u01ab\u01aa\3\2\2\2\u01ac\u01af")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01b0\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\7^\2\2")
        buf.write("\u01b1\u01b4\7$\2\2\u01b2\u01b4\5q9\2\u01b3\u01a6\3\2")
        buf.write("\2\2\u01b3\u01a7\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4p\3")
        buf.write("\2\2\2\u01b5\u01b6\7^\2\2\u01b6\u01b7\t\n\2\2\u01b7r\3")
        buf.write("\2\2\2\u01b8\u01bc\7$\2\2\u01b9\u01bb\5o8\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01bf\u01c0\7$\2\2\u01c0\u01c1\b:\5\2\u01c1t\3\2\2\2")
        buf.write("\u01c2\u01c4\t\13\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\b;\2\2\u01c8v\3\2\2\2\u01c9")
        buf.write("\u01ca\13\2\2\2\u01ca\u01cb\b<\6\2\u01cbx\3\2\2\2\u01cc")
        buf.write("\u01d0\7$\2\2\u01cd\u01cf\5o8\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5\t")
        buf.write("\f\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\b=\7\2\u01d7z\3\2\2\2\u01d8\u01d9\7^\2\2\u01d9\u01dc")
        buf.write("\n\n\2\2\u01da\u01dc\7^\2\2\u01db\u01d8\3\2\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc|\3\2\2\2\u01dd\u01e1\7$\2\2\u01de")
        buf.write("\u01e0\5o8\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e5\5{>\2\u01e5\u01e6\b?")
        buf.write("\b\2\u01e6~\3\2\2\2\34\2\u0130\u013b\u014c\u0152\u015a")
        buf.write("\u0161\u0165\u0169\u0178\u0181\u0188\u018c\u018f\u0195")
        buf.write("\u019a\u01a1\u01a4\u01ad\u01b3\u01bc\u01c5\u01d0\u01d4")
        buf.write("\u01db\u01e1\t\b\2\2\3\63\2\3\64\3\3:\4\3<\5\3=\6\3?\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    INT = 2
    STRING = 3
    BOOL = 4
    FLOAT = 5
    ARR = 6
    BREAK = 7
    DO = 8
    ELSE = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    RETURN = 13
    WHILE = 14
    VOID = 15
    OUT = 16
    CONTINUE = 17
    OF = 18
    INHERIT = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQUAL = 28
    DIF = 29
    LESS = 30
    BIGGER = 31
    LESSEQUAL = 32
    MOREEQUAL = 33
    CONCAT = 34
    LRB = 35
    RRB = 36
    LSB = 37
    RSB = 38
    POINT = 39
    CM = 40
    SM = 41
    CL = 42
    LPB = 43
    RPB = 44
    EQB = 45
    COMMENT = 46
    COMMENTS = 47
    BOOLEAN = 48
    IDENTIFIER = 49
    INTEGER = 50
    FLOATLITERAL = 51
    STRINGLITERAL = 52
    WS = 53
    ERROR_TOKEN = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'string'", "'boolean'", "'float'", "'array'", 
            "'break'", "'do'", "'else'", "'for'", "'function'", "'if'", 
            "'return'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "INT", "STRING", "BOOL", "FLOAT", "ARR", "BREAK", "DO", 
            "ELSE", "FOR", "FUNCTION", "IF", "RETURN", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "DIF", "LESS", "BIGGER", 
            "LESSEQUAL", "MOREEQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", 
            "POINT", "CM", "SM", "CL", "LPB", "RPB", "EQB", "COMMENT", "COMMENTS", 
            "BOOLEAN", "IDENTIFIER", "INTEGER", "FLOATLITERAL", "STRINGLITERAL", 
            "WS", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "INT", "STRING", "BOOL", "FLOAT", "ARR", "BREAK", 
                  "DO", "ELSE", "FOR", "FUNCTION", "IF", "RETURN", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "DIF", 
                  "LESS", "BIGGER", "LESSEQUAL", "MOREEQUAL", "CONCAT", 
                  "LRB", "RRB", "LSB", "RSB", "POINT", "CM", "SM", "CL", 
                  "LPB", "RPB", "EQB", "COMMENT", "COMMENTS", "BOOLEAN", 
                  "IDENTIFIER", "INTEGER", "FLOATLITERAL", "INTPART", "THAPPHAN", 
                  "MU", "CHAR_STR", "ESC_CHAR", "STRINGLITERAL", "WS", "ERROR_TOKEN", 
                  "UNCLOSE_STRING", "ILL_CHAR", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTEGER_action 
            actions[50] = self.FLOATLITERAL_action 
            actions[56] = self.STRINGLITERAL_action 
            actions[58] = self.ERROR_TOKEN_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text.replace('_','')

     

    def FLOATLITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text.replace('_','')

     

    def STRINGLITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:-1]

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                y = str(self.text)
                if y[-1] == '\n':
                    raise UncloseString(y[1:-1])
                else:
                    raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     


