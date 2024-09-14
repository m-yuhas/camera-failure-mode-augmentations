import argparse
import logging


import coloredlogs


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Augment datasets with common camera failure modes')
    parser.add_argument(
        '--data-path',
        help='Path to the directory or directory tree of images to augment'
    )
    parser.add_argument(
        '--output-path',
        help='Output directory for augmented images'
    )
    parser.add_argument(
        '--blur',
        type=int,
        help='Intensity of Gaussian blur to apply'
    )
    parser.add_argument(
        '--verbosity',
        choices=['debug', 'info', 'warn', 'error']
        default='info',
        help='Logging verbosity.'
    )
    args = parser.parse_args()
    logger = logging.getLogger('CFM Augmentation')
    coloredlogs.install(level=args.verbosity.upper())
    