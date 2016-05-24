import sys

# Please see the README for usage instructions

args = []
for arg in sys.argv:
    args.append(arg)

if "python" in args:
    from python.code_generator import CodeGenerator
    code_generator = CodeGenerator("python")
    if "tests" in args:
        print code_generator.generate_tests()
    if "usage" in args:
        print code_generator.generate_docs()
    if "examples" in args:
        code_generator.generate_examples()
