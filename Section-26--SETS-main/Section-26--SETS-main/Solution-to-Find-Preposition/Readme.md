quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""

prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}

# Add your code here.
def find_prep(p_quote):
    words = p_quote.split()
    preps_used = prep.intersection(words)
    return preps_used

print(find_prep(quote))