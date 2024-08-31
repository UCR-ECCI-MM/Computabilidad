from lexer import tokenize

def main():
    # test it out
    data = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE health-topics PUBLIC "-//NLM//DTD health-topics //EN" "https://medlineplus.gov/xml/mplus_topics.dtd">
    <health-topics total="2044" date-generated="08/10/2024 02:30:32">
    <health-topic meta-desc="If you are being tested for Type 2 diabetes, your doctor gives you an A1C test. The test is also used to monitor your A1C levels." title="A1C" url="https://medlineplus.gov/a1c.html" id="6308" language="English" date-created="12/22/2015">
    <also-called>Glycohemoglobin</also-called>
    <also-called>HbA1C</also-called>
    <also-called>Hemoglobin A1C test</also-called>'''

    tokenize(data)


if __name__ == "__main__":
    main()
