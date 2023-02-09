import sys
from subprocess import run

instance_name, zone_name = sys.argv[1:]


def get_external_ip(instance_name="airflow-server", zone_name="us-west1-b"):

    bash_command = f"gcloud compute instances describe {instance_name} --zone={zone_name} --format='value(networkInterfaces[0].accessConfigs[0].natIP)'"
    data = run(bash_command, capture_output=True, shell=True)
    return data.stdout.decode()[:-1]


if __name__ == "__main__":
    external_ip = get_external_ip(instance_name, zone_name)
