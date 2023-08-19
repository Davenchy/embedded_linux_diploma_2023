#!/usr/bin/env python3
"""Script to suggest activity"""
import requests
import argparse

BORED_API_ENDPOINT = "https://www.boredapi.com/api/activity"


class FailedException(Exception):
    pass


class NoActivityException(Exception):
    pass


def get_activity(participants=1, activity_type=None):
    """Get the activities nearby the user's location

    Check docs of the Bored API for more information about the returned data

    Args:
        participants (int): Number of participants
        activity_type (str): Type of activity, could be 'education',
            'recreational', 'social', 'diy', 'charity', 'cooking',
            'relaxation', 'music', 'busywork'

    Raises: FailedException if the request failed
    Raises: NoActivityException if no activity was found

    Returns: dict"""
    res = requests.get(BORED_API_ENDPOINT, params={
        "participants": participants,
        "type": activity_type
    })
    if res.status_code != 200:
        raise FailedException

    data = res.json()
    if "error" in data.keys():
        raise NoActivityException

    return data


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument(
        "-p", "--participants", type=int, default=1,
        help="Number of participants",
        required=False,
    )

    arg.add_argument(
        "-t", "--type", type=str, default=None,
        help="Type of activity",
        required=False,
        choices=[
            "education", "recreational", "social", "diy", "charity", "cooking",
            "relaxation", "music", "busywork"
        ]
    )

    args = arg.parse_args()

    try:
        activity = get_activity(args.participants, args.type)
    except FailedException:
        print("Failed to find activity")
        exit(1)
    except NoActivityException:
        print("No activity found")
        exit(1)

    print("Activity category: " + activity["type"])
    print("Suggested activity: " + activity["activity"])

    if "link" in activity.keys() and len(activity["link"]) > 0:
        print("Link: " + activity["link"])
