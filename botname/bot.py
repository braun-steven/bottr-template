import argparse
import logging

import praw


def parse_comment(comment: praw.models.Comment, opts: argparse.Namespace):
    """Process a comment"""
    logging.info('ID: {}'.format(comment.id))
    logging.info('Author: {}'.format(comment.author))
    logging.info('Body: {}'.format(comment.body))


def parse_submission(submission: praw.models.Submission, opts: argparse.Namespace):
    """Process a submission"""
    logging.info('ID: {}'.format(submission.id))
    logging.info('Author: {}'.format(submission.author))
    logging.info('Body: {}'.format(submission.title))
