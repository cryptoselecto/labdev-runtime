from labdev.cli import status

def test_status(capsys):
    # Call status() in the current repo
    status()

    # Capture printed output
    captured = capsys.readouterr()
    out = captured.out

    # Basic sanity checks on the output
    assert "Repo path:" in out
    assert "Current branch name:" in out
