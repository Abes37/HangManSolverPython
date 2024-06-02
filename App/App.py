import unittest
import subprocess
import sys

def run_tests():
    loader = unittest.TestLoader()
    tests = loader.discover('Tests', pattern='test_*.py')
    testRunner = unittest.TextTestRunner()
    result = testRunner.run(tests)
    return result.wasSuccessful()

def start_app():
    subprocess.run([sys.executable, 'App/main.py'])

if __name__ == "__main__":
    if run_tests():
        print("Tests passed. Starting the application...")
        start_app()
    else:
        print("Tests failed. Fix the issues before starting the application.")
