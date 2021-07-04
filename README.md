
# Advanced argument parser

This parser is based on an ordinary argparse module.
List of parameters to be requested with default values contains in YAML config.  

The best library for these purpose is the [Hydra](https://hydra.cc). If it's possible, then it is better to try Hydra.
In cases when Hydra is not available, I use this parser.  

Key points:
- Config with default values for params requires as path to YAML file or `Dict[str, Any]` object
- This parser maintains the structure of stacked dictionaries with **only one level**
  (required type `Dict[str, Union[Any, Dict[str, Any]]]`)
- Set own description of the parser with method `set_parser_desc`
- Set a help description (`help` attr in argparse.add_argument method) for any input parameters 
  contains in YAML config with method `add_params_desc`
- Use `parse_args` method to run (use `verbose` option to manage parser silence). 
  Output dict will have the same structure as the input dict parsed from YAML config
- See an example [here](https://github.com/gorodnitskiy/advanced_parser/tree/master/example)
- For installing use: `pip install /path/to/advanced_argparse`
