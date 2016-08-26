import argparse

def get_args():
    """Parse command line arguments """
    parser = argparse.ArgumentParser(description="Average multiple images")
    subparsers = parser.add_subparsers(dest='mode',
            help='Use images from a local dir or download new images')
    subparsers.required = True

    # Parent parser
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        '--output', '-o', type=str, default='output',
       help='file to output the image to')
    parent_parser.add_argument(
        '--offset', '-f', type=int,
        default=0, help='add a value to all pixels')

    # Local directory parser
    parser_local = subparsers.add_parser(
        'local', help='Directory to combine images from', parents=[parent_parser])
    parser_local.add_argument(
        'dir', type=str, help='dir to fetch images from')

    # Download parser
    parser_download = subparsers.add_parser(
        'download', help="Keywords for images to search for and filename",
        parents=[parent_parser])
    parser_download.add_argument(
        "terms", type=str, help="Keywords for images to search for and filename")
    parser_download.add_argument(
        '--count', '-c', type=int,
        default=10, help='number of photos to be combined')

    return parser.parse_args()
