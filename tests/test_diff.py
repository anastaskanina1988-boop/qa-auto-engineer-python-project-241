from pathlib import Path

from hexlet_code import generate_diff


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