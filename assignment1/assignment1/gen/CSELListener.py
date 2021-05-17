# Generated from D:/HK202/PPL/Assignment_1/assignment1/assignment1/initial/src/main/csel/parser\CSEL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete listener for a parse tree produced by CSELParser.
class CSELListener(ParseTreeListener):

    # Enter a parse tree produced by CSELParser#program.
    def enterProgram(self, ctx:CSELParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSELParser#program.
    def exitProgram(self, ctx:CSELParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSELParser#declares.
    def enterDeclares(self, ctx:CSELParser.DeclaresContext):
        pass

    # Exit a parse tree produced by CSELParser#declares.
    def exitDeclares(self, ctx:CSELParser.DeclaresContext):
        pass


    # Enter a parse tree produced by CSELParser#var_declare.
    def enterVar_declare(self, ctx:CSELParser.Var_declareContext):
        pass

    # Exit a parse tree produced by CSELParser#var_declare.
    def exitVar_declare(self, ctx:CSELParser.Var_declareContext):
        pass


    # Enter a parse tree produced by CSELParser#normal_declare.
    def enterNormal_declare(self, ctx:CSELParser.Normal_declareContext):
        pass

    # Exit a parse tree produced by CSELParser#normal_declare.
    def exitNormal_declare(self, ctx:CSELParser.Normal_declareContext):
        pass


    # Enter a parse tree produced by CSELParser#var_list.
    def enterVar_list(self, ctx:CSELParser.Var_listContext):
        pass

    # Exit a parse tree produced by CSELParser#var_list.
    def exitVar_list(self, ctx:CSELParser.Var_listContext):
        pass


    # Enter a parse tree produced by CSELParser#var_part.
    def enterVar_part(self, ctx:CSELParser.Var_partContext):
        pass

    # Exit a parse tree produced by CSELParser#var_part.
    def exitVar_part(self, ctx:CSELParser.Var_partContext):
        pass


    # Enter a parse tree produced by CSELParser#var_normal.
    def enterVar_normal(self, ctx:CSELParser.Var_normalContext):
        pass

    # Exit a parse tree produced by CSELParser#var_normal.
    def exitVar_normal(self, ctx:CSELParser.Var_normalContext):
        pass


    # Enter a parse tree produced by CSELParser#const_declare.
    def enterConst_declare(self, ctx:CSELParser.Const_declareContext):
        pass

    # Exit a parse tree produced by CSELParser#const_declare.
    def exitConst_declare(self, ctx:CSELParser.Const_declareContext):
        pass


    # Enter a parse tree produced by CSELParser#var_list_const.
    def enterVar_list_const(self, ctx:CSELParser.Var_list_constContext):
        pass

    # Exit a parse tree produced by CSELParser#var_list_const.
    def exitVar_list_const(self, ctx:CSELParser.Var_list_constContext):
        pass


    # Enter a parse tree produced by CSELParser#var_part_const.
    def enterVar_part_const(self, ctx:CSELParser.Var_part_constContext):
        pass

    # Exit a parse tree produced by CSELParser#var_part_const.
    def exitVar_part_const(self, ctx:CSELParser.Var_part_constContext):
        pass


    # Enter a parse tree produced by CSELParser#var_const.
    def enterVar_const(self, ctx:CSELParser.Var_constContext):
        pass

    # Exit a parse tree produced by CSELParser#var_const.
    def exitVar_const(self, ctx:CSELParser.Var_constContext):
        pass


    # Enter a parse tree produced by CSELParser#var.
    def enterVar(self, ctx:CSELParser.VarContext):
        pass

    # Exit a parse tree produced by CSELParser#var.
    def exitVar(self, ctx:CSELParser.VarContext):
        pass


    # Enter a parse tree produced by CSELParser#function_declare.
    def enterFunction_declare(self, ctx:CSELParser.Function_declareContext):
        pass

    # Exit a parse tree produced by CSELParser#function_declare.
    def exitFunction_declare(self, ctx:CSELParser.Function_declareContext):
        pass


    # Enter a parse tree produced by CSELParser#parameters.
    def enterParameters(self, ctx:CSELParser.ParametersContext):
        pass

    # Exit a parse tree produced by CSELParser#parameters.
    def exitParameters(self, ctx:CSELParser.ParametersContext):
        pass


    # Enter a parse tree produced by CSELParser#param_list.
    def enterParam_list(self, ctx:CSELParser.Param_listContext):
        pass

    # Exit a parse tree produced by CSELParser#param_list.
    def exitParam_list(self, ctx:CSELParser.Param_listContext):
        pass


    # Enter a parse tree produced by CSELParser#func_body.
    def enterFunc_body(self, ctx:CSELParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by CSELParser#func_body.
    def exitFunc_body(self, ctx:CSELParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by CSELParser#func_body_stm.
    def enterFunc_body_stm(self, ctx:CSELParser.Func_body_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#func_body_stm.
    def exitFunc_body_stm(self, ctx:CSELParser.Func_body_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#stm.
    def enterStm(self, ctx:CSELParser.StmContext):
        pass

    # Exit a parse tree produced by CSELParser#stm.
    def exitStm(self, ctx:CSELParser.StmContext):
        pass


    # Enter a parse tree produced by CSELParser#assign_stm.
    def enterAssign_stm(self, ctx:CSELParser.Assign_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#assign_stm.
    def exitAssign_stm(self, ctx:CSELParser.Assign_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#index_exp.
    def enterIndex_exp(self, ctx:CSELParser.Index_expContext):
        pass

    # Exit a parse tree produced by CSELParser#index_exp.
    def exitIndex_exp(self, ctx:CSELParser.Index_expContext):
        pass


    # Enter a parse tree produced by CSELParser#index_op.
    def enterIndex_op(self, ctx:CSELParser.Index_opContext):
        pass

    # Exit a parse tree produced by CSELParser#index_op.
    def exitIndex_op(self, ctx:CSELParser.Index_opContext):
        pass


    # Enter a parse tree produced by CSELParser#index.
    def enterIndex(self, ctx:CSELParser.IndexContext):
        pass

    # Exit a parse tree produced by CSELParser#index.
    def exitIndex(self, ctx:CSELParser.IndexContext):
        pass


    # Enter a parse tree produced by CSELParser#key_exp.
    def enterKey_exp(self, ctx:CSELParser.Key_expContext):
        pass

    # Exit a parse tree produced by CSELParser#key_exp.
    def exitKey_exp(self, ctx:CSELParser.Key_expContext):
        pass


    # Enter a parse tree produced by CSELParser#key_op.
    def enterKey_op(self, ctx:CSELParser.Key_opContext):
        pass

    # Exit a parse tree produced by CSELParser#key_op.
    def exitKey_op(self, ctx:CSELParser.Key_opContext):
        pass


    # Enter a parse tree produced by CSELParser#if_stm.
    def enterIf_stm(self, ctx:CSELParser.If_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#if_stm.
    def exitIf_stm(self, ctx:CSELParser.If_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#stm_else_if.
    def enterStm_else_if(self, ctx:CSELParser.Stm_else_ifContext):
        pass

    # Exit a parse tree produced by CSELParser#stm_else_if.
    def exitStm_else_if(self, ctx:CSELParser.Stm_else_ifContext):
        pass


    # Enter a parse tree produced by CSELParser#for_stm.
    def enterFor_stm(self, ctx:CSELParser.For_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#for_stm.
    def exitFor_stm(self, ctx:CSELParser.For_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#for_in.
    def enterFor_in(self, ctx:CSELParser.For_inContext):
        pass

    # Exit a parse tree produced by CSELParser#for_in.
    def exitFor_in(self, ctx:CSELParser.For_inContext):
        pass


    # Enter a parse tree produced by CSELParser#for_of.
    def enterFor_of(self, ctx:CSELParser.For_ofContext):
        pass

    # Exit a parse tree produced by CSELParser#for_of.
    def exitFor_of(self, ctx:CSELParser.For_ofContext):
        pass


    # Enter a parse tree produced by CSELParser#while_stm.
    def enterWhile_stm(self, ctx:CSELParser.While_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#while_stm.
    def exitWhile_stm(self, ctx:CSELParser.While_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#break_stm.
    def enterBreak_stm(self, ctx:CSELParser.Break_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#break_stm.
    def exitBreak_stm(self, ctx:CSELParser.Break_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#continue_stm.
    def enterContinue_stm(self, ctx:CSELParser.Continue_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#continue_stm.
    def exitContinue_stm(self, ctx:CSELParser.Continue_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#call_stm.
    def enterCall_stm(self, ctx:CSELParser.Call_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#call_stm.
    def exitCall_stm(self, ctx:CSELParser.Call_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#call.
    def enterCall(self, ctx:CSELParser.CallContext):
        pass

    # Exit a parse tree produced by CSELParser#call.
    def exitCall(self, ctx:CSELParser.CallContext):
        pass


    # Enter a parse tree produced by CSELParser#pass_param.
    def enterPass_param(self, ctx:CSELParser.Pass_paramContext):
        pass

    # Exit a parse tree produced by CSELParser#pass_param.
    def exitPass_param(self, ctx:CSELParser.Pass_paramContext):
        pass


    # Enter a parse tree produced by CSELParser#params.
    def enterParams(self, ctx:CSELParser.ParamsContext):
        pass

    # Exit a parse tree produced by CSELParser#params.
    def exitParams(self, ctx:CSELParser.ParamsContext):
        pass


    # Enter a parse tree produced by CSELParser#param.
    def enterParam(self, ctx:CSELParser.ParamContext):
        pass

    # Exit a parse tree produced by CSELParser#param.
    def exitParam(self, ctx:CSELParser.ParamContext):
        pass


    # Enter a parse tree produced by CSELParser#return_stm.
    def enterReturn_stm(self, ctx:CSELParser.Return_stmContext):
        pass

    # Exit a parse tree produced by CSELParser#return_stm.
    def exitReturn_stm(self, ctx:CSELParser.Return_stmContext):
        pass


    # Enter a parse tree produced by CSELParser#exp.
    def enterExp(self, ctx:CSELParser.ExpContext):
        pass

    # Exit a parse tree produced by CSELParser#exp.
    def exitExp(self, ctx:CSELParser.ExpContext):
        pass


    # Enter a parse tree produced by CSELParser#exp1.
    def enterExp1(self, ctx:CSELParser.Exp1Context):
        pass

    # Exit a parse tree produced by CSELParser#exp1.
    def exitExp1(self, ctx:CSELParser.Exp1Context):
        pass


    # Enter a parse tree produced by CSELParser#exp2.
    def enterExp2(self, ctx:CSELParser.Exp2Context):
        pass

    # Exit a parse tree produced by CSELParser#exp2.
    def exitExp2(self, ctx:CSELParser.Exp2Context):
        pass


    # Enter a parse tree produced by CSELParser#exp3.
    def enterExp3(self, ctx:CSELParser.Exp3Context):
        pass

    # Exit a parse tree produced by CSELParser#exp3.
    def exitExp3(self, ctx:CSELParser.Exp3Context):
        pass


    # Enter a parse tree produced by CSELParser#exp4.
    def enterExp4(self, ctx:CSELParser.Exp4Context):
        pass

    # Exit a parse tree produced by CSELParser#exp4.
    def exitExp4(self, ctx:CSELParser.Exp4Context):
        pass


    # Enter a parse tree produced by CSELParser#exp5.
    def enterExp5(self, ctx:CSELParser.Exp5Context):
        pass

    # Exit a parse tree produced by CSELParser#exp5.
    def exitExp5(self, ctx:CSELParser.Exp5Context):
        pass


    # Enter a parse tree produced by CSELParser#exp6.
    def enterExp6(self, ctx:CSELParser.Exp6Context):
        pass

    # Exit a parse tree produced by CSELParser#exp6.
    def exitExp6(self, ctx:CSELParser.Exp6Context):
        pass


    # Enter a parse tree produced by CSELParser#exp7.
    def enterExp7(self, ctx:CSELParser.Exp7Context):
        pass

    # Exit a parse tree produced by CSELParser#exp7.
    def exitExp7(self, ctx:CSELParser.Exp7Context):
        pass


    # Enter a parse tree produced by CSELParser#index_operator.
    def enterIndex_operator(self, ctx:CSELParser.Index_operatorContext):
        pass

    # Exit a parse tree produced by CSELParser#index_operator.
    def exitIndex_operator(self, ctx:CSELParser.Index_operatorContext):
        pass


    # Enter a parse tree produced by CSELParser#key_operator.
    def enterKey_operator(self, ctx:CSELParser.Key_operatorContext):
        pass

    # Exit a parse tree produced by CSELParser#key_operator.
    def exitKey_operator(self, ctx:CSELParser.Key_operatorContext):
        pass


    # Enter a parse tree produced by CSELParser#exp8.
    def enterExp8(self, ctx:CSELParser.Exp8Context):
        pass

    # Exit a parse tree produced by CSELParser#exp8.
    def exitExp8(self, ctx:CSELParser.Exp8Context):
        pass


    # Enter a parse tree produced by CSELParser#operands.
    def enterOperands(self, ctx:CSELParser.OperandsContext):
        pass

    # Exit a parse tree produced by CSELParser#operands.
    def exitOperands(self, ctx:CSELParser.OperandsContext):
        pass


    # Enter a parse tree produced by CSELParser#lit.
    def enterLit(self, ctx:CSELParser.LitContext):
        pass

    # Exit a parse tree produced by CSELParser#lit.
    def exitLit(self, ctx:CSELParser.LitContext):
        pass


    # Enter a parse tree produced by CSELParser#json.
    def enterJson(self, ctx:CSELParser.JsonContext):
        pass

    # Exit a parse tree produced by CSELParser#json.
    def exitJson(self, ctx:CSELParser.JsonContext):
        pass


    # Enter a parse tree produced by CSELParser#key_value.
    def enterKey_value(self, ctx:CSELParser.Key_valueContext):
        pass

    # Exit a parse tree produced by CSELParser#key_value.
    def exitKey_value(self, ctx:CSELParser.Key_valueContext):
        pass


    # Enter a parse tree produced by CSELParser#array.
    def enterArray(self, ctx:CSELParser.ArrayContext):
        pass

    # Exit a parse tree produced by CSELParser#array.
    def exitArray(self, ctx:CSELParser.ArrayContext):
        pass


    # Enter a parse tree produced by CSELParser#element.
    def enterElement(self, ctx:CSELParser.ElementContext):
        pass

    # Exit a parse tree produced by CSELParser#element.
    def exitElement(self, ctx:CSELParser.ElementContext):
        pass



del CSELParser