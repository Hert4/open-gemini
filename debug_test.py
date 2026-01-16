#!/usr/bin/env python3
"""
Debug script to identify which import is causing the bus error
"""

print("Starting debug test...")

try:
    print("1. Testing basic imports...")
    import sys
    import os
    print("   Basic imports successful")
    
    print("2. Testing google.generativeai...")
    import google.generativeai
    print("   google.generativeai import successful")
    
    print("3. Testing litellm...")
    import litellm
    print("   litellm import successful")
    
    print("4. Testing other key dependencies...")
    import requests
    import pydantic
    import tiktoken
    print("   Other key dependencies successful")
    
    print("5. Testing import of interpreter core modules...")
    from interpreter.core.llm import Llm
    print("   Llm import successful")
    
    print("6. Testing import of main interpreter...")
    from interpreter.core.core import OpenInterpreter
    print("   OpenInterpreter import successful")
    
    print("SUCCESS: All imports completed without bus error!")
    
except Exception as e:
    print(f"ERROR at step: {e}")
    import traceback
    traceback.print_exc()