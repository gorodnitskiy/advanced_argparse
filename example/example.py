from advanced_argparse import AdvancedParser
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s'
)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    example_cfg = './example_cfg.yaml'

    # Config with default values for params requires as
    # path to yaml file or Dict[str, Any]
    parser = AdvancedParser(cfg=example_cfg, logger=logger)

    # Set your own description of the parser
    # and set a description for any input parameters
    # ('help' attr in argparse.add_argument method)
    parser.set_parser_desc('New description for parser')
    parser.add_params_desc({'SPARK_HOME': 'path to spark_home'})

    # Use verbose option to manage parser silence
    args = parser.parse_args(verbose=True)

    logger.info('Initial config: {}'.format(parser.config))
    logger.info('Config with replacing values: {}'.format(args))
