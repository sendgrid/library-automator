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

if "ruby" in args:
    ruby_code_generator = CodeGenerator("ruby")
    if "tests" in args:
        print ruby_code_generator.generate_tests()
    if "usage" in args:
        print ruby_code_generator.generate_docs()
    if "examples" in args:
        ruby_code_generator.generate_examples()

if "java" in args:
    java_code_generator = CodeGenerator("java")
    if "tests" in args:
        print java_code_generator.generate_tests()
    if "usage" in args:
        print java_code_generator.generate_docs()
    if "examples" in args:
        java_code_generator.generate_examples()

if "nodejs" in args:
    nodejs_code_generator = CodeGenerator("nodejs")
    if "tests" in args:
        print nodejs_code_generator.generate_tests()
    if "usage" in args:
        print nodejs_code_generator.generate_docs()
    if "examples" in args:
        nodejs_code_generator.generate_examples()

if "csharp" in args:
    csharp_code_generator = CodeGenerator("csharp")
    if "tests" in args:
        print csharp_code_generator.generate_tests()
    if "usage" in args:
        print csharp_code_generator.generate_docs()
    if "examples" in args:
        csharp_code_generator.generate_examples()
