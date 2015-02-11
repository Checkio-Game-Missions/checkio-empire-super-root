"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": 4,
            "answer": 4,
            "show": 2.0
        },
        {
            "input": 27,
            "answer": 27,
            "show": 3.0
        },
        {
            "input": 81,
            "answer": 81,
            "show": 3.504336
        },

    ],
    "Edge": [
        {
            "input": 1,
            "answer": 1,
            "show": 1.0
        },
        {
            "input": 2,
            "answer": 2,
            "show": 1.55948
        },
        {
            "input": 10000000000,
            "answer": 10000000000,
            "show": 10.0
        },
        {
            "input": 9999999999,
            "answer": 9999999999,
            "show": 9.99999999996971
        },
    ],
    "Extra": [
        {
            "input": 3125,
            "answer": 3125,
            "show": 5.0
        },
        {
            "input": 823543,
            "answer": 823543,
            "show": 7.0
        },
        {
            "input": 387420489,
            "answer": 387420489,
            "show": 9.0
        },
        {
            "input": 5591410308,
            "answer": 5591410308,
            "show": 9.82349569660579
        },
        {
            "input": 3599715496,
            "answer": 3599715496,
            "show": 9.6891487943711
        },
        {
            "input": 6753053087,
            "answer": 6753053087,
            "show": 9.88091076711623
        },
        {
            "input": 1490925654,
            "answer": 1490925654,
            "show": 9.41850635493766
        },
        {
            "input": 4673126110,
            "answer": 4673126110,
            "show": 9.76883272752724
        },
        {
            "input": 42,
            "answer": 42,
            "show": 3.207193
        },
    ]
}
