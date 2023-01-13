from unittest import mock

import pytest

from reproml import main


@mock.patch("sys.argv", " ")
def test_main():
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.type == SystemExit
    assert e.value.code == 0
