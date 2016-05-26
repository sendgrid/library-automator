For automating docs (USAGE.md), unit tests and examples into our 7 SendGrid open source client libraries.

## Python

### Generate Tests

```bash
python app.py python tests > ./python/generated_files/unit_tests.py
cp ./python/generated_files/examples/unit_tests.md <path-to>/sendgrid-python/examples/test_sendgrid.py
```

### Generate Docs (Usage.md)

```bash
python app.py python usage > ./python/generated_files/USAGE.md
cp ./python/generated_files/USAGE.md <path-to>/sendgrid-python/
```

### Generate Examples

This will populate the python/generated_files/examples folder
```bash
python app.py python examples
cp -R ./python/generated_files/examples/ <path-to>/sendgrid-python/examples/
```

## PHP

### Generate Tests

```bash
python app.py php tests > ./php/generated_files/unit_tests.php
```

```bash
python app.py php usage > ./php/generated_files/USAGE.md
cp ./php/generated_files/USAGE.md <path-to>/sendgrid-php/
```