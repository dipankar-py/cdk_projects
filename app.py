#!/usr/bin/env python
import os

#from aws_cdk import core as cdk
from aws_cdk import core

from dip_cdk_project.dip_cdk_project_stack import DipCdkProjectStack


app = core.App()
DipCdkProjectStack(app, "DipCdkProjectStack" )

app.synth()
