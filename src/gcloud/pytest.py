import logging
import subprocess

logger = logging.getLogger(__name__)


# gcloudコマンドを実行する関数
def run_gcloud_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output


def test_run_gcloud_command():
    output = run_gcloud_command("gcloud config list")
    logger.info(f"### output: {output}")
    assert b"1.is.universe@gmail.com" in output
