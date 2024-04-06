import pytest
from pytest_mock import MockerFixture
from geojson2osm.__main__ import main


def test_main(mocker: MockerFixture) -> None:
    mocker.patch(
        "sys.argv",
        [
            "geojson2osm",
            "input.geojson",
            "output.xml"
        ],
    )
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"building": "yes"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [36.77125867456199, 37.2584759589531],
                            [36.77126068621875, 37.2584759589531],
                            [36.77126102149488, 37.258475158401765],
                            [36.771257668733604, 37.25847489155132],
                            [36.77125867456199, 37.2584759589531],
                        ]
                    ],
                },
            }
        ],
    }
    main()
    osm_xml = g2o(geojson_data)
    assert '<osm version="0.6" generator="geojson2osm">' in osm_xml
    assert '<tag k="building" v="yes" />' in osm_xml

    # Check for the presence of a way element with a closed loop
    way_pattern = re.compile(r'<way id="-\d+">.*?</way>', re.DOTALL)
    assert re.search(way_pattern, osm_xml)
