"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                      ('2023-03-01 18:30', '2023-03-01 19:30', 'Asia/Tokyo')],
            "answer": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York')],
        },
        {
            "input": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                      ('2023-03-01 04:00', '2023-03-01 06:00', 'America/New_York')],
            "answer": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York')],
        },
        {
            "input": [('2023-03-01 08:00', '2023-03-01 09:00', 'America/New_York'),
                      ('2023-03-01 14:00', '2023-03-01 15:00', 'Asia/Tokyo')],
            "answer": [('2023-03-01 14:00', '2023-03-01 15:00', 'Asia/Tokyo'),
                       ('2023-03-01 08:00', '2023-03-01 09:00', 'America/New_York')],
        },
        {
            "input": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                      ('2023-03-01 04:30', '2023-03-01 05:30', 'America/New_York'),
                      ('2023-03-01 06:00', '2023-03-01 07:00', 'America/Chicago')],
            "answer": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                       ('2023-03-01 06:00', '2023-03-01 07:00', 'America/Chicago')],
        },
    ],
    "Extra": [
        {
            "input": [('2023-03-01 10:00', '2023-03-01 11:15', 'America/Los_Angeles'),
                      ('2023-03-01 08:30', '2023-03-01 10:00', 'Europe/London'),
                      ('2023-03-01 12:00', '2023-03-01 13:30', 'Asia/Kolkata'),
                      ('2023-03-01 11:00', '2023-03-01 12:00', 'America/New_York'),
                      ('2023-03-01 09:30', '2023-03-01 11:00', 'Australia/Sydney'),
                      ('2023-03-01 12:30', '2023-03-01 14:00', 'Asia/Tokyo'),
                      ('2023-03-01 08:45', '2023-03-01 09:45', 'Europe/London'),
                      ('2023-03-01 13:00', '2023-03-01 14:30', 'America/Los_Angeles'),
                      ('2023-03-01 11:30', '2023-03-01 12:45', 'Asia/Kolkata'),
                      ('2023-03-01 09:45', '2023-03-01 11:00', 'Australia/Sydney'),
                      ('2023-03-01 11:30', '2023-03-01 12:30', 'America/New_York'),
                      ('2023-03-01 10:30', '2023-03-01 12:00', 'Asia/Tokyo')],
            "answer": [('2023-03-01 09:30', '2023-03-01 11:00', 'Australia/Sydney'),
                       ('2023-03-01 10:30', '2023-03-01 12:00', 'Asia/Tokyo'),
                       ('2023-03-01 12:30', '2023-03-01 14:00', 'Asia/Tokyo'),
                       ('2023-03-01 11:30', '2023-03-01 12:45', 'Asia/Kolkata'),
                       ('2023-03-01 08:30', '2023-03-01 10:00', 'Europe/London'),
                       ('2023-03-01 11:00', '2023-03-01 12:00', 'America/New_York'),
                       ('2023-03-01 10:00', '2023-03-01 11:15', 'America/Los_Angeles'),
                       ('2023-03-01 13:00', '2023-03-01 14:30', 'America/Los_Angeles')],
        },
        {
            "input": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                      ('2023-03-01 04:30', '2023-03-01 05:30', 'America/New_York'),
                      ('2023-03-01 06:00', '2023-03-01 07:00', 'America/Chicago')],
            "answer": [('2023-03-01 04:00', '2023-03-01 05:00', 'America/New_York'),
                       ('2023-03-01 06:00', '2023-03-01 07:00', 'America/Chicago')],
        },
    ]
}
