import os
os.environ["_JAVA_OPTIONS"] = "--add-opens=java.base/java.security=ALL-UNNAMED"

import logging
from pyspark import SparkContext

# Step 0: Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting SparkContext...")
        sc = SparkContext("local[*]", "SimpleWordCount")

        logger.info("Reading file into RDD...")
        rdd = sc.textFile("sample.txt")  # Make sure this file exists

        logger.info("Splitting lines into words...")
        words = rdd.flatMap(lambda line: line.split())

        logger.info("Mapping words to (word, 1) pairs...")
        word_pairs = words.map(lambda word: (word, 1))

        logger.info("Reducing by key to get word counts...")
        word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

        logger.info("Caching the word count RDD...")
        word_counts.cache()

        logger.info("Collecting the results...")
        output = word_counts.collect()

        logger.info("Printing word counts:")
        for word, count in output:
            print(f"{word}: {count}")

        # Optionally save to output
        # logger.info("Saving results to file...")
        # word_counts.saveAsTextFile("output_word_counts")

    except Exception as e:
        logger.error("An error occurred!", exc_info=True)

if __name__ == "__main__":
    main()
