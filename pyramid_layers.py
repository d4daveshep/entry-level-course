import pytest

# calculate how high we can build a 2-D pyramid with a given number of bricks
def calc_layers(bricks):
    layers = 0

    while bricks > layers:
        layers += 1
        bricks -= layers

        print("layers built:", layers, "bricks left:", bricks)
        if bricks < layers + 1:
            print("can't complete next layer with only", bricks, "bricks")
            break

    return layers


def test_calc_layers():
    assert (3 == calc_layers(6))
    assert (5 == calc_layers(20))
    assert (44 == calc_layers(1000))
    assert (1 == calc_layers(2))
