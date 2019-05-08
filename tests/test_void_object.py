from void_object import __version__, Void
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_call():
    try:
        v = Void()
        v()
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_attr():
    try:
        v = Void()
        v.asd
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_context():
    try:
        v = Void()
        with v as mgr:
            mgr.asd
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_getitem():
    try:
        v = Void()
        v['asd'][1]
    except Exception:
        pytest.fail("Unexpected Exception ..")
