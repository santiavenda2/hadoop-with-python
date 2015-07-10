from mrjob.job import MRJob
from mrjob.step import MRStep

mean = 0


class MRJobVariance(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_variance,
                   combiner=self.combiner_variance,
                   reducer=self.reducer_variance),
            # MRStep(reducer=self.reducer_find_max_word)
        ]

    def mapper_variance(self, _, line):
        # yield each value in the line
        value = float(line.strip()[:-1])
        yield None, ((value - mean) ** 2, 1)

    def combiner_variance(self, _, sum_and_counts):
        # optimization: sum the words we've seen so far
        suma_total = 0
        count_total = 0
        for suma, counts in sum_and_counts:
            suma_total += float(suma)
            count_total += int(counts)
        yield _, (suma_total, count_total)

    def reducer_variance(self, _, sum_and_counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        # yield None, (sum(counts), word)
        suma_total = 0
        count_total = 0
        for suma, counts in sum_and_counts:
            suma_total += float(suma)
            count_total += int(counts)
        yield suma_total / (count_total - 1)

    # discard the key; it is just None
    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        yield max(word_count_pairs)


if __name__ == '__main__':
    MRJobVariance.run()
