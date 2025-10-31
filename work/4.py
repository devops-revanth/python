#!/usr/bin/env python3

""" def function_name(parameters):
    Docstring: describe purpose
    code block
    return value
"""

# CPU Health Function

def check_cpu(usage):
    if usage > 90:
        return "High CPU Load"
    else:
        return "Load is normal"
    
print(check_cpu(75))
print(check_cpu(92))