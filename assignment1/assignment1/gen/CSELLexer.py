# Generated from D:/HK202/PPL/Assignment_1/assignment1/assignment1/initial/src/main/csel/parser\CSEL.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u0192\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u0082\n\f\f\f\16\f\u0085\13\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00a8\n\r\3\16\3\16\5\16\u00ac\n\16\3\16\5\16\u00af")
        buf.write("\n\16\3\17\6\17\u00b2\n\17\r\17\16\17\u00b3\3\20\3\20")
        buf.write("\7\20\u00b8\n\20\f\20\16\20\u00bb\13\20\3\21\3\21\5\21")
        buf.write("\u00bf\n\21\3\21\6\21\u00c2\n\21\r\21\16\21\u00c3\3\22")
        buf.write("\3\22\5\22\u00c8\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\3\25\6\25\u00d7\n\25\r\25")
        buf.write("\16\25\u00d8\3\26\3\26\7\26\u00dd\n\26\f\26\16\26\u00e0")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00eb\n\27\3\30\3\30\3\30\3\30\5\30\u00f1\n\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\7-\u0152\n-\f-\16-\u0155\13-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\5.\u015f\n.\3/\3/\3\60\6\60\u0164\n\60\r\60")
        buf.write("\16\60\u0165\3\60\3\60\3\61\3\61\3\61\3\62\3\62\7\62\u016f")
        buf.write("\n\62\f\62\16\62\u0172\13\62\3\62\5\62\u0175\n\62\3\62")
        buf.write("\3\62\3\63\3\63\7\63\u017b\n\63\f\63\16\63\u017e\13\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u0184\n\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u018c\n\64\f\64\16\64\u018f\13\64\3")
        buf.write("\64\3\64\4\u0083\u018d\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2\37\2!\2#\20%")
        buf.write("\2\'\2)\21+\22-\23/\24\61\25\63\26\65\27\67\309\31;\32")
        buf.write("=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[\2]*_+a,c-")
        buf.write("e.g/\3\2\17\3\2\62;\4\2GGgg\4\2--//\6\2\62;C\\aac|\3\2")
        buf.write("c|\4\2>>@@\5\2\'\',,\61\61\7\2\f\f\17\17$$))^^\t\2))^")
        buf.write("^ddhhppttvv\n\2*+..\60\60<=]]__}}\177\177\5\2\13\f\17")
        buf.write("\17\"\"\4\3\n\f\16\17\3\2$$\2\u01a6\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2#\3\2\2\2\2)")
        buf.write("\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2")
        buf.write("\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5k\3\2\2\2\7m\3")
        buf.write("\2\2\2\to\3\2\2\2\13q\3\2\2\2\rs\3\2\2\2\17u\3\2\2\2\21")
        buf.write("w\3\2\2\2\23y\3\2\2\2\25{\3\2\2\2\27}\3\2\2\2\31\u00a7")
        buf.write("\3\2\2\2\33\u00a9\3\2\2\2\35\u00b1\3\2\2\2\37\u00b5\3")
        buf.write("\2\2\2!\u00bc\3\2\2\2#\u00c7\3\2\2\2%\u00c9\3\2\2\2\'")
        buf.write("\u00ce\3\2\2\2)\u00d4\3\2\2\2+\u00da\3\2\2\2-\u00ea\3")
        buf.write("\2\2\2/\u00f0\3\2\2\2\61\u00f2\3\2\2\2\63\u00f4\3\2\2")
        buf.write("\2\65\u00f6\3\2\2\2\67\u00f8\3\2\2\29\u00fa\3\2\2\2;\u00fd")
        buf.write("\3\2\2\2=\u0101\3\2\2\2?\u0107\3\2\2\2A\u0110\3\2\2\2")
        buf.write("C\u0113\3\2\2\2E\u0118\3\2\2\2G\u011d\3\2\2\2I\u0123\3")
        buf.write("\2\2\2K\u0127\3\2\2\2M\u012a\3\2\2\2O\u012d\3\2\2\2Q\u0132")
        buf.write("\3\2\2\2S\u0139\3\2\2\2U\u0142\3\2\2\2W\u0146\3\2\2\2")
        buf.write("Y\u014f\3\2\2\2[\u015e\3\2\2\2]\u0160\3\2\2\2_\u0163\3")
        buf.write("\2\2\2a\u0169\3\2\2\2c\u016c\3\2\2\2e\u0178\3\2\2\2g\u0187")
        buf.write("\3\2\2\2ij\7=\2\2j\4\3\2\2\2kl\7.\2\2l\6\3\2\2\2mn\7<")
        buf.write("\2\2n\b\3\2\2\2op\7?\2\2p\n\3\2\2\2qr\7]\2\2r\f\3\2\2")
        buf.write("\2st\7_\2\2t\16\3\2\2\2uv\7*\2\2v\20\3\2\2\2wx\7+\2\2")
        buf.write("x\22\3\2\2\2yz\7}\2\2z\24\3\2\2\2{|\7\177\2\2|\26\3\2")
        buf.write("\2\2}~\7%\2\2~\177\7%\2\2\177\u0083\3\2\2\2\u0080\u0082")
        buf.write("\13\2\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0086\u0087\7%\2\2\u0087\u0088\7")
        buf.write("%\2\2\u0088\u0089\3\2\2\2\u0089\u008a\b\f\2\2\u008a\30")
        buf.write("\3\2\2\2\u008b\u008c\7P\2\2\u008c\u008d\7w\2\2\u008d\u008e")
        buf.write("\7o\2\2\u008e\u008f\7d\2\2\u008f\u0090\7g\2\2\u0090\u00a8")
        buf.write("\7t\2\2\u0091\u0092\7D\2\2\u0092\u0093\7q\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\u0095\7n\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7c\2\2\u0097\u00a8\7p\2\2\u0098\u0099\7C\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7t\2\2\u009b\u009c\7c\2\2\u009c\u00a8")
        buf.write("\7{\2\2\u009d\u009e\7L\2\2\u009e\u009f\7U\2\2\u009f\u00a0")
        buf.write("\7Q\2\2\u00a0\u00a8\7P\2\2\u00a1\u00a2\7U\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a8\7i\2\2\u00a7\u008b\3\2\2\2\u00a7\u0091")
        buf.write("\3\2\2\2\u00a7\u0098\3\2\2\2\u00a7\u009d\3\2\2\2\u00a7")
        buf.write("\u00a1\3\2\2\2\u00a8\32\3\2\2\2\u00a9\u00ab\5\35\17\2")
        buf.write("\u00aa\u00ac\5\37\20\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00af\5!\21\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\34\3\2\2\2\u00b0")
        buf.write("\u00b2\t\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\36\3\2")
        buf.write("\2\2\u00b5\u00b9\7\60\2\2\u00b6\u00b8\t\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba \3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00be\t\3\2\2\u00bd\u00bf\t\4\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00c2\t")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\"\3\2\2\2\u00c5\u00c8")
        buf.write("\5%\23\2\u00c6\u00c8\5\'\24\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8$\3\2\2\2\u00c9\u00ca\7V\2\2\u00ca")
        buf.write("\u00cb\7t\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd")
        buf.write("&\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf\u00d0\7c\2\2\u00d0")
        buf.write("\u00d1\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("(\3\2\2\2\u00d4\u00d6\7&\2\2\u00d5\u00d7\t\5\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9*\3\2\2\2\u00da\u00de\t\6\2")
        buf.write("\2\u00db\u00dd\t\5\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e0")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write(",\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\7?\2\2\u00e2")
        buf.write("\u00eb\7?\2\2\u00e3\u00e4\7#\2\2\u00e4\u00eb\7?\2\2\u00e5")
        buf.write("\u00eb\t\7\2\2\u00e6\u00e7\7>\2\2\u00e7\u00eb\7?\2\2\u00e8")
        buf.write("\u00e9\7@\2\2\u00e9\u00eb\7?\2\2\u00ea\u00e1\3\2\2\2\u00ea")
        buf.write("\u00e3\3\2\2\2\u00ea\u00e5\3\2\2\2\u00ea\u00e6\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00eb.\3\2\2\2\u00ec\u00ed\7(\2\2")
        buf.write("\u00ed\u00f1\7(\2\2\u00ee\u00ef\7~\2\2\u00ef\u00f1\7~")
        buf.write("\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\60")
        buf.write("\3\2\2\2\u00f2\u00f3\7-\2\2\u00f3\62\3\2\2\2\u00f4\u00f5")
        buf.write("\7/\2\2\u00f5\64\3\2\2\2\u00f6\u00f7\t\b\2\2\u00f7\66")
        buf.write("\3\2\2\2\u00f8\u00f9\7#\2\2\u00f98\3\2\2\2\u00fa\u00fb")
        buf.write("\7-\2\2\u00fb\u00fc\7\60\2\2\u00fc:\3\2\2\2\u00fd\u00fe")
        buf.write("\7?\2\2\u00fe\u00ff\7?\2\2\u00ff\u0100\7\60\2\2\u0100")
        buf.write("<\3\2\2\2\u0101\u0102\7D\2\2\u0102\u0103\7t\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105\u0106\7m\2\2\u0106")
        buf.write(">\3\2\2\2\u0107\u0108\7E\2\2\u0108\u0109\7q\2\2\u0109")
        buf.write("\u010a\7p\2\2\u010a\u010b\7v\2\2\u010b\u010c\7k\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d\u010e\7w\2\2\u010e\u010f\7g\2\2\u010f")
        buf.write("@\3\2\2\2\u0110\u0111\7K\2\2\u0111\u0112\7h\2\2\u0112")
        buf.write("B\3\2\2\2\u0113\u0114\7G\2\2\u0114\u0115\7n\2\2\u0115")
        buf.write("\u0116\7k\2\2\u0116\u0117\7h\2\2\u0117D\3\2\2\2\u0118")
        buf.write("\u0119\7G\2\2\u0119\u011a\7n\2\2\u011a\u011b\7u\2\2\u011b")
        buf.write("\u011c\7g\2\2\u011cF\3\2\2\2\u011d\u011e\7Y\2\2\u011e")
        buf.write("\u011f\7j\2\2\u011f\u0120\7k\2\2\u0120\u0121\7n\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122H\3\2\2\2\u0123\u0124\7H\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7t\2\2\u0126J\3\2\2\2\u0127")
        buf.write("\u0128\7Q\2\2\u0128\u0129\7h\2\2\u0129L\3\2\2\2\u012a")
        buf.write("\u012b\7K\2\2\u012b\u012c\7p\2\2\u012cN\3\2\2\2\u012d")
        buf.write("\u012e\7E\2\2\u012e\u012f\7c\2\2\u012f\u0130\7n\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131P\3\2\2\2\u0132\u0133\7T\2\2\u0133")
        buf.write("\u0134\7g\2\2\u0134\u0135\7v\2\2\u0135\u0136\7w\2\2\u0136")
        buf.write("\u0137\7t\2\2\u0137\u0138\7p\2\2\u0138R\3\2\2\2\u0139")
        buf.write("\u013a\7H\2\2\u013a\u013b\7w\2\2\u013b\u013c\7p\2\2\u013c")
        buf.write("\u013d\7e\2\2\u013d\u013e\7v\2\2\u013e\u013f\7k\2\2\u013f")
        buf.write("\u0140\7q\2\2\u0140\u0141\7p\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7N\2\2\u0143\u0144\7g\2\2\u0144\u0145\7v\2\2\u0145")
        buf.write("V\3\2\2\2\u0146\u0147\7E\2\2\u0147\u0148\7q\2\2\u0148")
        buf.write("\u0149\7p\2\2\u0149\u014a\7u\2\2\u014a\u014b\7v\2\2\u014b")
        buf.write("\u014c\7c\2\2\u014c\u014d\7p\2\2\u014d\u014e\7v\2\2\u014e")
        buf.write("X\3\2\2\2\u014f\u0153\7$\2\2\u0150\u0152\5[.\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0156\u0157\7$\2\2\u0157\u0158\b-\3\2\u0158Z\3\2\2\2")
        buf.write("\u0159\u015f\n\t\2\2\u015a\u015b\7)\2\2\u015b\u015f\7")
        buf.write("$\2\2\u015c\u015d\7^\2\2\u015d\u015f\t\n\2\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015a\3\2\2\2\u015e\u015c\3\2\2\2\u015f")
        buf.write("\\\3\2\2\2\u0160\u0161\t\13\2\2\u0161^\3\2\2\2\u0162\u0164")
        buf.write("\t\f\2\2\u0163\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0168\b\60\2\2\u0168`\3\2\2\2\u0169\u016a\13\2")
        buf.write("\2\2\u016a\u016b\b\61\4\2\u016bb\3\2\2\2\u016c\u0170\7")
        buf.write("$\2\2\u016d\u016f\5[.\2\u016e\u016d\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\t\r\2\2")
        buf.write("\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b")
        buf.write("\62\5\2\u0177d\3\2\2\2\u0178\u017c\7$\2\2\u0179\u017b")
        buf.write("\5[.\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0183\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0180\7^\2\2\u0180\u0184\n\n\2\2")
        buf.write("\u0181\u0182\7)\2\2\u0182\u0184\n\16\2\2\u0183\u017f\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186")
        buf.write("\b\63\6\2\u0186f\3\2\2\2\u0187\u0188\7%\2\2\u0188\u0189")
        buf.write("\7%\2\2\u0189\u018d\3\2\2\2\u018a\u018c\13\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u0190\u0191\b\64\7\2\u0191h\3\2\2\2\32\2\u0083")
        buf.write("\u00a7\u00ab\u00ae\u00b3\u00b9\u00be\u00c3\u00c7\u00d6")
        buf.write("\u00d8\u00dc\u00de\u00ea\u00f0\u0153\u015e\u0165\u0170")
        buf.write("\u0174\u017c\u0183\u018d\b\b\2\2\3-\2\3\61\3\3\62\4\3")
        buf.write("\63\5\3\64\6")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    COMMENT = 11
    LIT_TYPE = 12
    NUMBER = 13
    BOOLEAN = 14
    CON_IDENTIFIERS = 15
    VAR_IDENTIFIERS = 16
    RELATION_OP = 17
    LOGIC_BINARY_OP = 18
    PLUS_OP = 19
    MINUS_OP = 20
    MULTIPLYING_OP = 21
    LOGICAL_UNARY_OP = 22
    PLUS_OP_STR = 23
    RELATION_OP_STR = 24
    BREAK = 25
    CONTINUE = 26
    IF = 27
    ELIF = 28
    ELSE = 29
    WHILE = 30
    FOR = 31
    OF = 32
    IN = 33
    CALL = 34
    RETURN = 35
    FUNCTION = 36
    LET = 37
    CONSTANT = 38
    STRINGLIT = 39
    SEP = 40
    WS = 41
    ERROR_CHAR = 42
    UNCLOSE_STRING = 43
    ILLEGAL_ESCAPE = 44
    UNTERMINATED_COMMENT = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'='", "'['", "']'", "'('", "')'", "'{'", 
            "'}'", "'+'", "'-'", "'!'", "'+.'", "'==.'", "'Break'", "'Continue'", 
            "'If'", "'Elif'", "'Else'", "'While'", "'For'", "'Of'", "'In'", 
            "'Call'", "'Return'", "'Function'", "'Let'", "'Constant'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LIT_TYPE", "NUMBER", "BOOLEAN", "CON_IDENTIFIERS", 
            "VAR_IDENTIFIERS", "RELATION_OP", "LOGIC_BINARY_OP", "PLUS_OP", 
            "MINUS_OP", "MULTIPLYING_OP", "LOGICAL_UNARY_OP", "PLUS_OP_STR", 
            "RELATION_OP_STR", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", 
            "WHILE", "FOR", "OF", "IN", "CALL", "RETURN", "FUNCTION", "LET", 
            "CONSTANT", "STRINGLIT", "SEP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "COMMENT", "LIT_TYPE", "NUMBER", 
                  "INT_PART", "DECIMAL_PART", "EXP_PART", "BOOLEAN", "TRUE", 
                  "FALSE", "CON_IDENTIFIERS", "VAR_IDENTIFIERS", "RELATION_OP", 
                  "LOGIC_BINARY_OP", "PLUS_OP", "MINUS_OP", "MULTIPLYING_OP", 
                  "LOGICAL_UNARY_OP", "PLUS_OP_STR", "RELATION_OP_STR", 
                  "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                  "OF", "IN", "CALL", "RETURN", "FUNCTION", "LET", "CONSTANT", 
                  "STRINGLIT", "CHAR_STRING", "SEP", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[43] = self.STRINGLIT_action 
            actions[47] = self.ERROR_CHAR_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            actions[50] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                y = str(self.text)
            	self.text = y[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text)
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		text = str(self.text)
            		if (text[-1] is '\r') or (text[-1] is '\n') or (text[-1] is '\b') or (text[-1] is '\t') or (text[-1] is '\f'):
            			raise UncloseString(text[1:-1])
            		else:
            			raise UncloseString(text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise IllegalEscape(str(self.text)[1:])
                
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise UnterminatedComment()
                
     


