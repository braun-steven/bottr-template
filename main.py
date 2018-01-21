import argparse
import logging
from typing import List

import praw
from bottr.util import init_reddit, get_subs

from botname.bot import *
from botname.utils.args import parse_arg


def main(reddit: praw.Reddit, subs: List[str], opts: argparse.Namespace):
    """Main"""


if __name__ == '__main__':
    opts = parse_arg()
    handlers = [logging.FileHandler(opts.log)]

    if opts.debug:
        handlers.append(logging.StreamHandler())

    logging.basicConfig(level=logging.getLevelName(opts.log_level),
                        format='%(asctime)s [%(name)-12.12s] [%(levelname)-5.5s]  %(message)s',
                        handlers=handlers)

    # Get reddit session
    reddit = init_reddit()

    # Get subs
    subs = get_subs()

    # Run test comment if available
    if opts.test_comment is not None:
        opts.debug = True
        comment = reddit.comment(opts.test_comment)
        process_comment(comment, opts)
        exit(0)

    # Run test submission if available
    if opts.test_submission is not None:
        opts.debug = True
        submission = reddit.submission(opts.test_submission)
        process_submission(submission, opts)
        exit(0)

    main(reddit, subs, opts)
    exit(0)
