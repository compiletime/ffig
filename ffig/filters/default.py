from ffig.cppmodel import TypeKind


def c_param(arg):
    """Get a string representation of the native type and name for C function invocation.

    Arguments:
        arg: (cppmodel.Arg) Argument type and name as a single value.

    Returns:
        string: The string representation of the native type and variable name.

    This function is used to provide `c_double` in:

    ```
    ("Shape_Circle_create",
    [c_double,  POINTER(c_object_p)],
    c_int),
    ```

    """
    pass


def c_arg_value(arg):
    """Code to extract a c-api representation of a native argument.
    
    Arguments:
        arg: (cppmodel.Arg) Argument type and name as a single value.

    Returns:
        string: Code to extract a c-api representation of a native argument.

    This function is used to provide `shape.c_obj_` in:

    ```
    int rc = Shape_AbstractShape_is_equal(c_obj_, shape.c_obj_, out rv);
    ```

    """
    pass


def output_param_type(typ):
    """Get a string representation of the native type used for an output parameter.

    Arguments:
        typ: (cppmodel.Type) of output parameter

    Returns:
        string: The output parameter type.

    This function is used to provide `double* rv` in:

    `int shape_area(ShapePtr shape, double* rv);`
    """
    pass


def return_type(typ):
    """Get a string representation of a native return type from a C++ return type.

    Arguments:
        typ: (cppmodel.Type) function return type.

    Returns:
        string: The native return type.

    This function is used to provide `double` in:

    `double area();`
    """
    pass


def construct_output_value(typ, rv):
    """Code to construct a return parameter to be passed into a wrapped C-API invocation.

    Arguments:
        typ: (cppmodel.Type) of return parameter.
        rv: (string) to be used as the variable name in the returned code.

    Return:
        string: A code snippet to construct an output parameter of the correct kind.

    This function is used to provide `int rv = 0;` in:

    ```
    int rv = 0;                                                                     
    int rc = c_api_call_(arg1, arg2, &rv);
    ```
    """
    pass


def extract_return_value(typ, rv):
    """Code to turn a c-api output parameter value into a return value.

    Arguments:
        typ: (cppmodel.Type) of return parameter.
        rv: (string) to be used as the output parameter variable name.

    Return:
        string: A code snippet to extract a return value from an output parameter.

    This function is used to provide `Marshall.PtrToStringAnsi(rv)` in:

    ```
    return Marshal.PtrToStringAnsi(rv);
    ```
    """
    pass
