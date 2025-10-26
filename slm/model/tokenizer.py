class SimpleTokenizer:
    """
    Minimal tokenizer for SLM.
    """

    def __init__(self, vocab_size=8000):
        self.vocab_size = vocab_size
        self.word2id = {}
        self.id2word = {}
        self._build()

    def _build(self):
        specials = ["<pad>", "<unk>", "<bos>", "<eos>"]
        for i, w in enumerate(specials):
            self.word2id[w] = i
            self.id2word[i] = w

        for i in range(4, self.vocab_size):
            t = f"tok{i}"
            self.word2id[t] = i
            self.id2word[i] = t

    def encode(self, text):
        ids = [self.word2id.get(w, self.word2id["<unk>"]) for w in text.split()]
        ids.append(self.word2id["<eos>"])
        return ids

    def decode(self, ids):
        return " ".join(self.id2word.get(i, "<unk>") for i in ids)
