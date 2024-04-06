from pytest_mock import MockerFixture
from geojson2osm.__main__ import main


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
    assert file == '<osm version="0.6" generator="geojson2osm">'
