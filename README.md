This is the result of a short coding dojo (< 1h00) made during SoCraTes Rennes 2024,
with Seow Chin, Abbas, Thomas and Alex.
With a little more time we certainly could have improved more the code readability.

# Gilded Rose starting position in Python

## Run the unit tests from the Command-Line

```
python test_gilded_rose.py
```

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```
python texttest_fixture.py 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. You will need to specify the Python executable and interpreter in [config.gr](../texttests/config.gr). Uncomment these lines:

    executable:${TEXTTEST_HOME}/python/texttest_fixture.py
    interpreter:python
