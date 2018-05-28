import sys, os

sys.path.extend (['.', '..' ])

from pycparser import c_parser, c_ast, parse_file
CPPPATH = 'cpp.exe'

###################################################################################################

def fctGetAstFromCFile ( filename, cpp_args = [] ) :
    """ Parse C file and print static memory usage and data type dictionary. """

    try :
        astNode = parse_file( filename, use_cpp=True, cpp_path=CPPPATH, cpp_args = cpp_args )
        return astNode
    except c_parser.ParseError :
        error = sys.exc_info ()[1]
        print 'Parse error : %s' % str (error)
        return None
# end def fctGetAstFromCFile
###################################################################################################

def fctGlobalVariableDict(astObject):
    dictGlobalVariables = {}
    if isinstance (astObject, c_ast.Decl):
        declType = astObject.type
        if type(declType) == c_ast.TypeDecl and type(declType) != c_ast.Struct \
        and (type (declType) != c_ast.PtrDecl) and (type (declType) != c_ast.FuncDecl) \
        and (type (declType.type) != c_ast.Union) and type(declType.type) != c_ast.Struct :
            dictGlobalVariables[astObject.name] = declType.type.names[0]
        elif type(declType) == c_ast.ArrayDecl and type(declType.type) != c_ast.ArrayDecl and type(declType.type) != c_ast.Struct :
            dictGlobalVariables[astObject.name] = declType.type.type.names[0]
        elif type(declType) == c_ast.ArrayDecl and type(declType.type) == c_ast.ArrayDecl and type(declType.type) != c_ast.Struct:
            dictGlobalVariables[astObject.name] = declType.type.type.type.names[0]

    return dictGlobalVariables
# end def fctGlobalVariableDict
###################################################################################################

def fctGenASTDicts(astNode):
    dictGlobalVariables = {}
    if isinstance(astNode.ext, list):
        if len(astNode.ext) == 0:
            print 'No sub-nodes to process found in AST'

    for astObject in astNode.ext:
        dictGlobalVariables.update(fctGlobalVariableDict(astObject))

    print dictGlobalVariables
# end def fctGenASTDicts
###################################################################################################

##### main 

if __name__ == '__main__' :
    if len (sys.argv) > 1 :
        filename  = sys.argv [1]
    else :

        filename = 'Simple.c'

        if filename == 'Simple.c' :
            LOCATION = os.getcwd()

    include_dir = [ r'-U__GNUC__'
                  , r'-I./fake_libc_include'
                  ]

    astNode = fctGetAstFromCFile( os.path.join(LOCATION, filename), cpp_args = include_dir )
    
    if not isinstance (astNode, c_ast.FileAST) :
        print "AST-Node not of expected type"

    fctGenASTDicts( astNode )
### __END__ Parse_C_Code