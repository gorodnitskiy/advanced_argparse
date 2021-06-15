from typing import Dict, Any, Optional, Union

from collections import defaultdict
import copy
import argparse
import yaml


def yaml_parser(
    path: Optional[str] = None,
    data: Optional[str] = None,
    loader: yaml.Loader = yaml.SafeLoader
) -> Dict[str, Any]:
    if path:
        with open(r'{}'.format(path)) as file:
            return yaml.load(file, Loader=loader)

    elif data:
        return yaml.load(data, Loader=loader)

    else:
        raise ValueError('Either a path or data should be defined as input')


class AdvancedParser:
    parser_desc = """
        This parser is based on an ordinary argparse module
        with default values contained in the YAML config.

        If it's possible, then it is better to try Hydra library
        (https://hydra.cc) for these purposes.
    """
    args_desc = defaultdict(lambda: None)

    def __init__(
        self,
        cfg: Union[str, Dict[str, Any]],
        yaml_loader: Optional[yaml.Loader] = None,
        delimiter: str = '___',
        logger: Any = None
    ) -> None:
        self._logger = logger
        self._delimiter = delimiter
        if yaml_loader is None:
            yaml_loader = yaml.SafeLoader

        if isinstance(cfg, str):
            self.default_cfg = yaml_parser(
                path=cfg,
                loader=yaml_loader
            )
        else:
            self.default_cfg = cfg

    @classmethod
    def set_parser_desc(cls, desc: str) -> None:
        cls.parser_desc = desc

    @classmethod
    def add_params_desc(cls, args_desc: Dict[str, Any]) -> None:
        cls.args_desc.update(args_desc)

    @classmethod
    def set_delimiter(cls, delimiter: str) -> None:
        cls._delimiter = delimiter

    @property
    def config(self) -> Dict[str, Any]:
        return self.default_cfg

    @staticmethod
    def _cls_logging_(message: str, logger: Any) -> None:
        if logger:
            logger.info(message)
        else:
            print(message)

    def _replace_values_(
        self,
        arg_name: str,
        arg_value: Any,
        parser_args: Dict[str, Any],
        base_args: Dict[str, Any],
        verbose: bool,
        high_arg_name: Optional[str] = None
    ) -> None:
        if high_arg_name:
            curr_name = ''.join([high_arg_name, self._delimiter, arg_name])
        else:
            curr_name = arg_name

        if arg_value != parser_args[curr_name]:
            if verbose:
                AdvancedParser._cls_logging_(
                    '{}: **CHANGED**: {} -> {}'.format(
                        curr_name, arg_value, parser_args[curr_name]),
                    logger=self._logger
                )
            base_args[arg_name] = parser_args[curr_name]

        else:
            if verbose:
                AdvancedParser._cls_logging_(
                    '{}: {}'.format(curr_name, arg_value),
                    logger=self._logger
                )

    def parse_args(
        self,
        verbose: bool = False,
        delimiter: Optional[str] = None
    ) -> Dict[str, Any]:
        if delimiter:
            self.set_delimiter(delimiter)

        default_cfg = copy.deepcopy(self.default_cfg)
        flat_cfg = {}
        for arg_name, arg_value in default_cfg.items():
            if isinstance(arg_value, dict):
                for sub_arg_name, sub_arg_value in arg_value.items():
                    arg_name_long = ''.join([arg_name, self._delimiter, sub_arg_name])
                    flat_cfg[arg_name_long] = sub_arg_value

            else:
                flat_cfg[arg_name] = arg_value

        arg_parser = argparse.ArgumentParser(description=self.parser_desc)
        for arg_name, arg_value in flat_cfg.items():
            param_desc = self.args_desc[arg_name]
            if param_desc is not None:
                param_desc = str(param_desc)
            arg_parser.add_argument(
                '--{}'.format(arg_name),
                metavar='<{}>'.format(arg_name),
                default=arg_value,
                type=type(arg_value),
                help=param_desc
            )

        parser_args, unknown = arg_parser.parse_known_args()
        if verbose and unknown:
            AdvancedParser._cls_logging_(
                '**SOME ARGS ARE UNKNOWN**: {}'.format(unknown),
                logger=self._logger
            )

        parser_args_dict = vars(parser_args)
        for arg_name, arg_value in default_cfg.items():
            if isinstance(arg_value, dict):
                for sub_arg_name, sub_arg_value in arg_value.items():
                    AdvancedParser._replace_values_(
                        self, sub_arg_name, sub_arg_value, parser_args_dict,
                        arg_value, verbose, high_arg_name=arg_name
                    )

            else:
                AdvancedParser._replace_values_(
                    self, arg_name, arg_value, parser_args_dict,
                    default_cfg, verbose
                )

        return default_cfg
