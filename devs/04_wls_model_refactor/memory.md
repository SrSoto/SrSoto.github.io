# Watchlists' NLP-Model rebuild and FP-lowering 

Rebuilt our name-matching model from TensorFlow to PyTorch and re-trained with a better oriented dataset for our Watchlists name-matching use case.

* Starting point: Slower and less accurate model from legacy trainings.
* Ending point: New, faster and better model written from zero on PyTorch.
* Results: Lowered False Positive (FP) rates from ~8% to ~3% based on our service tests and from ~5% to ~1% on production environments.