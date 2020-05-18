import datetime
import pytest
from nadar import (
    SmartDate,
    SmartPeriod,
    delta_date,
    get_end,
    get_start,
    parse_period,
    parse_reference,
)


@pytest.mark.parametrize(
    "expected, date, period",
    [
        ("2018-01-01", "2018-03-28", "year"),
        ("2017-01-01", "2017-03-28", "year"),
        ("2016-01-01", "2016-08-28", "year"),
        (datetime.date(2018, 1, 1), datetime.date(2018, 3, 28), "year"),
        (datetime.date(2017, 1, 1), datetime.date(2017, 3, 28), "year"),
        (datetime.date(2016, 1, 1), datetime.date(2016, 8, 28), "year"),
        (SmartDate(2018, 1, 1), SmartDate(2018, 3, 28), "year"),
        (SmartDate(2017, 1, 1), SmartDate(2017, 3, 28), "year"),
        (SmartDate(2016, 1, 1), SmartDate(2016, 8, 28), "year"),
        ("2018-01-01", "2018-03-28", "quarter"),
        ("2017-01-01", "2017-03-28", "quarter"),
        ("2017-07-01", "2017-08-28", "quarter"),
        (datetime.date(2018, 1, 1), datetime.date(2018, 3, 28), "quarter"),
        (datetime.date(2017, 1, 1), datetime.date(2017, 3, 28), "quarter"),
        (datetime.date(2017, 7, 1), datetime.date(2017, 8, 28), "quarter"),
        (SmartDate(2018, 1, 1), SmartDate(2018, 3, 28), "quarter"),
        (SmartDate(2017, 1, 1), SmartDate(2017, 3, 28), "quarter"),
        (SmartDate(2017, 7, 1), SmartDate(2017, 8, 28), "quarter"),
        ("2018-03-01", "2018-03-28", "month"),
        ("2017-03-01", "2017-03-28", "month"),
        ("2017-08-01", "2017-08-28", "month"),
        (datetime.date(2018, 3, 1), datetime.date(2018, 3, 28), "month"),
        (datetime.date(2017, 3, 1), datetime.date(2017, 3, 28), "month"),
        (datetime.date(2017, 8, 1), datetime.date(2017, 8, 28), "month"),
        (SmartDate(2018, 3, 1), SmartDate(2018, 3, 28), "month"),
        (SmartDate(2017, 3, 1), SmartDate(2017, 3, 28), "month"),
        (SmartDate(2017, 8, 1), SmartDate(2017, 8, 28), "month"),
        ("2018-03-26", "2018-03-28", "week"),
        ("2018-02-12", "2018-02-15", "week"),
        ("2018-01-01", "2018-01-01", "week"),
        (datetime.date(2018, 3, 26), datetime.date(2018, 3, 28), "week"),
        (datetime.date(2018, 2, 12), datetime.date(2018, 2, 15), "week"),
        (datetime.date(2018, 1, 1), datetime.date(2018, 1, 1), "week"),
        (SmartDate(2018, 3, 26), SmartDate(2018, 3, 28), "week"),
        (SmartDate(2018, 2, 12), SmartDate(2018, 2, 15), "week"),
        (SmartDate(2018, 1, 1), SmartDate(2018, 1, 1), "week"),
    ],
)
def test_get_start(expected, date, period):
    result = get_start(period, date)
    assert expected == result
    assert isinstance(result, type(expected))


@pytest.mark.parametrize(
    "expected, date, period",
    [
        ("2018-12-31", "2018-03-28", "year"),
        ("2017-12-31", "2017-03-28", "year"),
        ("2016-12-31", "2016-08-28", "year"),
        (datetime.date(2018, 12, 31), datetime.date(2018, 3, 28), "year"),
        (datetime.date(2017, 12, 31), datetime.date(2017, 3, 28), "year"),
        (datetime.date(2016, 12, 31), datetime.date(2016, 8, 28), "year"),
        (SmartDate(2018, 12, 31), SmartDate(2018, 3, 28), "year"),
        (SmartDate(2017, 12, 31), SmartDate(2017, 3, 28), "year"),
        (SmartDate(2016, 12, 31), SmartDate(2016, 8, 28), "year"),
        ("2018-03-31", "2018-03-28", "quarter"),
        ("2017-03-31", "2017-03-28", "quarter"),
        ("2017-09-30", "2017-08-28", "quarter"),
        ("2017-12-31", "2017-12-28", "quarter"),
        (datetime.date(2018, 3, 31), datetime.date(2018, 3, 28), "quarter"),
        (datetime.date(2017, 3, 31), datetime.date(2017, 3, 28), "quarter"),
        (datetime.date(2017, 9, 30), datetime.date(2017, 8, 28), "quarter"),
        (datetime.date(2017, 12, 31), datetime.date(2017, 12, 28), "quarter"),
        (SmartDate(2018, 3, 31), SmartDate(2018, 3, 28), "quarter"),
        (SmartDate(2017, 3, 31), SmartDate(2017, 3, 28), "quarter"),
        (SmartDate(2017, 9, 30), SmartDate(2017, 8, 28), "quarter"),
        (SmartDate(2017, 12, 31), SmartDate(2017, 12, 28), "quarter"),
        ("2018-03-31", "2018-03-28", "month"),
        ("2017-03-31", "2017-03-28", "month"),
        ("2017-08-31", "2017-08-28", "month"),
        (datetime.date(2018, 3, 31), datetime.date(2018, 3, 28), "month"),
        (datetime.date(2017, 3, 31), datetime.date(2017, 3, 28), "month"),
        (datetime.date(2017, 8, 31), datetime.date(2017, 8, 28), "month"),
        (SmartDate(2018, 3, 31), SmartDate(2018, 3, 28), "month"),
        (SmartDate(2017, 3, 31), SmartDate(2017, 3, 28), "month"),
        (SmartDate(2017, 8, 31), SmartDate(2017, 8, 28), "month"),
        ("2018-04-01", "2018-03-28", "week"),
        ("2018-02-18", "2018-02-15", "week"),
        ("2018-01-07", "2018-01-01", "week"),
        (datetime.date(2018, 4, 1), datetime.date(2018, 3, 28), "week"),
        (datetime.date(2018, 2, 18), datetime.date(2018, 2, 15), "week"),
        (datetime.date(2018, 1, 7), datetime.date(2018, 1, 1), "week"),
        (SmartDate(2018, 4, 1), SmartDate(2018, 3, 28), "week"),
        (SmartDate(2018, 2, 18), SmartDate(2018, 2, 15), "week"),
        (SmartDate(2018, 1, 7), SmartDate(2018, 1, 1), "week"),
    ],
)
def test_get_end(expected, date, period):
    result = get_end(period, date)
    assert expected == result
    assert isinstance(result, type(expected))


@pytest.mark.parametrize(
    "expected, date, years, months, days",
    [
        ("2018-04-05", "2018-03-30", 0, 0, 6),
        ("2018-02-28", "2018-03-31", 0, -1, 0),
        (datetime.date(2018, 4, 5), datetime.date(2018, 3, 30), 0, 0, 6),
        (datetime.date(2018, 2, 28), datetime.date(2018, 3, 31), 0, -1, 0),
        (SmartDate(2018, 4, 5), SmartDate(2018, 3, 30), 0, 0, 6),
        (SmartDate(2018, 2, 28), SmartDate(2018, 3, 31), 0, -1, 0),
    ],
)
def test_delta_date(expected, date, years, months, days):
    result = delta_date(date, years=years, months=months, days=days)
    assert expected == result
    assert isinstance(result, type(expected))


@pytest.mark.parametrize(
    "expected, text, reference",
    [
        (SmartDate(2017, 5, 8), "one year ago", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 2, 8), "three months ago", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 5, 3), "five days ago", datetime.date(2018, 5, 8)),
        (SmartDate(2017, 11, 8), "two quarters ago", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 5, 7), "yesterday", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 5, 8), "today", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 5, 9), "tomorrow", datetime.date(2018, 5, 8)),
        (SmartDate(2018, 5, 8), "2018-05-08", datetime.date(2018, 5, 8)),
    ],
)
def test_parse_reference(expected, text, reference):
    assert expected == parse_reference(text, reference)


@pytest.mark.parametrize(
    "expected, text, reference",
    [
        (
            SmartPeriod(SmartDate(2018, 4, 1), SmartDate(2018, 4, 30)),
            "last month",
            datetime.date(2018, 5, 8),
        ),
        (
            SmartPeriod(SmartDate(2018, 5, 7), SmartDate(2018, 5, 7)),
            "this week",
            datetime.date(2018, 5, 8),
        ),
        (
            SmartPeriod(SmartDate(2017, 1, 1), SmartDate(2017, 12, 31)),
            "last year",
            datetime.date(2018, 5, 8),
        ),
        (
            SmartPeriod(SmartDate(2017, 1, 1), SmartDate(2017, 3, 31)),
            "last quarter",
            datetime.date(2017, 5, 3),
        ),
        (
            SmartPeriod(SmartDate(2017, 7, 1), SmartDate(2017, 9, 30)),
            "next quarter",
            datetime.date(2017, 5, 3),
        ),
        (
            SmartPeriod(SmartDate(2018, 1, 1), SmartDate(2018, 12, 31)),
            "next year",
            datetime.date(2017, 5, 3),
        ),
        (
            SmartPeriod(SmartDate(2017, 5, 4), SmartDate(2017, 5, 4)),
            "next day",
            datetime.date(2017, 5, 3),
        ),
        (
            SmartPeriod(SmartDate(2018, 4, 4), SmartDate(2018, 4, 9)),
            "between 15 and 10 days ago",
            datetime.date(2018, 4, 19),
        ),
        (
            SmartPeriod(SmartDate(2017, 11, 19), SmartDate(2018, 1, 19)),
            "between five and three months ago",
            datetime.date(2018, 4, 19),
        ),
    ],
)
def test_parse_period(expected, text, reference):
    assert expected == parse_period(text, reference)
