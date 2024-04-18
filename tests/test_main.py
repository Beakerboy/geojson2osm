import pytest
from pytest_mock import MockerFixture
from geojson2osm.__main__ import main


@pytest.fixture(autouse=True)
def run_around_tests() -> Generator:
    # Code that will run before your test, for example:
    # A test function will be run at this point
    yield
    # Code that will run after your test:
    p = Path("output.xml")
    p.unlink()


def test_main(mocker: MockerFixture) -> None:
    mocker.patch(
        "sys.argv",
        [
            "geojson2osm",
            "tests/files/input.geojson",
            "output.xml"
        ],
    )
    main()
    f = open("output.xml", "r")
    file = f.read()
    f1 = open("tests/files/output.xml", "r")
    expected = f1.read()
    assert file == expected


def test_multipolygon(mocker: MockerFixture) -> None:
    mocker.patch(
        "sys.argv",
        [
            "geojson2osm",
            "tests/files/Bug_multi.geojson",
            "output.xml"
        ],
    )
    main()
