import sys
from code_generator import CodeGenerator
# Please see the README for usage instructions

args = []
for arg in sys.argv:
    args.append(arg)

if "python" in args:
    python_code_generator = CodeGenerator("python")
    if "tests" in args:
        print python_code_generator.generate_tests()
    if "usage" in args:
        print python_code_generator.generate_docs()
    if "examples" in args:
        python_code_generator.generate_examples()

if "php" in args:
    php_code_generator = CodeGenerator("php")
    if "tests" in args:
        print php_code_generator.generate_tests()
    if "usage" in args:
        print php_code_generator.generate_docs()
    if "examples" in args:
        php_code_generator.generate_examples()