def compute_total_iterations_in_training_loop(num_samples: int, batch_size: int, num_epochs: int) -> int:
  """Returns the total number of iterations for which a model is trained.
  
  https://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks
  """
  
  return (num_samples//batch_size) * num_epochs
