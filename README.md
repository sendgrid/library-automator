# library-automator
For automating v3 endpoints into our 7 libraries

## Python

### Generate Tests

```bash
python app.py python tests > ./python/generated_files/unit_tests.py
```

### Generate Docs (Usage.md)

```bash
python app.py python usage > ./python/generated_files/USAGE.md
```

### Generate Examples

# this will populate the python/generated_files/examples folder
# cp -R ./python/generated_files/examples/ ../../../temp/sendgrid-python/examples/
```bash
python app.py python examples
```

## PHP

### Generate Tests

```bash
python app.py php tests > ./php/generated_files/unit_tests.py
```