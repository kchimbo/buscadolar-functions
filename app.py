#!/usr/bin/env python3

import aws_cdk as cdk

from buscadolar_functions.buscadolar_functions_stack import BuscadolarFunctionsStack


app = cdk.App()
BuscadolarFunctionsStack(app, "buscadolar-functions")

app.synth()
