from pathlib import Path

import pytest

from gendiff import generate_diff


def test_generate_diff():
    base_path = Path('tests/test_data')

    expected = (base_path / 'expected.txt').read_text()

    result = generate_diff(
        base_path / 'file1.json',
        base_path / 'file2.json',
    )

    assert result == expected


def test_generate_diff_yaml():
    base_path = Path('tests/test_data')

    expected = (base_path / 'expected.txt').read_text()

    result = generate_diff(
        base_path / 'file1.yml',
        base_path / 'file2.yml',
    )

    assert result == expected


def test_generate_diff_plain():
    base_path = Path('tests/test_data')

    expected = (base_path / 'plain_expected.txt').read_text()

    result = generate_diff(
        base_path / 'file1.json',
        base_path / 'file2.json',
        'plain',
    )

    assert result == expected


def test_generate_diff_json():
    base_path = Path('tests/test_data')

    expected = (base_path / 'json_expected.txt').read_text()

    result = generate_diff(
        base_path / 'file1.json',
        base_path / 'file2.json',
        'json',
    )

    assert result == expected


def test_generate_diff_unknown_format():
    base_path = Path('tests/test_data')

    with pytest.raises(ValueError, match='Unknown format'):
        generate_diff(
            base_path / 'file1.json',
            base_path / 'file2.json',
            'unknown',
        )
