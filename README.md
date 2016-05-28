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

### Generate Docs (Usage.md)

```bash
python app.py php usage > ./php/generated_files/USAGE.md
cp ./php/generated_files/USAGE.md <path-to>/sendgrid-php/
```

### Generate Examples

This will populate the php/generated_files/examples folder
```bash
python app.py php examples
cp -R ./php/generated_files/examples/ <path-to>/sendgrid-php/examples/
```

## Ruby

### Generate Tests

```bash
python app.py ruby tests > ./ruby/generated_files/unit_tests.rb
```

### Generate Docs (Usage.md)

```bash
python app.py ruby usage > ./ruby/generated_files/USAGE.md
cp ./ruby/generated_files/USAGE.md <path-to>/sendgrid-ruby/
```

### Generate Examples

This will populate the ruby/generated_files/examples folder
```bash
python app.py ruby examples
cp -R ./ruby/generated_files/examples/ <path-to>/sendgrid-ruby/examples/
```

## Java

### Generate Tests

```bash
python app.py java tests > ./java/generated_files/unit_tests.java
```

### Generate Docs (Usage.md)

```bash
python app.py java usage > ./java/generated_files/USAGE.md
cp ./java/generated_files/USAGE.md <path-to>/sendgrid-java/
```

### Generate Examples

This will populate the java/generated_files/examples folder
```bash
python app.py java examples
cp -R ./java/generated_files/examples/ <path-to>/sendgrid-java/examples/

# Tests

`python -m unittest discover -v`